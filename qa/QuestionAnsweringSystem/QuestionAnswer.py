# coding=utf-8

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from datasource.CandidateEvidence import CandidateEvidence
from filter.ScoreMgr import ScoreManager
from filter.parser.ParserWord import wordParser
from const import ThresholdValue

evi_dict = CandidateEvidence.read_resource_all()


class QA(object):
    def __init__(self):
        pass

    def input_question(self, que_in):
        que_in = wordParser.parse(que_in)
        sm = ScoreManager(que_in, evi_dict)
        score_evi = sm.score_topn(3)
        answer = CandidateEvidence.id2str(score_evi[0][0])
        answer_notgood = u'没有合适的答案'
        thv = score_evi[0][1]  #(id,freq)
        return (
            score_evi[0][0] if thv >= 6 else 0, answer if thv >= ThresholdValue else  answer_notgood, score_evi[0][1])


qa = QA()

if __name__ == '__main__':
    flag = 2  # 1/2 切换输出
    if flag == 1:  # 传入测试列表，测试总体正确率
        import matplotlib.pyplot as plt
        import matplotlib

        matplotlib.use('AGG')
        x = list()
        y = list()

        qa = QA()
        # qa.input_question(u'饮酒后驾驶机动车')
        qa.input_question(u'使用伪造、变造的机动车号牌、行驶证、驾驶证的')
        # qa.input_question(u'不系安全带怎么处罚')
        import xlrd

        wb = xlrd.open_workbook('./datasource/source/traffic_rule.xlsx')
        st = wb.sheet_by_index(4)
        count = 0
        score_0 = 0
        with open('result.txt', 'w') as f:
            cou = 0
            for row in range(st.nrows):
                cou += 1
                id, _, score = qa.input_question(st.cell(row, 3).value)
                if id == row + 1:
                    # print 'count', count
                    if score <= 30:
                        x.append(count)
                        y.append(score)
                    count += 1
                    f.write('count   ' + str(count) + '  score ' + str(score) + '\n')
                elif score == 0:
                    score_0 += 1
                else:
                    f.write(str(id) + '   ' + 'question: ' + str(row) + '  answer  ' + str(id) + '\n')
                # print row
                f.write('row  ' + str(row) + '\n')
        print 'count  ', count
        print 'score_0 ', score_0
        plt.plot(x, y)
        plt.savefig("easyplot.jpg")
    if flag == 2:  # 循环从控制台读取问题，输出答案
        # qa = QA()
        while 1:
            in_q = raw_input(u'输入问题，利索点')
            id, answer, score = qa.input_question(in_q)
            print '问题所在行号： ', id
            # print str(answer).replace('u\'', '\'').decode('unicode_escape')
            print answer
            print '此问题分数  ：', score
