# coding=utf-8
from  collections import Counter, defaultdict

from qa.QuestionAnsweringSystem.const import Weights
from abstract_score import Score, ScoreWrapper


class WordFreqScore(Score):
    def __init__(self, q_in, a_in):
        super(WordFreqScore, self).__init__(q_in, a_in)
        self.weight = Weights.WordFreq.value

    def get_score(self):
        a_counter = Counter(self.parser_a)
        word_freq_dict = Counter()
        for word in self.parser_q:
            if a_counter.has_key(word):
                word_freq_dict[word] += (a_counter[word])
        tf = sum(a_counter.viewvalues())
        word_tf = sum(word_freq_dict.values())
        return (word_tf, self.weight)


class WordFreqScoreWrapper(ScoreWrapper):
    def __init__(self):
        super(WordFreqScoreWrapper, self).__init__()
        pass

    def get_evi_score_list(self, q_in, a_list):
        evidence_score = defaultdict()
        for id, ans in a_list.items():
            bs_obj = WordFreqScore(q_in, ans)
            score, weight = bs_obj.get_score()
            evidence_score[int(id)] = score*weight
        return evidence_score


if __name__ == '__main__':
    parser_q = [u'我', '们']
    a = u'你问我爱你有多深'
    a_counter = Counter(a)
    print  a_counter.get(u'我')

    ret1 = filter(lambda x: x in parser_q, a_counter)
    print str(ret1).replace('u\'', '\'').decode('unicode-escape')

    print a_counter.values()
    print a_counter.viewvalues()

    a = {'a': 2, 'b': 3, 'c': 4}
    print a.values()
    print float(float(1) / 3)
