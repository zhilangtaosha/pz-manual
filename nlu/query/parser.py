# _*_ coding: utf-8 _*_
import json
import urllib

from base.base import Base
from conf.conf import max_seg_len
from conf.const import *
from nlu.query.dict import userdict, entity
from utils.util import tounicode


class Word(Base):
    """

    """

    def __init__(self, cont='', pos='', ner='', relate='', parent='', cont_ner=''):
        Base.__init__(self)
        self.cont = cont
        self.cont_ner = cont_ner
        self.pos = pos
        self.ner = ner
        self.relate = relate
        self.parent = parent


class Sentence(Base):
    """

    """

    def __init__(self):
        Base.__init__(self)
        self._words = []

    def add(self, word):
        self._words.append(word)

    def clear(self):
        self._words = []

    def words(self):
        return self._words


class QueryParser(Base):
    """
    对用户对query进行nlp分析，得到实体、谓词等
    """

    def __init__(self):
        Base.__init__(self)
        self._query = ''
        self._template = ''
        self._sent = Sentence()
        self._entities = []
        self._user_seg = CustomSegment()

    def _seg_ner(self, query):
        text, text_tag, tag_sys = self._user_seg.seg(query)
        for tag, word_info in tag_sys.items():
            std_name = entity.get_std(word_info[NER], word_info[CONT])
            if std_name == '':
                std_name = word_info[CONT]
            self._entities.append(
                Word(cont=word_info[CONT], pos=word_info[POS], cont_ner=std_name, ner=word_info[NER]))
            # ltp_words = get_ltp(text_tag)
            # for word in ltp_words:
            #     w = Word(word[CONT], word[POS], word[NER], word[RELATE], word[PARENT])
            #     if word[CONT] in tag_sys:
            #         w.cont = tag_sys[word[CONT]][CONT]
            #         w.ner = tag_sys[word[CONT]][NER]
            #         w.pos = tag_sys[word[CONT]][POS]
            #     self._sent.add(w)

    def get_sentence(self):
        return self._sent

    def get_template(self):
        return self._template

    def get_text(self):
        return self._query

    def get_entities(self):
        return self._entities

    def parse(self, query):
        query = tounicode(userdict.remove_stopwords(query))
        self._query = query.strip()
        if query.strip() == u'':
            return
        self._seg_ner(query)
        self._gen_template()

    def _gen_template(self):
        query = self._query
        for w in self._entities:
            if w.ner in custom_ner:
                query = query.replace(w.cont, '<' + w.ner + '>')
        self._template = query


def get_ltp(query):
    if isinstance(query, unicode):
        query = query.encode('utf-8')
    ltp = urllib.urlopen(LTP_GET + query).read()
    return json.loads(ltp)[0][0]


# def post_ltp(query):
#     data = {'s': query, 'x': 'n', 't': 'all', 'f': 'json'}
#     request = urllib2.Request(LTP_POST)
#     params = urllib.urlencode(data)
#     response = urllib2.urlopen(request, params)
#     content = response.read().strip()
#     return json.loads(content)[0][0]


class CustomSegment(Base):
    """"""

    def __init__(self):
        super(CustomSegment, self).__init__()
        self._dict = userdict

    def seg(self, text):
        """
        :param text: unicode
        :return:
        """
        text = tounicode(text)
        text_tag = text
        end = len(text)
        i = 0
        tag_idx = 97
        tag_sys = {}
        while end >= 0:
            beg = end - max_seg_len
            if beg < 0:
                beg = 0
            beg += i
            sub_text = text[beg: end]
            if self._dict.has(sub_text):
                tag = 'tag' + chr(tag_idx)
                text = text.replace(sub_text, ' %s ' % sub_text)
                text_tag = text_tag.replace(sub_text, ' %s ' % tag)
                info = self._dict.get(sub_text)
                tag_sys[tag] = {POS: info[POS], NER: info[NER], CONT: sub_text}
                end = beg
                i = 0
                tag_idx += 1
            elif beg == end:
                end -= 1
                i = 0
            else:
                i += 1
        return text, text_tag, tag_sys
