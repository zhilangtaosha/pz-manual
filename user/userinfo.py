# _*_ coding: utf-8 _*_

from common.exception import CustomException


class UserInfo(object):
    """

    """

    def __init__(self, uid):
        if uid.strip() == '':
            raise CustomException('user id is empty')
        self._user_id = uid

    @property
    def id(self):
        return self._user_id
