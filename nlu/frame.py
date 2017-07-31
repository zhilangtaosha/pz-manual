# _*_ coding: utf-8 _*_

import json

from common.exception import CustomException
from conf.const import *


# class FrameTools(object):
#     """
#
#     """
#
#     def __init__(self):
#         self._frames = {}
#         self._pipelines = {}
#         self._load(project_dir + '/conf/frame', self._frames)
#         # self._load(project_dir + '/conf/pipeline', self._pipelines)
#
#     @staticmethod
#     def _load(fp, obj):
#         for line in open(fp):
#             if line.strip(" ").startswith("#"):
#                 continue
#             if len(line.strip("\n \r")) == 0:
#                 continue
#             try:
#                 j = json.loads(line)
#             except ValueError:
#                 print 'Grammar is wrong: '
#                 print line
#             obj[j[TOPICID]] = j
#
#     def get_frame(self, topicid):
#         if topicid.value in self._frames:
#             return self._frames[topicid.value]
#         return {}
#
#     @property
#     def frames(self):
#         return self._frames
#
#     def get_pipeline(self, topicid):
#         if topicid.value in self._pipelines:
#             return self._pipelines[topicid.value][SLOTS]
#         return {}
#
#     @property
#     def pipelines(self):
#         return self._pipelines
#
#
# frame_tools = FrameTools()


class SemanticFrame(object):
    """
    
    """

    def __init__(self):
        self.domain = None
        self.intent = None
        self.name = None
        self.hyponymy = None
        self.slots = {}

    def load(self, frm):
        """
        从字符串中实例化domain、intent、slots参数
        :param frm: 
        :return: 
        """
        if isinstance(frm, str):
            semantic = json.loads(frm)
        elif isinstance(frm, dict):
            semantic = frm
        else:
            raise CustomException('%s is invalid.' % frm)
        # if DOMAIN in semantic:
        #     self.domain = semantic[DOMAIN]
        # if INTENT in semantic:
        #     self.intent = semantic[INTENT]
        if SLOTS in semantic:
            for arg, val in semantic[SLOTS].items():
                self.slots[arg] = val

    def clear(self):
        for key in self.slots.keys():
            self.slots[key] = ""

    def update(self, arg, val):
        if arg not in self.slots:
            raise CustomException(
                'argument "%s" not in SemanticFrame: Domain:%s, Intent:%s' % (arg, self.domain, self.intent))
        else:
            self.slots[arg] = val

    def get(self, arg):
        return self.slots[arg]

    def add(self, arg, val):
        self.slots[arg] = val
        # if arg not in self._slots:
        #     raise CustomException(
        #         'argument "%s" not in SemanticFrame: Domain:%s, Intent:%s' % (arg, self._domain, self._intent))
        # if val in ['', None]:
        #     return
        # self._slots[arg] = reason_argument_value(self._slots, self._domain, self._intent, arg, val)

        # def _reason(self):
        #     reason_slots(self.domain, self.intent, self.slots)
