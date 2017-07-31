# coding=utf-8

from collections import Counter, defaultdict

from qa.QuestionAnsweringSystem.const import Weights
from abstract_score import Score, ScoreWrapper


class SkipBiagramScore(Score):
    def __init__(self, q_in, a_in):
        super(SkipBiagramScore, self).__init__(q_in, a_in)
        self.weight = Weights.SkipBiagram.value

    @staticmethod
    def to_ngrams(unigrams, length):
        return zip(*[unigrams[i:] for i in range(length)])

    def get_score(self):
        skip_bigram_info = defaultdict(lambda: defaultdict(Counter))
        score = 0
        ngram_counts = defaultdict(Counter)
        tri_list_a = self.to_ngrams(self.parser_a, 3)
        tri_list_q = self.to_ngrams(self.parser_q, 3)
        ngram_counts[3].update(tri_list_a)
        for ngram, count in ngram_counts[3].items():
            if ngram in tri_list_q:
                skip_bigram_info[ngram[0]][ngram[-1]] += Counter({2: count})
                skip_bigram_info[ngram[-1]][ngram[0]] += Counter({-2: count})
                score += 2
        return (score, self.weight)


class SkipBiagramWrapper(ScoreWrapper):
    def __init__(self):
        super(SkipBiagramWrapper, self).__init__()

    def get_evi_score_list(self, q_in, a_list):
        evidence_score = defaultdict(dict)
        for id, ans in a_list.iteritems():
            bs_obj = SkipBiagramScore(q_in, ans)
            score, weight = bs_obj.get_score()
            evidence_score[id] = score * weight
        return evidence_score
