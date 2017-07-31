# _*_ coding: utf-8 _*_


import copy
import json

from conf.const import *


class Response(object):
    """
    {
        "rc": 0,
        "sc": 0,
        "error": "",
        "text": "",
        "topic": "",
        "intent": "",
        "semantic": {
            "slots": {

            }
        },
        "data": {
            "result": {
               "list": [],
               "uplist": [],
               "title": ""
            }
        },
        "answer": {

        },
        "tips": {
        },
        "appendix": {
        }
    }
    """

    def __init__(self):
        self._response = {
            RP_RC: 0,
            RP_SC: 0,
            RP_ERROR: "",
            RP_TEXT: "",
            RP_TOPIC: "",
            RP_INTENT: "",
        }
        self._semantic = {}
        self._data = {}
        self._answer = {}
        self.set_answer({})
        self.set_data({})
        self.set_slots({})

    def set_text(self, text):
        self._response[RP_TEXT] = text

    def set_topic_intent(self, topic_name, intent_name):
        self._response[RP_TOPIC] = topic_name
        self._response[RP_INTENT] = intent_name

    def set_state_code(self, sc):
        assert isinstance(sc, StateCode)
        self._response[RP_SC] = sc.value

    def set_response_code(self, rc):
        assert isinstance(rc, ResponseCode)
        self._response[RP_RC] = rc.value
        if rc == ResponseCode.OK:
            if RP_ERROR in self._response:
                self._response.pop(RP_ERROR)
        else:
            self._response[RP_ERROR] = RESPONSE_CODE_ERROR[rc]

    def set_slots(self, slots):
        assert isinstance(slots, dict)
        self._semantic[RP_SLOTS] = copy.deepcopy(slots)
        self._response[RP_SEMANTIC] = self._semantic

    def set_answer(self, result):
        if len(result) == 0:
            self._answer[RP_ANSWER_STATE] = AnswerState.NoAnswer.value
        else:
            self._answer[RP_ANSWER_STATE] = AnswerState.Normal.value
        self._answer[RP_RESULT] = copy.deepcopy(result)
        self._response[RP_ANSWER] = self._answer

    def set_data(self, data):
        self._data[RP_RESULT] = copy.deepcopy(data)
        self._response[RP_DATA] = self._data

    def get_data(self):
        return self._response[RP_DATA]

    def dumps(self):
        return json.dumps(self._response)

    def is_empty(self):
        if self._answer[RP_ANSWER_STATE] == AnswerState.NoAnswer.value \
                and self._response[RP_SC] == StateCode.Normal.value:
            return True
        return False

    def set(self, topic):
        semantic = topic.get_semantic()
        self.set_slots(semantic.slots)
        self.set_topic_intent(semantic.domain, semantic.intent)
        self.set_text(topic.get_query_info().get_text())
