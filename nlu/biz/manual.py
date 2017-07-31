# _*_ coding: utf-8 _*_

from conf.const import *
from conf.manual_frame import manual_frames
from conf.manual_syno import manual_synos
from data.rdb import db_query
from nlu.topic import Topic


class ManualTopic(Topic):
    """"""

    def __init__(self):
        super(ManualTopic, self).__init__()
        self._topicid = TopicID.ManualTopic
        self._domain = DOMAIN_MANUAL
        self._intent = INTENT_QUERY

    @staticmethod
    def get_field_by_part(part, field):
        sql = "select m.%s from gs8_manual_v3 m WHERE m.part = '%s'" % (field, part)
        data = db_query.get(sql)
        return list(set([item[0].encode('utf-8') for item in data if item[0] != '']))

    @staticmethod
    def get_field_by_parent(parent, field):
        sql = "select m.%s from gs8_manual_v3 m WHERE m.parent = '%s'" % (field, parent)
        data = db_query.get(sql)
        return list(set([item[0].encode('utf-8') for item in data if item[0] != '']))

    def parse(self, query_info):
        super(ManualTopic, self).parse(query_info)

        interactive_state = False

        if self.stateid == TopicStateID.SelectManualOption:
            query = query_info.get_text()
            semantic = self.get_semantic()
            entity_name = semantic.name
            hyponymy = semantic.hyponymy
            field = self.arguments[FIELD]
            val = self._get_value(query, entity_name, field, hyponymy)
            interactive_state = val != ''
            if interactive_state:
                semantic.slots[field] = val

        if not interactive_state:
            self.set_stateid(TopicStateID.Null)
            semantic = self.get_semantic()
            semantic.clear()
            query = query_info.get_text()
            entity_name, hyponymy = self._get_entity(query_info)
            query = query.replace(entity_name, '')
            if entity_name == '':
                return False
            frame = self._get_frame(entity_name)
            if frame is None:
                return False
            slots = frame[SLOTS]
            for arg, val in slots.items():
                slots[arg] = self._get_value(query, entity_name, arg, hyponymy)
            if hyponymy == PART:
                slots[PART] = entity_name
            semantic.slots = slots
            semantic.domain = frame[DOMAIN]
            semantic.intent = frame[INTENT]
            semantic.name = entity_name
            semantic.hyponymy = hyponymy
        return True

    def _get_value(self, query, entity_name, field_name, hyponymy):
        data_set = []
        if hyponymy == PARENT:
            data_set = self.get_field_by_parent(entity_name, field_name)
        elif hyponymy == PART:
            data_set = self.get_field_by_part(entity_name, field_name)
        data_set.sort(key=lambda x: len(x), reverse=True)
        if len(data_set) == 0:
            return ''
        if entity_name in manual_synos and field_name in manual_synos[entity_name]:
            synos_ = manual_synos[entity_name][field_name]
            for std in data_set:
                if std in synos_:
                    for syno in synos_[std]:
                        if syno in query:
                            return std
        return ''

    def _get_frame(self, entity_name):
        if entity_name in manual_frames:
            return manual_frames[entity_name]
        return None

    @staticmethod
    def _get_entity(query_info):
        # todo 根据动词进行语义消歧
        entities = query_info.get_entities()
        query = query_info.get_text().encode('utf-8')
        entity_names = []
        for entity in entities:
            cont_ner = entity.cont_ner
            if isinstance(cont_ner, unicode):
                cont_ner = cont_ner.encode('utf-8')
            entity_names.append(cont_ner)
        # entity_names = [entity.cont_ner for entity in entities]
        entity, hyponymy = '', 'part'
        if len(set(['空调', '温度', '除霜', '出风模式']) & set(entity_names)) > 0:
            entity = '空调'
        elif len(set(['电器盒', '保险盒']) & set(entity_names)) > 0:
            entity = '保险盒'
        elif '电源' in entity_names:
            entity = '电源'
        elif '蓝牙' in entity_names:
            entity = '蓝牙'
        elif '电话' in entity_names:
            entity = '电话'
        elif 'USB音源' in entity_names:
            entity = 'USB音源'
        elif '音效' in entity_names:
            entity = '音效'
        elif 'USB视频' in entity_names:
            entity = 'USB视频'
        elif 'USB图片' in entity_names:
            entity = 'USB图片'
        elif '儿童座椅' in entity_names:
            entity = '儿童座椅'
        elif '安全带' in entity_names:
            entity = '安全带'
        elif '扶手' in entity_names:
            entity = '扶手'
        elif '头枕' in entity_names:
            entity = '头枕'
        elif len(set(['座椅', '座椅通风']) & set(entity_names)) > 0:
            entity = '座椅'
        elif len(set(['雨刮', '刮水']) & set(entity_names)) > 0:
            entity = '雨刮'
        elif '天窗' in entity_names and '遮阳板' not in entity_names:
            entity = '天窗'
        elif '遮阳板' in entity_names:
            entity = '遮阳板'
        elif '车灯' in entity_names:
            entity = '车灯'
            hyponymy = 'parent'
        elif '角灯' in entity_names:
            entity = '角灯'
        elif '开门灯' in entity_names:
            entity = '开门灯'
        elif '阅读灯' in entity_names:
            entity = '阅读灯'
        elif '近光灯' in entity_names:
            entity = '近光灯'
        elif '日间行车灯' in entity_names:
            entity = '日间行车灯'
        elif '上车照明灯' in entity_names:
            entity = '上车照明灯'
        elif '双闪灯' in entity_names:
            entity = '双闪灯'
        elif '雾灯' in entity_names:
            entity = '雾灯'
        elif '小灯' in entity_names:
            entity = '小灯'
        elif '迎宾照明灯' in entity_names:
            entity = '迎宾照明灯'
        elif '远光灯' in entity_names:
            entity = '远光灯'
        elif '智能迎宾灯' in entity_names:
            entity = '智能迎宾灯'
        elif '转向灯' in entity_names:
            entity = '转向灯'
        elif '曲目' in entity_names:
            entity = '曲目'
        elif len(set(['收音机', '存台', '频道', '波段', '搜台', '电台']) & set(entity_names)) > 0:
            entity = '收音机'
        elif '方向盘' in entity_names:
            entity = '方向盘'
        elif '喇叭' in entity_names:
            entity = '喇叭'
        elif '点烟器照明灯' in entity_names:
            entity = '点烟器照明灯'
        elif '定速巡航' in entity_names:
            entity = '定速巡航'
        elif '氛围灯' in entity_names:
            entity = '氛围灯'
        elif '行李箱照明灯' in entity_names:
            entity = '行李箱照明灯'
        elif '后视镜' in entity_names:
            entity = '后视镜'
        elif '手套箱照明灯' in entity_names:
            entity = '手套箱照明灯'
        elif '照明灯' in entity_names:
            entity = '照明灯'
        elif '发动机' in entity_names:
            entity = '发动机'
        elif '保险丝' in entity_names:
            entity = '保险丝'
        elif '杯架' in entity_names:
            entity = '杯架'
        elif '备胎' in entity_names:
            entity = '备胎'
        elif '并线辅助系统' in entity_names:
            entity = '并线辅助系统'
        elif '玻璃水' in entity_names:
            entity = '玻璃水'
        elif '车窗' in entity_names:
            entity = '车窗'
        elif '车道偏离预警系统' in entity_names:
            entity = '车道偏离预警系统'
        elif len(set(['车门', '自动解锁', '自动上锁', '自动锁车']) & set(entity_names)) > 0 \
                or '锁车' in query:
            entity = '车门'
        elif '车门礼貌灯' in entity_names:
            entity = '车门礼貌灯'
        elif '电子稳定系统' in query:
            entity = '车身电子稳定系统'
        elif '倒车雷达系统' in entity_names:
            entity = '倒车雷达系统'
        elif '电子手刹' in entity_names:
            entity = '电子手刹'
        elif '儿童安全锁' in entity_names:
            entity = '儿童安全锁'
        elif '发动机' in entity_names:
            entity = '发动机'
        elif '发动机舱盖' in entity_names:
            entity = '发动机舱盖'
        elif '防盗警报' in entity_names:
            entity = '防盗警报'
        elif '服务中心' in entity_names:
            entity = '服务中心'
        elif '行李箱照明灯' in entity_names:
            entity = '行李箱照明灯'
        elif '后视镜' in entity_names:
            entity = '后视镜'
        elif '化妆镜照明灯' in entity_names:
            entity = '化妆镜照明灯'
        elif '换挡拨片' in entity_names:
            entity = '换挡拨片'
        elif '机油' in entity_names:
            entity = '机油'
        elif '警告牌' in entity_names:
            entity = '警告牌'
        elif '冷却液' in entity_names:
            entity = '冷却液'
        elif '螺栓' in entity_names:
            entity = '螺栓'
        elif '轮胎' in entity_names:
            entity = '轮胎'
        elif '牌照灯' in entity_names:
            entity = '牌照灯'
        elif '千斤顶' in entity_names:
            entity = '千斤顶'
        elif '牵引钩' in entity_names:
            entity = '牵引钩'
        elif '牵引力控制系统' in entity_names:
            entity = '牵引力控制系统'
        elif '前碰撞预警系统' in entity_names:
            entity = '前碰撞预警系统'
        elif '求救电话' in entity_names:
            entity = '求救电话'
        elif '全地形反馈系统' in entity_names:
            entity = '全地形反馈系统'
        elif '全景泊车系统' in entity_names:
            entity = '全景泊车系统'

        elif '手机互联' in entity_names:
            entity = '手机互联'
        elif '手机无线充电' in entity_names:
            entity = '手机无线充电'
        elif '手套箱' in entity_names:
            entity = '手套箱'
        elif '手套箱照明灯' in entity_names:
            entity = '手套箱照明灯'
        elif '随车工具' in entity_names:
            entity = '随车工具'
        elif '天窗' in entity_names:
            entity = '天窗'
        elif '下坡辅助控制系统' in entity_names:
            entity = '下坡辅助控制系统'
        elif '掀背门' in entity_names:
            entity = '掀背门'
        elif '蓄电池' in entity_names:
            entity = '蓄电池'
        elif '眼镜盒' in entity_names:
            entity = '眼镜盒'
        elif len(set(['仪表', '里程']) & set(entity_names)) > 0:
            entity = '仪表'
        elif '屏幕' in entity_names:
            entity = '屏幕'
        elif '导航地图' in entity_names:
            entity = '导航地图'
        elif '导航系统' in entity_names:
            entity = '导航系统'
        elif '音源' in entity_names:
            entity = '音源'
        elif '语音交互' in entity_names:
            entity = '语音交互'
        elif '音响' in entity_names:
            entity = '音响'
        elif '雨刮' in entity_names:
            entity = '雨刮'
        elif '遮物帘' in entity_names:
            entity = '遮物帘'
        elif '遮阳板' in entity_names:
            entity = '遮阳板'
        elif '制动液' in entity_names:
            entity = '制动液'
        elif '智能启停系统' in entity_names:
            entity = '智能启停系统'
        elif '主动制动辅助系统' in entity_names:
            entity = '主动制动辅助系统'
        elif '自动驻车' in entity_names:
            entity = '自动驻车'
        elif '自适应巡航控制系统' in entity_names:
            entity = '自适应巡航控制系统'
        elif '点烟器' in entity_names:
            entity = '点烟器'
        elif '音响系统' in entity_names:
            entity = '音响系统'
        elif '系统设置' in entity_names:
            entity = '系统设置'
        elif '系统功能' in entity_names:
            entity = '系统功能'
        elif '屏幕保护' in entity_names:
            entity = '屏幕保护'
        elif 'IPOD' in entity_names:
            entity = 'IPOD'
        elif '车辆信息' in entity_names:
            entity = '车辆信息'
        elif '车生活' in entity_names:
            entity = '车生活'
        elif '起动开关' in entity_names:
            entity = '起动开关'
        elif '变速箱' in entity_names:
            entity = '变速箱'
        elif 'P档' in entity_names:
            entity = 'P档'
        elif 'R档' in entity_names:
            entity = 'R档'
        elif 'N档' in entity_names:
            entity = 'N档'
        elif 'D档' in entity_names:
            entity = 'D档'
        elif 'S档' in entity_names:
            entity = 'S档'
        elif '驾驶模式' in entity_names:
            entity = '驾驶模式'
        elif '车辆' in entity_names:
            entity = '车辆'
        elif '电子驻车制动系统' in entity_names:
            entity = '电子驻车制动系统'
        elif '启停系统' in entity_names:
            entity = '启停系统'
        elif '自适应巡航' in entity_names:
            entity = '自适应巡航'
        elif '油箱盖' in entity_names:
            entity = '油箱盖'
        elif '保险盒' in entity_names:
            entity = '保险盒'
        elif '电瓶' in entity_names:
            entity = '电瓶'
        elif '机械钥匙' in entity_names:
            entity = '机械钥匙'
        elif '遥控钥匙' in entity_names:
            entity = '遥控钥匙'
        return entity, hyponymy
