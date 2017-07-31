# _*_ coding: utf-8 _*_

from conf.const import *
from nlg.generation import Generation
from qa.QuestionAnsweringSystem.datasource.CandidateEvidence import CandidateEvidence
from utils.util import calc_sim

evi_dict = CandidateEvidence.read_resource_all()


class QASysGeneration(Generation):
    """"""

    def __init__(self):
        Generation.__init__(self)
        self._topicid = TopicID.QAService

    def generate(self):
        super(QASysGeneration, self).generate()
        semantic = self.topic.get_semantic()
        qid_list = semantic.slots['qid_list']
        qid = semantic.slots['qid']
        query = self.topic.get_query_info().get_text()
        self._response.set_text(query)
        self._response.set_topic_intent(semantic.domain, semantic.intent)
        if qid != '':
            if not str(qid).isdigit():
                answer = CandidateEvidence.id2str(int(qid), flag=1)
                if calc_sim(answer, query) > 90:
                    answer = CandidateEvidence.id2str(int(qid), flag=2)
                    answer = {"data": answer, "id": qid}
                    self._response.set_answer(answer)
                    self.topic.end()
                    self.topic.set_stateid(TopicStateID.Null)
                else:
                    self._response.set_answer({})
            else:
                answer = CandidateEvidence.id2str(int(qid), flag=2)
                answer = {"data": answer, "id": qid}
                self._response.set_answer(answer)
                self.topic.end()
                self.topic.set_stateid(TopicStateID.Null)
        elif len(qid_list) == 0:
            self._response.set_answer({})
        else:
            qestion_list = []
            for qid in qid_list:
                question = CandidateEvidence.id2str(qid, flag=1)
                qestion_list.append(question)
            self._response.set_data({'title': '请选择您想咨询问题',
                                     'list': qestion_list,
                                     'uplist': qid_list})
            self.topic.set_stateid(TopicStateID.SelectQaOption)
            self.response.set_state_code(StateCode.Interactive)
        return self._response
