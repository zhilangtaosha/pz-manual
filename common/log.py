# _*_ coding: utf-8 _*_
import os
import time

from conf.const import PROJECT_DIR


# 字节bytes转化kb\m\g
def format_size(bts):
    try:
        bts = float(bts)
        kb = bts / 1024
    except:
        print("传入的字节格式不对")
        return "Error"

    if kb >= 1024:
        M = kb / 1024
        if M >= 1024:
            G = M / 1024
            return "%fG" % (G)
        else:
            return "%fM" % (M)
    else:
        return "%fkb" % (kb)


# 获取文件大小，单位字节
def get_doc_size(path):
    try:
        size = os.path.getsize(path)
        return size
    except Exception as err:
        print(err)


# 获取文件夹大小
def get_file_size(path):
    sumsize = 0
    try:
        filename = os.walk(path)
        for root, dirs, files in filename:
            for fle in files:
                size = os.path.getsize(path + fle)
                sumsize += size
        return format_size(sumsize)
    except Exception as err:
        print(err)


def log(cont):
    cont = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ': \t' + cont + '\n'
    log_file_name = PROJECT_DIR + 'log/log_file.txt'
    if not os.path.exists(log_file_name):
        log_file = open(log_file_name, 'w')
        log_file.close()
    if get_doc_size(log_file_name) > 52428800:  # 50M
        os.rename(log_file_name, log_file_name + str(int(time.time())))
        log_file = open(log_file_name, 'w')
    else:
        log_file = open(log_file_name, 'a')
    log_file.write(cont.encode("utf-8"))
    log_file.close()
