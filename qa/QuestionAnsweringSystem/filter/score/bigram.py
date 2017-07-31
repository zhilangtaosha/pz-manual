# coding=utf-8

from collections import Counter,defaultdict

from qa.QuestionAnsweringSystem.const import Weights
from abstract_score import Score, ScoreWrapper


class BiagramScore(Score):
    def __init__(self, q_in, a_in):
        super(BiagramScore, self).__init__(q_in, a_in)
        self.weight = Weights.Biagram.value

    def get_score(self):
        word_bigram_a = zip(*[self.parser_a[i:] for i in range(2)])
        word_bigram_q = zip(*[self.parser_q[i:] for i in range(2)])
        bigram_counter_q = Counter(word_bigram_q)
        bigram_counter_a = Counter(word_bigram_a)
        score = 0
        # print str(bigram_counter_a).replace('u\'', '\'').decode('unicode-escape')
        for bi in bigram_counter_q.iterkeys():
            # print str(bi).replace('u\'','\'').decode('unicode-escape')
            if bi in bigram_counter_a.iterkeys():
                score += 2

        return (score, self.weight)


class BiagramScoreWrapper(ScoreWrapper):
    def __init__(self):
        super(BiagramScoreWrapper, self).__init__()

    def get_evi_score_list(self, q_in, a_list):
        # evidence_score=defaultdict(dict)
        evidence_score = defaultdict(dict)
        for id, ans in a_list.iteritems():
            # print id,ans
            bs_obj = BiagramScore(q_in, ans)
            score, weight = bs_obj.get_score()
            evidence_score[id] = score * weight
        return evidence_score


if __name__ == '__main__':
    parser_a = ['what', 'a', 'fuck', 'day', 'how', 'are', 'you', 'what', 'a']
    parser_q = ['what', 'a', 'fuck', 'day', 'how', 'are', 'you', 'what', 'a']
    from collections import defaultdict


    def get_score():
        word_bigram_a = zip(*[parser_a[i:] for i in range(2)])
        word_bigram_q = zip(*[parser_q[i:] for i in range(2)])
        bigram_counter_q = Counter(word_bigram_q)
        bigram_counter_a = Counter(word_bigram_a)
        score = 0
        for bi in bigram_counter_q.iterkeys():
            if bi in bigram_counter_a.iterkeys():
                score += 2
                # print score


    get_score()
