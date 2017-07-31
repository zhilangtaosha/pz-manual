# _*_ coding: utf-8 _*_
import collections
import operator
from conf.const import *
from nlg.generation import Generation
from data.graph import graph_search
from data.rdb import db_query
from utils.util import calc_sim


class BrokenDownGeneration(Generation):
    """"""

    def __init__(self):
        Generation.__init__(self)
        self._topicid = TopicID.BrokenDownTopic

    @staticmethod
    def sql(part_item, phen_item):
        sql = 'SELECT image, reason, method, query FROM gs8_fault AS t WHERE t.part="%s" AND t.phen="%s"' % (
            part_item, phen_item)
        return sql

    def answer(self, data_q, answer, query):
        for item in data_q:
            data = dict(item)
            result = {}
            similarity = calc_sim(data['query'], query)
            if similarity > 80:
                self.append(result, data, similarity)
                answer.append(result)

    @staticmethod
    def append(result, data, similarity):
        result['data'] = ''
        result['reason'] = data['reason']
        result['method'] = data['method']
        result['image'] = data['image']
        result['sim'] = similarity

    def cal_sim(self, answer, query):
        sql = 'SELECT image, reason, method, query FROM gs8_fault '
        data = db_query.get(sql)
        for item in data:
            data = dict(item)
            similarity = calc_sim(data['query'], query)
            if similarity >= 90:
                result = {}
                self.append(result, data, similarity)
                answer.append(result)
                break

    @staticmethod
    def cal_sim_0(part, phen, answer, query):
        for part_item in part:
            for phen_item in phen:
                sql = 'SELECT image, reason, method, query FROM gs8_fault AS t WHERE t.part="%s" AND t.phen="%s"' % (
                    part_item, phen_item)
                result = ''
                data = db_query.get(sql)
                for item in data:
                    data = dict(item)
                    similarity = calc_sim(data['query'], query)
                    if similarity > 50:
                        result = {}
                        result['data'] = ''
                        result['reason'] = data['reason']
                        result['method'] = data['method']
                        result['image'] = data['image']
                        answer.append(result)
        if answer:
            return answer[0]
        else:
            return answer

    def generate(self):
        super(BrokenDownGeneration, self).generate()
        query = self.topic.get_query_info().get_text()
        semantic = self.topic.get_semantic()
        part = semantic.slots[AUTO_PART]
        phen = semantic.slots[AUTO_PHEN]
        stints = semantic.slots[STINTS]
        answer = []
        if all([part, phen]):
            for part_item in part:
                for phen_item in phen:
                    if not stints:
                        sql = self.sql(part_item, phen_item)
                    else:
                        placeholder = []
                        for k, v in stints.items():
                            placeholder.append(' AND %s="%s"' % (k, v))
                        rel_property = "".join(placeholder)
                        sql = 'SELECT image, reason, method, query FROM gs8_fault  WHERE part="%s" AND phen="%s"' % (
                            part_item, phen_item) + rel_property
                    data_q = db_query.get(sql)
                    if data_q:
                        self.answer(data_q, answer, query)
                    else:
                        data_q = db_query.get(self.sql(part_item, phen_item))
                        if data_q:
                            self.answer(data_q, answer, query)
            if not answer:
                self.cal_sim(answer, query)
        elif all([len(part) == 0, len(phen) >= 1]):
            for phen_item in phen:
                sql = 'SELECT image, reason, method, query FROM gs8_fault AS t WHERE t.part="车体" AND t.phen="%s"' % phen_item
                data = db_query.get(sql)
                if len(data) > 0:
                    for item in data:
                        data = dict(item)
                        result = {}
                        similarity = calc_sim(data['query'], query)
                        if similarity > 50:
                            self.append(result, data, similarity)
                            answer.append(result)
                    if not answer:
                        self.cal_sim(answer, query)
                else:
                    self.cal_sim(answer, query)
        elif all([len(part) >= 1, len(phen) == 0]):
            for part_item in part:
                sql = 'SELECT image, reason, method, query FROM gs8_fault AS t WHERE  t.part="%s"' % part_item
                data = db_query.get(sql)
                if len(data) > 0:
                    for item in data:
                        data = dict(item)
                        result = {}
                        similarity = calc_sim(data['query'], query)
                        if similarity > 50:
                            self.append(result, data, similarity)
                            answer.append(result)
                            break
        else:
            self.cal_sim(answer, query)
        answer = sorted(answer, key=operator.itemgetter('sim'), reverse=True)
        answer_ = answer[0] if answer else self.cal_sim_0(part, phen, answer, query)
        self._response.set_text(query)
        self._response.set_topic_intent(DOMAIN_BROKENDOWN, INTENT_QUERY)
        self._response.set_answer(answer_)
        self.topic.end()
        return self._response
