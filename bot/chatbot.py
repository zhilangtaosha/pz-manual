# _*_ coding: utf-8 _*_

import json

from common.exception import AnswerError
from common.log import log
from common.session import smgr
from conf.const import *
from nlg.generation_mgr import GenerationManager
from nlu.topic_mgr import TopicManager
from user.userinfo import UserInfo


class ChatBot(object):
    """
    
    """

    def __init__(self):
        self._query = ''
        self._userinfo = None
        self._topic_mgr = None
        self._generation_mgr = GenerationManager()
        self._force = 0
        self._session = None

    def set(self, args):
        """
        :param args:
            用户唯一标识：uid
            问答请求：query
            强制新一轮会话：fs，默认为0表示否，1表示是
        :return:
        """
        if UID in args:
            self._session = smgr.get(args[UID])
        else:
            pass  # todo raise exception 缺少用户唯一标识
        if QUERY in args:
            self._init_query(args[QUERY])
        else:
            pass  # todo raise exception 设计错误码维护类
        if FORCE in args or self._session.get(S_NOTUNDERSTAND) == 1:
            self._force = 1
        else:
            self._force = 0
        self._init_userinfo(args[UID])
        self._init_topic_mgr()
        self._init_exception()

        log(json.dumps(args, ensure_ascii=False) + '\n')

    def _init_exception(self):
        self._expt = self._session.get(S_EXCEPT)
        if self._expt is None:
            self._expt = AnswerError()
            self._session.add(S_EXCEPT, self._expt)
        self._expt.ae = 0

    def _init_topic_mgr(self):
        self._topic_mgr = self._session.get(S_TOPIC_MGR)
        if self._topic_mgr is None or self._force == 1:
            self._topic_mgr = TopicManager()
            self._topic_mgr.set_user_info(self._userinfo)
            self._session.add(S_TOPIC_MGR, self._topic_mgr)

    def _init_query(self, qry):
        """
        对query对编码解码可以放到这里统一处理
        :param qry:
        :return:
        """
        self._query = qry.upper()

    def _init_userinfo(self, uid):
        self._userinfo = self._session.get(S_USERINFO)
        if self._userinfo is None:
            self._userinfo = UserInfo(uid)
            self._session.add(S_USERINFO, self._userinfo)

    def get_response(self):
        self._topic_mgr.parse(self._query)
        self._generation_mgr.set_topic(self._topic_mgr.get_topic())
        response = self._generation_mgr.generate()
        if self._expt.ae == 1 and response.is_empty():
            response.set_response_code(ResponseCode.NoneAutoQuestion)
        if response.is_empty():
            self._session.add(S_NOTUNDERSTAND, 1)
        else:
            self._session.add(S_NOTUNDERSTAND, 0)
        result = response.dumps()
        log(result.decode('unicode-escape') + '\n')
        return result

