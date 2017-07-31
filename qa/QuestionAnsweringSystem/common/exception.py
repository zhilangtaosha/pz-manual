# _*_ coding: utf-8 _*_


class CustomException(Exception):
    pass


class SessionException(Exception):
    pass


class ReturnStrException(Exception):
    def __init__(self, str_in):
        self.str_in = str_in

    def __str__(self):
        return self.str_in
