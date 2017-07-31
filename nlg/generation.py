# _*_ coding: utf-8 _*_

import abc

from base.base import Base
from nlg.response import *


class Generation(Base):
    """
    
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        Base.__init__(self)
        self._topic = None
        self._topicid = None  # 子类必须自定义该成员变量
        self._response = None

    @property
    def topic(self):
        return self._topic

    @property
    def topicid(self):
        return self._topicid

    @property
    def response(self):
        return self._response

    def set_topic(self, topic):
        self._topic = topic

    @abc.abstractmethod
    def generate(self):
        self._response = Response()
        self._response.set_response_code(ResponseCode.OK)
        self._response.set_state_code(StateCode.Normal)
        self._response.set(self._topic)
