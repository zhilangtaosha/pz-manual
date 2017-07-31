# _*_ coding: utf-8 _*_


from conf.const import *
from data.graph import graph_search
from nlu.topic import Topic
from fuzzywuzzy import fuzz
from utils.util import tounicode

insurance_company_prop_syno = {
    'service_line': {'客服热线': 1, '客服': 1, '电话': .5, '热线': 1, '联系方式': 1},
    'insurance_line': {'投保热线': 1, '投保': 1, '买': 1},
    'query_policy': {'投保报价': 1, '保费': 1, '报价': 1, '网址': 1, '网站': 1, '地址': 1, '系统': 1},
    'query_compensate': {'理赔查询': 1, '理赔': 1},
    'insurance_count': {'保单查询': 1, '保单': 1}
}

insurance_prop_syno = {
    'define': {'险种定义': 1, '定义': 1, '什么': 1},
    'price': {'投保价格': 1, '价格': 1, '投保': 1},
    'repeat': {'金额累加': 1, '累加': 1, '上限': 1, '累计': 1},
    'compensate': {'赔付金额': 1, '赔付': 1},
    'free': {'免赔率': 1, '免赔': 1}
}


class InsuranceTopic(Topic):
    """"""

    def __init__(self):
        Topic.__init__(self)
        self._topicid = TopicID.InsuranceTopic

    def parse(self, query_info):
        super(InsuranceTopic, self).parse(query_info)
        entites = query_info.get_entities()
        if len(entites) == 0:
            pass
        else:
            for entity in entites:
                if entity.ner == ONTOLOGY:
                    return self._parse_ontology(entity)
                elif entity.ner == INSURANCE_COMPANY:
                    return self._parse_company(entity)
                elif entity.ner == INSURANCE:
                    return self._parse_insurance(entity)
                else:
                    return False

    def _parse_ontology(self, entity):
        semantic = self.get_semantic()
        if entity.cont_ner == 'insurance':
            semantic.add(KG_TYPE, INSURANCE)
            semantic.add(KG_NAME, '*')
            return True
        elif entity.cont_ner == 'company':
            semantic.add(KG_TYPE, INSURANCE_COMPANY)
            semantic.add(KG_NAME, '*')
            return True
        else:
            return False

    def _parse_insurance(self, entity):
        node = graph_search.get_node(entity.ner, KG_NAME, entity.cont_ner)
        if node is None:
            return False
        props = graph_search.get_properties(node)
        query = self._query_info.get_text()
        temp = self._query_info.get_template()
        prop_score = {}
        for prop in props:
            if prop not in insurance_prop_syno:
                continue
            synos = insurance_prop_syno[prop]
            for word, weight in synos.items():
                if word in temp:
                    if prop in prop_score:
                        prop_score[prop] += weight
                    else:
                        prop_score[prop] = weight
        if len(prop_score) == 0:
            # print fuzz.ratio(query, entity.cont)

            if entity.ner == INSURANCE:
                if fuzz.ratio(query, entity.cont) > 80:
                    semantic = self.get_semantic()
                    semantic.domain = DOMAIN_INSURANCE
                    semantic.intent = INTENT_QUERY
                    semantic.add(KG_TYPE, entity.ner)
                    semantic.add(KG_NAME, entity.cont_ner)
                    semantic.add(PROPERTY, 'define')
                    return True
                return False
            else:
                return False
        else:
            sorted_list = sorted(prop_score.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
            prop = sorted_list[0][0]
            semantic = self.get_semantic()
            semantic.domain = DOMAIN_INSURANCE
            semantic.intent = INTENT_QUERY
            semantic.add(KG_TYPE, entity.ner)
            semantic.add(KG_NAME, entity.cont_ner)
            semantic.add(PROPERTY, prop)
            return True

    def _parse_company(self, entity):
        cont = tounicode(entity.cont_ner)
        node = graph_search.get_node(entity.ner, KG_NAME, cont)
        if node is None:
            return False
        props = graph_search.get_properties(node)
        query = self._query_info.get_text()
        prop_score = {}
        for prop in props:
            if prop not in insurance_company_prop_syno:
                continue
            synos = insurance_company_prop_syno[prop]
            for word, weight in synos.items():
                if word in query:
                    if prop in prop_score:
                        prop_score[prop] += weight
                    else:
                        prop_score[prop] = weight
        if len(prop_score) == 0:
            return False
        sorted_list = sorted(prop_score.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
        prop = sorted_list[0][0]
        semantic = self.get_semantic()
        semantic.domain = DOMAIN_INSURANCE_COMPANY
        semantic.intent = INTENT_QUERY
        semantic.add(KG_TYPE, entity.ner)
        semantic.add(KG_NAME, cont)
        semantic.add(PROPERTY, prop)
        return True
