# _*_ coding: utf-8 _*_


class CustomException(Exception):
    pass  # todo 自定义输出格式


class SessionException(Exception):
    pass


class ExceptionHolder(object):
    """"""

    def __init__(self):
        self._exceptions = {}

    def get(self, ex_id):
        if ex_id in self._exceptions:
            return self._exceptions[ex_id]
        else:
            return ""

    def set(self, ex_id, ex_val):
        pass

    def init(self, uid):
        self._exceptions[uid] = {}


exceptions = ExceptionHolder()


class AnswerError(object):
    """"""

    def __init__(self):
        self.ae = 0
