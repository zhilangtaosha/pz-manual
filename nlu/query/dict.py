# _*_ coding: utf-8 _*_

from base.base import Base
from conf.const import PROJECT_DIR, KG_NAME, KG_TYPE, POS, NER, SEP
from data.graph import graph_search

_END = 'end'

nodes = graph_search.selector.select()


class UserDict(Base):
    """用户自定义分词词典。使用时候注意，文本一定要变成Unicode码"""

    def __init__(self):
        super(UserDict, self).__init__()
        self._stopwords = []
        self._trie = {}
        if self.debug:
            self.load_stopwords()
            # self.load_kg()
            self.load()

    def load_stopwords(self, dict_file=''):
        if dict_file != '':
            user_dict = dict_file
        else:
            user_dict = PROJECT_DIR + 'conf/stop_words'
        for word in open(user_dict):
            word = word.strip()
            if word == '':
                continue
            if word not in self._stopwords:
                self._stopwords.append(word)

    def is_stopword(self, word):
        return word in self._stopwords

    def remove_stopwords(self, text):
        for word in self._stopwords:
            text = text.replace(word, '')
        return text

    def add(self, lex, pos=u'n', ner=u''):
        tr = self._trie
        for w in lex:
            if w not in tr:
                tr[w] = {}
            tr = tr[w]
        tr[_END] = True
        tr[POS] = pos if pos != '' else u'n'
        tr[NER] = ner
        return tr

    @property
    def data(self):
        return self._trie

    def has(self, text):
        if text.strip() == '':
            return False
        tr = self.get(text)
        if tr is not None:
            if _END in tr:
                return True
        return False

    def get(self, lex):
        if lex.strip() == '':
            return None
        tr = self._trie
        for w in lex:
            if w not in tr:
                return None
            else:
                tr = tr[w]
        return tr

    def load(self, dict_file=''):
        if dict_file != '':
            user_dict = dict_file
        else:
            user_dict = PROJECT_DIR + 'conf/user_dict'
        for line in open(user_dict):
            line = line.strip()
            if line.startswith('#') or line == '':
                continue
            ws = line.decode('utf-8').replace(' ', '').split(',')
            if len(ws) == 3:
                self.add(ws[0], ws[1], ws[2])
            elif len(ws) == 2:
                self.add(ws[0], ws[1])
            else:
                self.add(ws[0])

    def load_kg(self):
        node_names = []
        for node in nodes:
            node_names.append({node[KG_NAME]: node[KG_TYPE]})
        node_names.sort(key=lambda x: len(x.keys()[0]), reverse=True)
        for node_name in node_names:
            ner = node_name.values()[0]
            cont = node_name.keys()[0]
            self.add(cont, ner=ner)


class EntitySyno(Base):
    """
    读取实体名同义词配置文件，根据实体的label、name获取同义的实体名字
    配置文件：conf/entity_sysno_name
    # type,node_name,syno1, syno2...
    # 例如：
    # part,发动机,引擎,马达
    """

    def __init__(self):
        Base.__init__(self)
        self._syno = {}
        if self.debug:
            self.load()

    def load(self):
        type_ = 0
        name = 1
        f = PROJECT_DIR + 'conf' + SEP + 'entity_syno_name'
        for line in open(f):
            line = line.strip()
            if line.startswith('#') or line == '':
                continue
            words = line.replace(' ', '').split(',')

            if words[type_] not in self._syno:
                self._syno[words[type_]] = {}
            node_name = self._syno[words[type_]]
            if words[name] not in node_name:
                node_name[words[name]] = []
            sort_word = words[1:]
            sort_word.sort(key=lambda x: len(x), reverse=True)
            node_name[words[name]].extend(sort_word)
            # for w in sort_word:
            #     node_name[words[name]].append(w)

    def get_syno(self, label, name):
        if label in self._syno:
            syno = self._syno[label]
        else:
            return [name]
        if name in syno:
            return self._syno[label][name]
        else:
            return [name]

    def get_std(self, label, name):
        if label in self._syno:
            syno = self._syno[label]
            for std, s in syno.items():
                if name in s:
                    return std
        return ''


entity = EntitySyno()
userdict = UserDict()
