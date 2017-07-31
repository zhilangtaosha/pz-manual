# coding=utf-8

import sys
from collections import defaultdict

import xlrd

from qa.QuestionAnsweringSystem.common.exception import ReturnStrException
from qa.QuestionAnsweringSystem.const import SYNONYM_PATH

reload(sys)
sys.setdefaultencoding('utf-8')


class SynonymReplace(object):
    def __init__(self):
        pass

    @staticmethod
    def read_synonym_source(syn_path=SYNONYM_PATH):
        """
        读取同义词excel，返回包含同义词词典
        :return:
        """
        syn_dict = defaultdict(list)
        fileflag = syn_path.split('.')[-1]
        if 'xlsx' == fileflag:
            wb = xlrd.open_workbook(syn_path)
            st = wb.sheet_by_index(0)
            nrows = st.nrows
            ncols = st.ncols
            for i in range(nrows):
                if st.cell_value(i, 0):
                    syn_dict.update({unicode(st.cell_value(i, 0)): []})
                for j in range(ncols):
                    if st.cell_value(i, j):
                        syn_dict[st.cell_value(i, 0)].append(unicode(st.cell_value(i, j)))
        elif 'txt' == fileflag:
            def getlist(str_in):
                return str_in.split()

            with open(syn_path, 'r') as f:
                for line in f.readlines():
                    tmp_dict = dict()
                    # print line.split()
                    tmp_dict[line.split()[0]] = getlist(line)
                    syn_dict.update(tmp_dict)
        else:
            raise ReturnStrException(u'没有传入正确同义词源')
        return syn_dict

    def sent_replace(self, sent_in):
        syn_dict = self.read_synonym_source()
        sent_out = sent_in
        for key, i in syn_dict.items():
            if isinstance(key, str):
                key = key.decode('utf-8')
            for j in i:
                if isinstance(j, str):
                    j = j.decode('utf-8')
                if j in sent_in:
                    sent_out = sent_out.replace(j, key)
        return sent_out


syr = SynonymReplace()

if __name__ == '__main__':
    s1 = SynonymReplace()
    ret1 = s1.read_synonym_source()
    # print ret1
    # for kk in ret1.items():
    #     print (str(kk).replace('u\'', '\'').decode('unicode_escape'))
    ret = s1.sent_replace(u'漫水桥漫水桥漫水桥', )
    print ret
    # print dict(1,2)
