# _*_ coding: utf-8 _*_

from conf.conf import debug


class Base(object):
    """所有类都应该继承该基类"""

    def __init__(self):
        self.debug = debug

    def log(self, text):
        pass
