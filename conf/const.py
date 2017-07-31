# _*_ coding: utf-8 _*_

from enum import Enum

from project_property import project_dir, path_sep


class TopicID(Enum):
    NullTopic = 0
    QAService = 1  # QA问答
    ControlTopic = 2  # 语音控制
    ManualTopic = 3  # 手册业务
    BrokenDownTopic = 4  # 车辆故障业务
    InsuranceTopic = 5  # 车辆保险
    MaintenanceTopic = 6  # 保养
    TrafficLawTopic = 7  # 交通法规


class TopicStateID(Enum):
    Null = 0
    SelectQaOption = 1
    SelectManualOption = 2


# 返回码，是否出现异常信息
class ResponseCode(Enum):
    OK = 0
    ArgumentError = 1
    SemanticError = 2
    ServerError = 3
    NoneAutoQuestion = 4


# 多轮交互状态码
class StateCode(Enum):
    Normal = 0  # 普通对话
    Interactive = 1  # 多轮交互对话


# 答案标识位
class AnswerState(Enum):
    NoAnswer = 0  # 没有答案
    Normal = 1  # 有答案


RESPONSE_CODE_ERROR = {
    ResponseCode.OK: '',
    ResponseCode.ArgumentError: 'argument error',  # Get参数错误
    ResponseCode.SemanticError: 'semantic error',  # 语义解析错误
    ResponseCode.ServerError: 'server error',  # 服务器内部错误
    ResponseCode.NoneAutoQuestion: 'non auto'  # 不是汽车相关问题
}


class ModelID(Enum):
    Null = 0


# Response
RP_RC = 'rc'
RP_SC = 'sc'
RP_ERROR = 'error'
RP_TEXT = 'text'
RP_TOPIC = 'topic'
RP_INTENT = 'intent'
RP_SEMANTIC = 'semantic'
RP_SLOTS = 'slots'
RP_DATA = 'data'
RP_ANSWER = 'answer'
RP_ANSWER_STATE = 'state'
RP_TIPS = 'tips'
RP_APPENDIX = 'appendix'
RP_RESULT = 'result'

# 自定义常量
ID = 'id'
IMAGE = 'image'
PROPERTY = 'property'
DOMAIN_INSURANCE = 'insurance'
DOMAIN_INSURANCE_COMPANY = 'insurance_company'
DOMAIN_MAINTENANCE = 'maintenance'
DOMAIN_MANUAL = 'manual'
DOMAIN_BROKENDOWN = 'brokendown'
DOAMIN_QA = 'qa'
INTENT_QUERY = 'query'

# 项目根目录
PROJECT_DIR = project_dir + path_sep
SEP = path_sep

# 常量字符串
DOMAIN = 'domain'
INTENT = 'intent'
SLOTS = 'slots'
WEIGHT = 'weight'
TOPICID = 'topicid'
HYPON = 'hyponymy'
PART = 'part'
FIELD = 'field'
TITLE = 'title'
LIST = 'list'
UPLIST = 'uplist'
INTERACTIVE = 'interactive'
DESCRIPTION = 'description'
DESC = 'desc'

# 图谱节点的属性
KG_TYPE = 'type'
KG_NAME = 'name'
KG_DISPALYNAME = 'displayname'

# Get请求参数
UID = 'uid'
QUERY = 'query'
FORCE = 'fs'

# Session的Key
S_TOPIC_MGR = 's_topic_mgr'
S_EXCEPT = 's_except'
S_NOTUNDERSTAND = 's_notunderstand'
S_RELATION_MGR = 's_relation_mgr'
S_USERINFO = 's_userinfo'

# MySQL配置参数
MYSQL_HOST = '47.92.130.0'
MYSQL_PORT = 3306
MYSQL_USER = 'pz_a'
MYSQL_PASSWD = 'pz_a'
MYSQL_DB = 'gs8_pz_a'
MYSQL_TB = 'gs8_qa'
# sqlalchemy配置
sqlalchemy_engine = 'mysql://pz_a:pz_a@47.92.130.0:3306/gs8_pz_a?charset=utf8'
sqlalchemy_kwargs = {
    'pool_size': 50,
    'pool_timeout': 3,
    'pool_recycle': 7200,
    'echo': False,
    'encoding': 'utf8',
}
# Neo4j配置参数
BOLT = 'bolt://112.126.81.218:7688/db/data/'
NEO_USER = 'neo4j'
NEO_PASSWD = '123456'

# LTP服务器配置
LTP_GET = 'http://47.93.80.118:5000/?query='
LTP_POST = 'http://47.93.80.118:12345/ltp'

# LTP相关标注
POS = 'pos'
CONT = 'cont'
CONT_NER = 'cont_ner'
NER = 'ne'
PARENT = 'parent'
RELATE = 'relate'
# 自定义故障限定词
STINTS = 'stints'
OPE = 'ope'
POSITION = 'position'
ROAD = 'road'
WEATHER = 'weather'
RUNNING = 'running'
GEAR = 'gear'
SPEED = 'speed'
GAV = 'gav'
START = 'start'
KIND = 'kind'
REASON = 'reason'
METHOD = 'method'
ATTENTION = 'attention'
# 自定义实体标注
AUTO_PART = 'PART'
AUTO_FUNC = 'FUNCTION'
AUTO_PHEN = 'PHEN'
AUTO_METHOD = 'METHOD'
INSURANCE_COMPANY = 'COMPANY'
INSURANCE = 'INSURANCE'
ONTOLOGY = 'ONTOLOGY'
PROJECT = 'PROJECT'
custom_ner = [AUTO_PART, AUTO_FUNC, INSURANCE_COMPANY, INSURANCE, ONTOLOGY,
              AUTO_PHEN, PROJECT]
# QA 返回topn 数目
TopN = 3

# 疑问词
interrogative_method = [u'处理', u'怎么办', u'解决', u'如何', u'怎么处理',
                        u'怎么解决', u'怎样', u'怎么', u'咋整', u'咋',
                        u'咋回事', u'咋处理']
