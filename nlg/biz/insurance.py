# _*_ coding: utf-8 _*_

from conf.const import *
from nlg.generation import Generation
from data.graph import graph_search
from data.rdb import db_query


class InsuranceGeneration(Generation):
    """"""

    def __init__(self):
        Generation.__init__(self)
        self._topicid = TopicID.InsuranceTopic

    def generate(self):
        super(InsuranceGeneration, self).generate()
        semantic = self.topic.get_semantic()
        if semantic.slots[KG_NAME] == '*':
            nodes = graph_search.get_nodes(semantic.slots[KG_TYPE])
            result = []
            for node in nodes:
                result.append(node[KG_NAME])
            self._response.set_slots(semantic.slots)
            self._response.set_text(self.topic.get_query_info().get_text())
            self._response.set_topic_intent(DOMAIN_INSURANCE, INTENT_QUERY)
            self._response.set_answer(', '.join(result))
        else:
            if semantic.domain == DOMAIN_INSURANCE_COMPANY:
                sql = 'SELECT id, %s FROM gs8_insurance_company AS ic WHERE ic.name = "%s"' % (
                    semantic.slots[PROPERTY], semantic.slots[KG_NAME]
                )
            elif semantic.domain == DOMAIN_INSURANCE:
                sql = 'SELECT id, %s FROM gs8_insurance AS ic WHERE ic.name = "%s"' % (
                    semantic.slots[PROPERTY], semantic.slots[KG_NAME]
                )
            else:
                self.topic.end()
                return self._response
            data = db_query.get(sql)
            result = {}
            if len(data) > 0:
                result['id'] = dict(data[0])['id']
                result['data'] = dict(data[0])[semantic.slots[PROPERTY]]
                result['field'] = semantic.slots[PROPERTY]
            self._response.set_slots(semantic.slots)
            self._response.set_text(self.topic.get_query_info().get_text())
            self._response.set_topic_intent(semantic.domain, semantic.intent)
            self._response.set_answer(result)
        self.topic.end()
        return self._response
