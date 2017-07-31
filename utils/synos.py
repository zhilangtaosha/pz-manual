# _*_ coding: utf-8 _*_

from fuzzywuzzy import fuzz

from conf.syno import *


class Syno(object):
    """

    """

    def __init__(self):
        pass

    @staticmethod
    def get(sentence):
        score = -1
        sentid = -1
        for k, sents in syno_query.items():
            for s in sents:
                sco = fuzz.ratio(sentence.encode('utf-8'), s)
                # sco = get_sim_score(sentence, s)
                if sco > score and sco > 65:  # 阈值
                    score = sco
                    sentid = k
        if  sentid == -1:
            return sentid,sentence.encode("utf-8")
        return sentid, std_query[sentid]


syno = Syno()
