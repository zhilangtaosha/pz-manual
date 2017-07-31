# _*_ coding: utf-8 _*_

from const import *

#  debug模式
debug = True

# 分词长度
max_seg_len = 10

response = {
    RP_RC: 0,
    RP_SC: 0,
    RP_ERROR: "",
    RP_TEXT: "",
    RP_TOPIC: "",
    RP_INTENT: "",
    RP_SEMANTIC: {
        RP_SLOTS: {
        }
    },
    RP_DATA: {
        RP_RESULT: {
        }
    },
    RP_ANSWER: {
        RP_RESULT: {
            RP_ANSWER_STATE: 0
        }
    },
    RP_TIPS: {
    },
    RP_APPENDIX: {
    }
}
