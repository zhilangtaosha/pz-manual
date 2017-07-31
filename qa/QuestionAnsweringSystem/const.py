# coding=utf-8
import os

from enum import Enum

path_sep = os.path.sep


def get_dir(abs_path):
    return os.path.dirname(os.path.abspath(abs_path))


def cwd(abs_path):
    return get_dir(abs_path) + path_sep


_cwd = cwd(__file__)

# Grocery分类器名称
GR_TR = _cwd + 'classification' + path_sep + 'model' + path_sep + 'gr_traffic_rule'
# 停用词所在文件
PATH_STOPWORDS = _cwd + 'datasource' + path_sep + 'category_file' + path_sep + 'stopwords.txt'
# 测试正确率数据源所在文件，格式如sheet4
PATH_SOURCE = _cwd + 'datasource' + path_sep + 'source' + path_sep + 'traffic_rule.xlsx'
JIEBA_LOADPATH = _cwd + 'datasource' + path_sep + 'category_file' + path_sep + 'user_dict.txt'


# 同义词存放路径
class SynonymPath(Enum):
    ExcelPath = _cwd + 'datasource' + path_sep + 'source' + path_sep + 'synonym' + path_sep + 'synonym01.xlsx'
    TxtPath = _cwd + 'datasource' + path_sep + 'source' + path_sep + 'synonym' + path_sep + 'synonym.txt'


SYNONYM_PATH = SynonymPath.TxtPath.value


# # mysqlip
# class MySqlConfig(Enum):
#     MYSQL_IP = '192.168.20.81'
#     MYSQL_USER = 'root'
#     MYSQL_PASSWD = 'admin'
#     MYSQL_DB = 'pz_gac_a'
#     MYSQL_TB='zyl_test'

ThresholdValue = 8


class SOURCEID(Enum):
    ExcelId = 1
    MySqlId = 2


SOURCE_ID = SOURCEID.MySqlId.value


class ModelID(Enum):
    """
        分类器ID
    """
    NullTopic = 0
    GroceryID = 1


class Weights(Enum):
    """
    QA核心算法权重
    """
    WordFreq = 2
    Biagram = 4
    SkipBiagram = 4


class QuestionType(Enum):
    """
    问题类型
    """
    NULL = 0
    TrafficRuleType = 1


if __name__ == '__main__':
    print GR_TR
    print ModelID.GroceryID.value
