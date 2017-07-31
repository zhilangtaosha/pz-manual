# _*_ coding: utf-8 _*_

import abc

from base.base import Base
from conf.const import TopicStateID, TopicID
from frame import SemanticFrame


class Topic(Base):
    """

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        Base.__init__(self)
        self._user_info = None
        self._query_info = None
        self._semantic = SemanticFrame()
        self._topicid = TopicID.NullTopic  # 子类必须自定义该成员变量
        self._stateid = TopicStateID.Null  # 状态id，子类自己定义stateid的含义
        self._finished = False
        self._domain = None
        self._intent = None
        self.arguments = {}

    @property
    def domain(self):
        return self._domain

    @property
    def intent(self):
        return self._intent

    def __str__(self):
        return '%s: %s' % (self._domain, self.__class__.__name__)

    def set_stateid(self, stid):
        assert isinstance(stid, TopicStateID)
        self._stateid = stid

    def set_user_info(self, user_info):
        self._user_info = user_info

    def get_user_info(self):
        return self._user_info

    def get_query_info(self):
        return self._query_info

    # def _init_states(self):
    #     model_module = importlib.import_module(self.__module__)
    #     try:
    #         states_cls = getattr(model_module, '_STATES_CLS')
    #         if states_cls is not None:
    #             for state_cls in states_cls:
    #                 self.add_state(state_cls())
    #     except AttributeError:
    #         raise CustomException('init states exception')

    @property
    def userid(self):
        return self._user_info.uid

    # def init_semantic(self):
    #     frame = copy.deepcopy(frame_tools.get_frame(self._topicid))
    #     self._semantic.load(frame)

    @abc.abstractmethod
    def parse(self, query_info):
        """
        返回值是bool类型，表明query_info语义分析是否属于当前topic
        :param query_info:
        :return:
        """
        self._query_info = query_info

    def get_semantic(self):
        return self._semantic

    def begin(self):
        """
        对话开始时，调用该方法
        :return:
        """
        self._finished = False

    def end(self):
        """
        对话结束后，调用该方法
        :return:
        """
        self._finished = True
        self._semantic.clear()

    @property
    def finished(self):
        return self._finished

    @property
    def topicid(self):
        return self._topicid

    @property
    def stateid(self):
        return self._stateid
