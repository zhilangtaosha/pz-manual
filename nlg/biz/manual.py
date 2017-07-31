# _*_ coding: utf-8 _*_


from conf.const import *
from data.rdb import db_query
from nlg.generation import Generation


class ManualGeneration(Generation):
    """"""

    def __init__(self):
        super(ManualGeneration, self).__init__()
        self._topicid = TopicID.ManualTopic

    def generate(self):
        super(ManualGeneration, self).generate()
        semantic = self.topic.get_semantic()
        hyponymy = semantic.hyponymy
        entity_name = semantic.name
        default = 'part_default'
        grp = 'part_grp'
        if hyponymy == PARENT:
            default = 'parent_default'
            grp = 'parent_grp'
            sql = 'SELECT * FROM gs8_manual_v3 '
            where = ' WHERE parent="车灯" '
        else:
            sql = 'SELECT * FROM gs8_manual_v3'
            where = ''
        for arg, val in semantic.slots.items():
            if val != '':
                if where == '':
                    where = ' where gs8_manual_v3.%s="%s" ' % (arg, val)
                else:
                    where += ' and gs8_manual_v3.%s="%s" ' % (arg, val)
        sql += where
        data = db_query.get(sql)
        cnt = len(data)
        if cnt == 0:
            pass
        elif cnt == 1:
            self.response.set_answer({METHOD: dict(data[0])[METHOD],
                                      # ATTENTION: dict(data[0])[ATTENTION],
                                      IMAGE: dict(data[0])[IMAGE]})
        else:
            if self.topic.stateid != TopicStateID.Null:
                self.response.set_answer({METHOD: dict(data[0])[METHOD],
                                          # ATTENTION: dict(data[0])[ATTENTION],
                                          IMAGE: dict(data[0])[IMAGE]})
                return self.response
            is_break = False
            for row in data:
                if dict(row)[default] == 1:
                    self.response.set_answer({METHOD: dict(row)[METHOD],
                                              # ATTENTION: dict(row)[ATTENTION],
                                              IMAGE: dict(row)[IMAGE]})
                    is_break = True  # todo end topic
                    break
            if not is_break:
                grp_id = dict(data[0])[grp]  # todo 取grpid最多的值
                if grp_id is None:
                    return self.response
                if grp_id == 0:
                    return self.response
                inter_sql = 'select * from gs8_manual_v3_conf where gs8_manual_v3_conf.%s = %d' % (grp, grp_id)
                inter = db_query.get(inter_sql)
                self.response.set_data({TITLE: dict(inter[0])[INTERACTIVE],
                                        LIST: self._format_arg_list(dict(inter[0])[LIST]),
                                        UPLIST: self._format_arg_list(dict(inter[0])[UPLIST])})
                self.response.set_state_code(StateCode.Interactive)
                self.topic.arguments[FIELD] = dict(inter[0])[FIELD]
                self.topic.set_stateid(TopicStateID.SelectManualOption)
        return self.response

    def _format_arg_list(self, args):
        args = args.replace('，', ',').replace(' ', '')
        return args.split(',')
