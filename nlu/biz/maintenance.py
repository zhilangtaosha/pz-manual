# _*_ coding: utf-8 _*_

from conf.const import *
from data.graph import graph_search
from nlu.topic import Topic

project_syno = {
    'consequence': {'后果': 1, '坏处': 1, '损伤': 1, '隐患': 1, '现象': 1, '怎么样': 1, '怎样': 1, '问题': 1},
    'function': {'作用': 1},
    'period': {'周期': 1, '多久': 1, '多长': 1, '公里': 1, '时候': 1, '需要': 1}
}


class MaintenceTopic(Topic):
    """"""

    def __init__(self):
        Topic.__init__(self)
        self._topicid = TopicID.MaintenanceTopic

    def parse(self, query_info):
        super(MaintenceTopic, self).parse(query_info)
        entities = query_info.get_entities()
        for entity in entities:
            if entity.ner == PROJECT:
                return self._parse_project(entity)
        return False

    def _parse_project(self, entity):
        node = graph_search.get_node(entity.ner, KG_NAME, entity.cont_ner)
        if node is None:
            return False
        props = graph_search.get_properties(node)
        query = self._query_info.get_text()
        prop_score = {}
        for prop in props:
            if prop not in project_syno:
                continue
            synos = project_syno[prop]
            for word, weight in synos.items():
                if word in query:
                    if prop in prop_score:
                        prop_score[prop] += weight
                    else:
                        prop_score[prop] = weight
        if len(prop_score) == 0:
            semantic = self.get_semantic()
            semantic.add(KG_TYPE, entity.ner)
            semantic.add(KG_NAME, entity.cont_ner)
            semantic.add(PROPERTY, 'function')
            return True
        else:
            sorted_list = sorted(prop_score.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
            prop = sorted_list[0][0]
            semantic = self.get_semantic()
            semantic.add(KG_TYPE, entity.ner)
            semantic.add(KG_NAME, entity.cont_ner)
            semantic.add(PROPERTY, prop)
            return True
