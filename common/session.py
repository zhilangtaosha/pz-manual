# _*_ coding: utf-8 _*_

import time
import uuid

from common.exception import SessionException


class Session(object):
    """

    """

    def __init__(self):
        self.valid_time = 60 * 5  # session默认的有时间（分钟）
        self._create_time = time.time()
        self._last_time = time.time()
        self._id = uuid.uuid1()
        self._userid = ''
        self._holder = {}

    def is_over_time(self):
        return time.time() - self.last_time > self.valid_time

    def _update_last_time(self):
        self._last_time = time.time()

    def set_userid(self, uid):
        self._userid = uid

    @property
    def userid(self):
        return self._userid

    @property
    def create_time(self):
        return self._create_time

    @property
    def last_time(self):
        return self._last_time

    @property
    def id(self):
        return self._id

    def _has_key(self, k):
        return k in self._holder

    def update(self, k, v):
        self._update_last_time()  # todo: 以后优化为装饰器
        if self._has_key(k):
            self._holder[k] = v
        else:
            raise SessionException('no key:%s in session' % str(k))

    def add(self, k, v, replace=True):
        self._update_last_time()
        if replace:
            self._holder[k] = v
        elif not self._has_key(k):
            self._holder[k] = v

    def delete(self, k):
        self._update_last_time()
        if self._has_key(k):
            del (self._holder[k])

    def get(self, k):
        # type: (object) -> object
        self._update_last_time()
        if self._has_key(k):
            return self._holder[k]
        else:
            return None


class SessionManager(object):
    """

    """

    def __init__(self):
        self._session_holder = {}

    def _has_session(self, k):
        return k in self._session_holder

    def get(self, k):
        # type: (object) -> object
        if k is None:
            raise SessionException('argument "k" of session method get(k) is None')
        if self._has_session(k):
            session = self._session_holder[k]
            if session.is_over_time():
                self.delete(k)
                session = Session()
                session.set_userid(k)
                self._add(k, session)
            return session
        else:
            session = Session()
            session.set_userid(k)
            self._add(k, session)
            return session

    def delete(self, k):
        if self._has_session(k):
            del (self._session_holder[k])

    def _add(self, k, s):
        self._session_holder[k] = s


smgr = SessionManager()

