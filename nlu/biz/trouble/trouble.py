# _*_ coding: utf-8 _*_
from conf.const import *
from nlu.topic import Topic
from data.graph import graph_search
from extract_stint_word import *


class BrokenDownTopic(Topic):
    """"""

    def __init__(self):
        Topic.__init__(self)
        self._topicid = TopicID.BrokenDownTopic
        self._part = []
        self._phen = []

    def parse(self, query_info):
        super(BrokenDownTopic, self).parse(query_info)
        entities = query_info.get_entities()
        if len(entities) == 0:
            return False
        else:
            self.clear()
            for entity in entities:
                if entity.ner == AUTO_PART:
                    self._part.append(entity.cont_ner)
                if entity.ner == AUTO_PHEN:
                    self._phen.append(entity.cont_ner)
        self._add_entity()
        self._extract_stint_word(query_info)
        return True

    def clear(self):
        self._part = []
        self._phen = []
    def _extract_stint_word(self, query_info):
        """
        提取 部件的位置,操作,运行状态,路况...等限定条件
        stints = {OPE: "", POSITION: "", ROAD: "", WEATHER: "", RUNNING: "", GEAR: "", SPEED: "", GAV: "", START: ""}
        :param query_info: 用于提取query
        :return: 限定条件
        """
        stints = {}
        semantic = self.get_semantic()
        query = query_info.get_text()
        if position_from(query):
            if isinstance(position_from(query), list):
                stints[POSITION] = position_from(query)[0]
            else:
                stints[POSITION] = position_from(query)
        if start_from(query):
            if isinstance(start_from(query), list):
                stints[START] = start_from(query)[0]
            else:
                stints[START] = start_from(query)
        if speed_from(query):
            if isinstance(speed_from(query), list):
                stints[SPEED] = speed_from(query)[0]
            else:
                stints[SPEED] = speed_from(query)
        if running_from(query):
            if isinstance(running_from(query), list):
                stints[RUNNING] = running_from(query)[0]
            else:
                stints[RUNNING] = running_from(query)
        if road_from(query):
            if isinstance(road_from(query), list):
                stints[ROAD] = road_from(query)[0]
            else:
                stints[ROAD] = road_from(query)
        if kind_from(query):
            if isinstance(kind_from(query), list):
                stints[KIND] = kind_from(query)[0]
            else:
                stints[KIND] = kind_from(query)
        if opt_from(query):
            if isinstance(opt_from(query), list):
                stints[OPE] = opt_from(query)[0]
            else:
                stints[OPE] = opt_from(query)
        semantic.add(STINTS, stints)

    @property
    def _get_part(self):
        return list(set(self._part))

    @property
    def _get_phen(self):
        return list(set(self._phen))

    def _add_entity(self):
        semantic = self.get_semantic()
        semantic.clear()
        semantic.add(AUTO_PART, self._get_part)
        semantic.add(AUTO_PHEN, self._get_phen)

