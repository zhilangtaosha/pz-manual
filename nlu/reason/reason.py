# _*_ coding: utf-8 _*_


def reason_before_parser(domain, intent, argument, query):
    """
    在Query被解析前，调用该方法，可以修改Query的内容
    :param domain: 
    :param intent: 
    :param argument: 
    :param query: 
    :return: 
    """

    return query


def reason_argument_value(slots, domain, intent, argument, value):
    """
    当向语义Frame中添加slots参数时候，调用该函数
    在该函数中根据domain、intent、argument名称，修改value的值
    :param domain: 
    :param intent: 
    :param argument: 
    :param value: 
    :return: 返回修改后的value
    """
    return value


def reason_slots(domain, intent, slots):
    """
    当Frame解析结束完成时，调用该函数
    根据domain、intent更新slots内容
    :param domain: 
    :param intent: 
    :param slots: 
    """
    # slots.clear()
    pass
