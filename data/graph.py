# _*_ coding: utf-8 _*_

from py2neo import Graph, NodeSelector

from conf.const import *

_graph = Graph(BOLT, username=NEO_USER, password=NEO_PASSWD)


class GraphSearch(object):
    """"""

    def __init__(self):
        self._selector = NodeSelector(_graph)

    @property
    def selector(self):
        return self._selector

    def get_node(self, label, property_key, property_value):
        node = _graph.find_one(label, property_key, property_value)
        return node

    def get_nodes(self, label, property_key=None, property_value=None):
        nodes = _graph.find(label, property_key, property_value)
        return nodes

    def get_properties(self, node):
        return node.properties

    def get_relations(self, start_node, end_node=None):
        rels = _graph.match(start_node=start_node, end_node=end_node)
        return rels

    def get_relations_by_entity(self, start_node, end_node=None, label=None):
        s = self.get_node(start_node.ner, KG_NAME, start_node.cont_ner)
        e = self.get_node(end_node.ner, KG_NAME, end_node.cont_ner)
        rels = _graph.match(start_node=s, rel_type=label, end_node=e)
        return rels

    def find(self, label, property_key=None, property_value=None, limit=None):
        """ 通过属性值来查找节点和关系
        find_code_1 = test_graph.find_one(label="Person",
        property_key="name",
        property_value="test_node_1"
        )
        print find_code_1['name']
        :param
        """
        if limit == 1:
            return _graph.find_one(label, property_key=property_key, property_value=property_value)
        else:
            return _graph.find(label, property_key=property_key, property_value=property_value, limit=limit)

    def match(self, start_node=None, rel_type=None, end_node=None, bidirectional=False, limit=None):
        """ 通过节点/关系查找相关联的节点/关系
        find_relationship = test_graph.match_one(start_node=find_code_1,end_node=find_code_3,bidirectional=False)
        print find_relationship
        :param
        """
        if limit == 1:
            return _graph.match_one(start_node=start_node, rel_type=rel_type, end_node=end_node,
                                    bidirectional=bidirectional)
        else:
            return _graph.match(start_node=start_node, rel_type=rel_type, end_node=end_node,
                                bidirectional=bidirectional, limit=limit)

    def data(self, statement, parameters=None, **kw):
        # "MATCH (a:Person) RETURN a.name, a.born LIMIT 4"
        # [{'a.born': 1964, 'a.name': 'Keanu Reeves'},
        # {'a.born': 1967, 'a.name': 'Carrie-Anne Moss'},
        # {'a.born': 1961, 'a.name': 'Laurence Fishburne'},
        # {'a.born': 1960, 'a.name': 'Hugo Weaving'}]
        return _graph.data(statement, parameters=parameters, **kw)


graph_search = GraphSearch()

#
# class Entity(object):
#     """提取实体"""
#
#     def extract_entity(self, query, topic_content):
#         result = _graph.data("match (e:%s) return e.name" % topic_content)
#         entity_list = []
#         for item in result:
#             entity_list.append(item["e.name"])
#         for entity in set(entity_list):
#             if entity in query:
#                 yield entity
#
#     def generate_template(self, query, topic_content):
#         for item in self.extract_entity(query, topic_content):
#             if item:
#                 template = query.replace(item, "<%s>" % topic_content)
#                 return template
#
#     def find_predicate(self, query, topic_content):
#         result = []
#         for item in self.extract_entity(query, topic_content):
#             if item:
#                 result = _graph.data("match (e:%s{name:'%s'})-[r]->()  return r.name" % (topic_content, item))
#             else:
#                 for word in ["油箱", "油表", "行车电脑"]:
#                     res = _graph.data("match (e:%s{name:'%s'})-[r]->()  return r.name" % (topic_content, word))
#                     result.append(res[0])
#         predicate_list = []
#         for predicate in result:
#             predicate_list.append(predicate["r.name"])
#         return set(predicate_list)
#
#     def find_phen(self, query, topic_content):
#         for item in self.extract_entity(query, topic_content):
#             result = _graph.data("match (e:%s{name:'%s'})-[r]->(p)  return p.name" % (topic_content, item))
#         predicate_list = []
#         for predicate in result:
#             predicate_list.append(predicate["p.name"])
#         return set(predicate_list)
