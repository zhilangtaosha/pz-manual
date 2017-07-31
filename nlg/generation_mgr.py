# _*_ coding: utf-8 _*_

from common.exception import CustomException
from generation_cls import GENERATIONS_CLS
from response import Response
from conf.const import *


class GenerationManager(object):
    """
    
    """

    def __init__(self):
        self._generations = {}
        self._cur_generation = None
        self._init_generation()

    def _init_generation(self):
        for generation_cls in GENERATIONS_CLS:
            instance = generation_cls()
            self._generations[instance.topicid] = instance

    def set_topic(self, topic):
        if topic.topicid in self._generations:
            self._cur_generation = self._generations[topic.topicid]
            self._cur_generation.set_topic(topic)
        else:
            raise CustomException('genertion of topicid "%s" not exist.' % topic.topicid)

    def _default(self):
        response = Response()
        response.set_response_code(ResponseCode.OK)
        response.set_data({'list': self._load_default()})
        return response

    def _load_default(self):
        data = []
        for line in open(PROJECT_DIR + 'conf/default_answer'):
            data.append(line.strip())
        return data

    def generate(self):
        response = self._cur_generation.generate()
        if response.is_empty():
            return self._default()
        return response

