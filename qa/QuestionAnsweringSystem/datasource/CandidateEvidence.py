# coding=utf-8

import MySQLdb
import xlrd
from conf.const import MYSQL_DB,MYSQL_PASSWD,MYSQL_USER,MYSQL_HOST,MYSQL_PORT,MYSQL_TB
from qa.QuestionAnsweringSystem.common.exception import ReturnStrException
from qa.QuestionAnsweringSystem.const import  PATH_SOURCE, SOURCE_ID
from qa.QuestionAnsweringSystem.filter.parser.ParserWord import wordParser

conn = MySQLdb.connect(host=MYSQL_HOST, user=MYSQL_USER,
                       passwd=MYSQL_PASSWD, port=MYSQL_PORT, charset='utf8')
conn.select_db(MYSQL_DB)

cursor = conn.cursor()


class CandidateEvidence(object):
    def __init__(self, answer=None, que_in=None):
        self.answer = answer
        self.evidence = {}
        self.question = que_in
        # self.read_source()
        self.st = None

    # TODO 数据源修改后，加以调整 ，暂时使用  def read_resource_all(path=PATH_SOURCE, flag=2)  获取数据源
    def read_source(self, flag=2, path=PATH_SOURCE, ):
        """
        分类后获取对应的数据源，从数据源挑选候选证据，进行处理。  挑选依据 包含 问题中的字
        :param path:
        :return:
        """
        wb = xlrd.open_workbook(path)
        self.st = wb.sheet_by_index(4)
        ncols, nrows = self.st.ncols, self.st.nrows
        for row in range(nrows):
            if any(int(self.st.cell(row, 2).value) == int(ans_id) for (ans_id, ans_freq) in self.answer):
                if any(word in self.st.cell(row, 1).value for word in self.question):
                    try:
                        if flag == 1:
                            pass
                    except ValueError as e:
                        print e.message

    def get_evidence(self):
        for k, evidence in self.evidence.items():
            self.evidence[int(k)] = wordParser.a_sub_b(evidence)
        return self.evidence

    @staticmethod
    def read_resource_all(path=PATH_SOURCE, sid=SOURCE_ID, flag_q=2, flag_a=None):
        evidence = dict()
        if sid == 1:
            """读取excel"""
            wb = xlrd.open_workbook(path)
            st = wb.sheet_by_index(4)
            ncols, nrows = st.ncols, st.nrows
            for row in range(nrows):
                str_add = u""
                if flag_q:  # ！=1  取问题的flag遍
                    for i in range(flag_q):
                        str_add += unicode(st.cell(row, 3).value)
                        str_add += ' '
                if flag_a:
                    str_add = u""
                    for i in range(flag_a):
                        str_add += unicode(st.cell(row, 3).value)
                        str_add += ' '
                evidence[int(st.cell(row, 0).value)] = wordParser.parse(str_add)
        elif sid == 2:
            """
               mysql数据源使用

            """
            cursor = conn.cursor()
            cursor.execute('select id,question,answer from {}'.format(MYSQL_TB))
            data = cursor.fetchall()
            evidence = dict()
            for key, v1, v2 in data:
                q_str = ''
                if flag_q:
                    for i in range(flag_q):
                        q_str += v1 + ' '
                if flag_a:
                    for j in range(flag_a):
                        q_str += v2 + ' '
                evidence[int(key)] = wordParser.parse(unicode(q_str))
                # print key,v1,v2
            cursor.close()
            return evidence
        else:
            raise

    @staticmethod
    def id2str(_id, sid=SOURCE_ID,flag=2):
        if sid == 1:
            """excel数据源 使用"""
            wb = xlrd.open_workbook(PATH_SOURCE)
            st = wb.sheet_by_index(4)
            # print id, nrows, ncols
            return st.cell(int(_id), 1).value
        elif sid == 2:
            """mysql数据源使用"""
            cursor = conn.cursor()
            cursor.execute("select %s from %s WHERE id=%s" % ('question' if flag==1 else 'answer',MYSQL_TB,_id))
            ret_str = cursor.fetchone()
            # print str(ret_str).replace('u\'', '\'').decode('unicode_escape')
            return ret_str[0].decode('utf-8')
        else:
            raise ReturnStrException(u"输入数据源参数不对，请仔细检查")


if __name__ == '__main__':
    ce = CandidateEvidence()
    # ce.read_resource_all()
    ce.id2str(6)
