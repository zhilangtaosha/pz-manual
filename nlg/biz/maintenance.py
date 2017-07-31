# _*_ coding: utf-8 _*_


from conf.const import *
from data.graph import graph_search
from data.rdb import db_query
from nlg.generation import Generation


class MaintenanceGeneration(Generation):
    """"""

    def __init__(self):
        Generation.__init__(self)
        self._topicid = TopicID.MaintenanceTopic

    def generate(self):
        super(MaintenanceGeneration, self).generate()
        semantic = self.topic.get_semantic()
        sql = 'SELECT id, %s FROM gs8_maintenance AS m WHERE m.name = "%s"' % (
            semantic.slots[PROPERTY], semantic.slots[KG_NAME])
        data = db_query.get(sql)
        result = {}
        if len(data) > 0:
            if dict(data[0])[semantic.slots[PROPERTY]].strip() == '':
                pass
            else:
                result['data'] = dict(data[0])[semantic.slots[PROPERTY]]
                result['id'] = dict(data[0])['id']
                result['field'] = semantic.slots[PROPERTY]
        self._response.set_slots(semantic.slots)
        self._response.set_text(self.topic.get_query_info().get_text())
        self._response.set_topic_intent(DOMAIN_MAINTENANCE, INTENT_QUERY)
        self._response.set_answer(result)
        self.topic.end()
        return self._response

