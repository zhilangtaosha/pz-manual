# _*_ coding: utf-8 _*_

from nlu.query.parser import entity
from nlu.query.dict import userdict


def init():
    #  加载用户字典
    # userdict.load_kg()
    userdict.load()
    userdict.load_stopwords()
    entity.load()


init()
print 'init finish'
