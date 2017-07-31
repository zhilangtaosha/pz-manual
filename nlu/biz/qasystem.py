# _*_ coding: utf-8 _*_


from conf.const import *
from nlu.topic import Topic
from qa.QuestionAnsweringSystem.const import ThresholdValue
from qa.QuestionAnsweringSystem.datasource.CandidateEvidence import CandidateEvidence
from qa.QuestionAnsweringSystem.filter.ScoreMgr import ScoreManager
from qa.QuestionAnsweringSystem.filter.parser.ParserWord import wordParser

evi_dict = CandidateEvidence.read_resource_all()


class QASysTopic(Topic):
    def __init__(self):
        Topic.__init__(self)
        self._topicid = TopicID.QAService

    def parse(self, query_info):
        super(QASysTopic, self).parse(query_info)
        query_info = query_info.get_text()
        semantic = self.get_semantic()
        semantic.domain = DOAMIN_QA
        semantic.intent = INTENT_QUERY
        semantic.add('qid', '')
        if self.stateid == TopicStateID.Null:
            que_in = wordParser.parse(query_info)
            sm = ScoreManager(que_in, evi_dict)
            score_evi = sm.score_topn(TopN)
            qid_list = [k1 for (k1, k2) in score_evi if k2 > ThresholdValue]
            semantic.add('qid_list', qid_list)
            if len(qid_list) == 1:
                semantic.add('qid', qid_list[0])
            return True
        elif self.stateid == TopicStateID.SelectQaOption:
            qid_list = semantic.get('qid_list')
            if not query_info.isdigit():
                semantic.add('qid', '')
                self.set_stateid(TopicStateID.Null)
                return False
            qid = int(query_info)
            if qid in qid_list:
                semantic.add('qid', qid)
                return True
