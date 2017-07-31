# _*_ coding: utf-8 _*_


from common.session import smgr
from conf.const import *
from nlu.query.parser import *
from topic_cls import TOPICS_CLS


class TopicManager(object):
    """

    """

    def __init__(self):
        self._user_info = None
        self._topics = {}
        self._current_topic = None
        self._pre_topic = None
        self._init_topics()

    def set_user_info(self, user_info):
        self._user_info = user_info

    def _init_topics(self):
        for topic_cls in TOPICS_CLS:
            topic = topic_cls()
            topic.set_user_info(self._user_info)
            self.add_topic(topic)

    def add_topic(self, topic):
        if topic.topicid not in self._topics:
            self._topics[topic.topicid] = topic

    def clear_all(self):
        for topicid, topic in self._topics.items():
            topic.get_semantic().clear()

    def _start_new_topic(self, query_info):
        self._current_topic = self.classify_topic(query_info)
        if not self._current_topic.parse(query_info):
            self._current_topic = self._topics[TopicID.QAService]
            self._current_topic.parse(query_info)
        self._pre_topic = self._current_topic
        self._current_topic.begin()
        # self._current_topic.get_semantic().clear()

    def parse(self, query):
        query_info = QueryParser()
        query_info.parse(query)

        # sentid, std_query = syno.get(query)
        if self._pre_topic is not None and not self._pre_topic.finished:
            if self._pre_topic.parse(query_info):
                self._current_topic = self._pre_topic
            else:
                self._start_new_topic(query_info)
        else:
            self._start_new_topic(query_info)

    def classify_topic(self, query_info):
        template = query_info.get_template()
        # if '<PHEN>' in template:
        #     topic_id = TopicID.BrokenDownTopic
        if '<PART>' in template or '<FUNCTION>' in template:
            topic_id = TopicID.ManualTopic
        elif '<COMPANY>' in template:
            topic_id = TopicID.InsuranceTopic
        elif '<INSURANCE>' in template:
            topic_id = TopicID.InsuranceTopic
        elif '<PROJECT>'in template:
            topic_id = TopicID.MaintenanceTopic
        else:
            s = smgr.get(self._user_info.id)
            expt = s.get(S_EXCEPT)
            expt.ae = 1
            topic_id = TopicID.QAService
        # topic_id = TopicID.ManualTopic  # classify(query_info)  # todo
        # topic_id = TopicID.QAService  # classify(query_info)  # todo
        return self._topics[topic_id]

    def get_topic(self):
        return self._current_topic
