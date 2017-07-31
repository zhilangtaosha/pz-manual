# _*_ coding: utf-8 _*_

from const import PART, HYPON, PARENT, SLOTS, DOMAIN, DOMAIN_MANUAL, INTENT, INTENT_QUERY

manual_frames = {
    '空调': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '空调',
        HYPON: PART,
        SLOTS: {PART: '', 'function': '', 'property': '', 'position': '', 'category': '', 'operate': ''}},
    '车灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '车灯',
        HYPON: PARENT,
        SLOTS: {PART: '', 'operate': '', 'function': '', 'position': '', 'condition': ''}},
    '角灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '角灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '安全带': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '安全带',
        HYPON: PART,
        SLOTS: {PART: '', 'property': '', 'position': '', 'operate': ''}},
    '点烟器照明灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '点烟器照明灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '定速巡航': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '定速巡航',
        HYPON: PART,
        SLOTS: {PART: '', 'property': '', 'operate': ''}},
    '儿童座椅': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '儿童座椅',
        HYPON: PART,
        SLOTS: {PART: '', 'category': '', 'operate': ''}},
    '方向盘': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '方向盘',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': '', 'property': ''}},
    '氛围灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '氛围灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '扶手': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '扶手',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': '', 'position': ''}},
    '行李箱照明灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '行李箱照明灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '机械钥匙': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '机械钥匙',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '近光灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '近光灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '开门灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '开门灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '喇叭': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '喇叭',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '日间行车灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '日间行车灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '上车照明灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '上车照明灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '双闪灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '双闪灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '手套箱照明灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '手套箱照明灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '天窗': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '天窗',
        HYPON: PART,
        SLOTS: {PART: '', 'category': '', 'operate': '', 'condition': ''}},
    '雾灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '雾灯',
        HYPON: PART,
        SLOTS: {PART: '', 'position': '', 'operate': ''}},
    '小灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '小灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '迎宾照明灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '迎宾照明灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '遥控钥匙': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '遥控钥匙',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': '', 'property': ''}},
    '头枕': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '头枕',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '阅读灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '阅读灯',
        HYPON: PART,
        SLOTS: {PART: '', 'position': '', 'operate': ''}},
    '远光灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '远光灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '雨刮': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '雨刮',
        HYPON: PART,
        SLOTS: {PART: '', 'function': '', 'position': '', 'operate': '', 'category': ''}},
    '照明灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '照明灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '遮阳板': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '遮阳板',
        HYPON: PART,
        SLOTS: {PART: '', 'category': '', 'operate': ''}},
    '智能迎宾灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '智能迎宾灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '转向灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '转向灯',
        HYPON: PART,
        SLOTS: {PART: '', 'position': '', 'operate': ''}},
    '座椅': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '座椅',
        HYPON: PART,
        SLOTS: {PART: '', 'property': '', 'position': '', 'operate': '', 'function': '', 'condition': ''}},
    '发动机': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '发动机',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': '', 'condition': ''}},
    '保险丝': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '保险丝',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '杯架': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '杯架',
        HYPON: PART,
        SLOTS: {PART: '', 'position': '', 'operate': ''}},
    '备胎': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '备胎',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '并线辅助系统': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '并线辅助系统',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '玻璃水': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '玻璃水',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '车窗': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '车窗',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': '', 'condition': ''}},
    '车道偏离预警系统': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '车道偏离预警系统',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '车门': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '车门',
        HYPON: PART,
        SLOTS: {PART: '', 'function': '', 'operate': '', 'condition': ''}},
    '车门礼貌灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '车门礼貌灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '车身电子稳定系统': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '车身电子稳定系统',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '倒车雷达系统': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '倒车雷达系统',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '电子手刹': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '电子手刹',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '儿童安全锁': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '儿童安全锁',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '发动机舱盖': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '发动机舱盖',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '防盗警报': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '防盗警报',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': '', 'condition': ''}},
    '服务中心': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '服务中心',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '后视镜': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '后视镜',
        HYPON: PART,
        SLOTS: {PART: '', 'function': '', 'property': '', 'position': '', 'operate': '', 'condition': ''}},
    '化妆镜照明灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '化妆镜照明灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '换挡拨片': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '换挡拨片',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '机油': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '机油',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '警告牌': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '警告牌',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '冷却液': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '冷却液',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '轮胎': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '轮胎',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '螺栓': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '螺栓',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '牌照灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '牌照灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '千斤顶': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '千斤顶',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '牵引钩': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '牵引钩',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': '', 'position': ''}},
    '牵引力控制系统': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '牵引力控制系统',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '求救电话': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '求救电话',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '全地形反馈系统': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '全地形反馈系统',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '全景泊车系统': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '全景泊车系统',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '收音机': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '收音机',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': '', 'function': '', 'condition': ''}},
    '手机互联': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '手机互联',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '手机无线充电': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '手机无线充电',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '手套箱': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '手套箱',
        HYPON: PART,
        SLOTS: {PART: '', 'position': '', 'operate': ''}},
    '随车工具': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '随车工具',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '下坡辅助控制系统': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '下坡辅助控制系统',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '掀背门': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '掀背门',
        HYPON: PART,
        SLOTS: {PART: '', 'property': '', 'operate': '', 'condition': ''}},
    '蓄电池': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '蓄电池',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '眼镜盒': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '眼镜盒',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '仪表': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '仪表',
        HYPON: PART,
        SLOTS: {PART: '', 'function': '', 'operate': '', 'condition': ''}},
    '音响': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '音响',
        HYPON: PART,
        SLOTS: {PART: '', 'function': '', 'operate': '', 'condition': ''}},
    '遮物帘': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '遮物帘',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '制动液': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '制动液',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '智能启停系统': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '智能启停系统',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '主动制动辅助系统': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '主动制动辅助系统',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '自动驻车': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '自动驻车',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '自适应巡航控制系统': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '自适应巡航控制系统',
        HYPON: PART,
        SLOTS: {PART: '', 'property': '', 'operate': ''}},
    '点烟器': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '点烟器',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '电源': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '电源',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': '', 'category': ''}},
    '音响系统': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '音响系统',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': '', 'condition': ''}},
    '屏幕': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '屏幕',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': '', 'condition': ''}},
    '导航系统': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '导航系统',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': '', 'condition': ''}},
    '音源': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '音源',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': '', 'condition': ''}},
    '语音交互': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '语音交互',
        HYPON: PART,
        SLOTS: {PART: '', 'category': '', 'operate': '', 'condition': ''}},
    '系统设置': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '系统设置',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': '', 'condition': ''}},
    '系统功能': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '系统功能',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': '', 'condition': ''}},
    '导航地图': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '导航地图',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': '', 'condition': ''}},
    '曲目': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '曲目',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': '', 'condition': ''}},
    '电话': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '电话',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': '', 'condition': ''}},
    '屏幕保护': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '屏幕保护',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    'USB音源': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: 'USB音源',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': '', 'condition': ''}},
    '音效': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '音效',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    'USB视频': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: 'USB视频',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    'USB图片': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: 'USB图片',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '蓝牙': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '蓝牙',
        HYPON: PART,
        SLOTS: {PART: '', 'function': '', 'operate': '', 'condition': ''}},
    'IPOD': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: 'IPOD',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '车辆信息': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '车辆信息',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '车生活': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '车生活',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '起动开关': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '起动开关',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '变速箱': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '变速箱',
        HYPON: PART,
        SLOTS: {PART: '', 'function': ''}},
    'P档': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: 'P档',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    'R档': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: 'R档',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    'N档': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: 'N档',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    'D档': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: 'D档',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    'S档': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: 'S档',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '驾驶模式': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '驾驶模式',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': '', 'category': ''}},
    '车辆': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '车辆',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '电子驻车制动系统': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '电子驻车制动系统',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '启停系统': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '启停系统',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '自适应巡航': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '自适应巡航',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': '', 'property': ''}},
    '油箱盖': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '油箱盖',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '保险盒': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '保险盒',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': '', 'category': ''}},
    '电瓶': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '电瓶',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '四轮驱动锁止模式指示灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '四轮驱动锁止模式指示灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '充电系统报警灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '充电系统报警灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '发动机故障指示灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '发动机故障指示灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '机油压力低报警灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '机油压力低报警灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '排放故障指示灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '排放故障指示灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '左转向信号与危险警告指示灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '左转向信号与危险警告指示灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '车道偏移状态指示灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '车道偏移状态指示灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '前碰预警状态指示灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '前碰预警状态指示灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '发动机冷却液温度高指示灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '发动机冷却液温度高指示灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '辅助保护系统指示灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '辅助保护系统指示灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '燃油低指示灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '燃油低指示灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '自适应巡航指示灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '自适应巡航指示灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '右转向信号与危险警告指示灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '右转向信号与危险警告指示灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '防盗启动锁止系统指示灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '防盗启动锁止系统指示灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '电子刹车状态指示灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '电子刹车状态指示灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '电子刹车故障指示灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '电子刹车故障指示灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '手刹车与制动系统指示灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '手刹车与制动系统指示灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '车辆稳定性辅助指示灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '车辆稳定性辅助指示灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '车辆稳定性辅助关闭': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '车辆稳定性辅助关闭',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '防抱死制动系统指示灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '防抱死制动系统指示灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '变速箱故障指示灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '变速箱故障指示灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '胎压检测系统指示灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '胎压检测系统指示灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '电动助力转向指示灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '电动助力转向指示灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '定速巡航指示灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '定速巡航指示灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '前排乘员座椅安全带提示灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '前排乘员座椅安全带提示灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    'ECO经济模式指示灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: 'ECO经济模式指示灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '驾驶员座椅安全带提示灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '驾驶员座椅安全带提示灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '启停系统故障指示灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '启停系统故障指示灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '启停系统工作指示灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '启停系统工作指示灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '远光指示灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '远光指示灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '点灯指示灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '点灯指示灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '前雾灯指示灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '前雾灯指示灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '后雾灯指示灯': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '后雾灯指示灯',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},
    '前碰撞预警系统': {
        DOMAIN: DOMAIN_MANUAL,
        INTENT: INTENT_QUERY,
        PART: '前碰撞预警系统',
        HYPON: PART,
        SLOTS: {PART: '', 'operate': ''}},

}
