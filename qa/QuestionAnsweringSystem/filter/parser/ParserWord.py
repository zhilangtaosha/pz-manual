# -*- coding: utf-8 -*-
import sys

import jieba

from qa.QuestionAnsweringSystem.const import JIEBA_LOADPATH
from qa.QuestionAnsweringSystem.const import PATH_STOPWORDS
from qa.QuestionAnsweringSystem.filter.parser.synonym_replace.pre_replace_synonym import syr

reload(sys)
sys.setdefaultencoding('utf-8')

jieba.load_userdict(JIEBA_LOADPATH)

"""
分词，返回分词后列表，
处理停用词，英文单词，数字
jieba  自定义词典

"""


class WordParser(object):
    def __init__(self):
        self.stop = [line.strip().decode('utf-8') for line in open(PATH_STOPWORDS).readlines()]
        # self.stop = [line.strip() for line in open(PATH_STOPWORDS).readlines()]

    def a_sub_b(self, text_list):
        ret = []
        # text_list=jieba.lcut(text_list)
        for el in text_list:
            if el in self.stop:
                pass
            elif el in [' ', u' ']:
                pass
            else:
                ret.append(el)
        return ret

    def parse(self, text):
        if not text:
            return []
        if isinstance(text, str):
            text = text.decode('utf-8')
        # 同义词替换
        text = syr.sent_replace(text)
        text_parser = jieba.lcut(text)
        ret_list = self.a_sub_b(text_parser)
        # print str(ret_list).replace('u\'','\'').decode('unicode_escape')
        return ret_list


wordParser = WordParser()

if __name__ == '__main__':
    ret1 = wordParser.parse('电脑大幅度漫水桥？')
    print str(ret1).replace('u\'', '\'').decode('unicode_escape')

    a = '电脑大幅度漫水桥'
    print type(a)
    print type(unicode(a))
    print a
