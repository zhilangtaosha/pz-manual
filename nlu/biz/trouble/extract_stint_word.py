# _*_ coding: utf-8 _*_
import re


def opt_from(query):
    pat ="智慧传祺|打方向|(?:轻)?(?:点|松|踩)(?:油门|刹车)|急刹车|油箱加满|ECO模式|升(?:挡|档)|放置.*时间|加油"

    com = re.compile(pat)
    result = com.findall(query)
    result = list(set(result))
    return result


def kind_from(query):
    pass
#     pat = "智能"
#     com = re.compile(pat)
#     try:
#         result = com.search(query).group()
#     except AttributeError as e:
#         result = ''
#     return result


def road_from(query):
    pat = "颠簸|减速带|坡(?:道)?|不平|坑(?:洼)?|坎"
    com = re.compile(pat)
    try:
        result = com.search(query).group()
    except AttributeError as e:
        result = ''
    return result


def running_from(query):
    pat = "行驶|怠速|启动|起步|停车|原地"
    com = re.compile(pat)
    try:
        result = com.search(query).group()
    except AttributeError as  e:
        result = ''
    return result


def speed_from(query):
    pat = "高速|低速"
    com = re.compile(pat)
    try:
        result = com.search(query).group()
    except AttributeError as e:
        result = ''
    return result


def start_from(query):
    pat = "(冷|凉)(?:车)?启动"
    com = re.compile(pat)
    try:
        result = com.search(query).group(1)
    except AttributeError as e:
        result = ''
    return result


def position_from(query):
    pat = "左|右|(?:前|后)部|副驾驶|车内"
    com = re.compile(pat)
    try:
        result = com.search(query).group()
    except AttributeError as e:
        result = ''
    return result

def weather_from(query):
    pat = "雨天|雨后"
    com = re.compile(pat)
    result = com.findall(query)
    return result

def gear_from(query):
    pat = '(P|R|N|D|1|2|3|4|倒|p|r|d|d)(?:档|挡)'
    com = re.compile(pat)
    result = com.findall(query)
    result = [x.upper() for x in result]
    return result

# if __name__ == "__main__":
#     dic = {"opt":opt_from,"kind":kind_from,"road":road_from,"runing":running_from,
#            "speed":speed_from,"start":start_from,"position":position_from,
#            "weather":weather_from,"gear":gear_from
#            }
#
#
#
#
#     from xlrd import *
#     excel = open_workbook("/home/an/uploads/gs8_test_re.xls")
#     sheet = excel.sheet_by_index(0)
#
#     row_num = sheet.nrows
#     for i in range(1,row_num):
#         query = sheet.cell_value(i,0)
#         query = query.encode('utf-8')
#         for k,v in dic.items():
#
#             result = v(query)
#             print query
#             print k
#             if isinstance(result,str):
#                 print result
#             if isinstance(result,list):
#                 for j in result:
#                     print j