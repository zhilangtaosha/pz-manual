# coding=utf-8
import abc

from qa.QuestionAnsweringSystem.common.exception import CustomException


class Score(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, q_in, a_in):
        self.quetion = q_in
        self.answer = a_in
        self.parser_q = q_in
        self.parser_a = a_in

        self.weight = None

    @abc.abstractmethod
    def get_score(self):
        raise CustomException('%s does not instantiate method "get_score".' % self.__class__.__name__)


class ScoreWrapper(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, evi_list=None):
        self.evi_list = evi_list

    @abc.abstractmethod
    def get_evi_score_list(self, q_in, a_list):
        raise CustomException('%s does not instantiate method "get_evi_score_list".' % self.__class__.__name__)
