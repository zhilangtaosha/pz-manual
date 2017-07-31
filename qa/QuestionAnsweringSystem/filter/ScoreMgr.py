# coding=utf-8
from collections import Counter

from qa.QuestionAnsweringSystem.filter.score.score_cls import ScoreList


class ScoreManager(object):
    def __init__(self, q_in, evidence_list):
        self.evidence_list = evidence_list
        self.question = q_in

    def score_topn(self, topn):
        evi_score_dict = Counter()
        for score_met in ScoreList:
            methodwrapper = score_met()
            evi_score = methodwrapper.get_evi_score_list(self.question, self.evidence_list)
            evi_score_dict.update(evi_score)
        # print evi_score_dict
        return evi_score_dict.most_common(topn)
