# _*_ coding: utf-8 _*_

import os

# 项目根目录，结尾不带路径分隔符
project_dir = os.path.dirname(os.path.abspath(__file__))

# 路径分隔符，适应不同的操作系统平台
path_sep = os.path.sep


def get_dir(abs_path):
    """
    计算abs_path的目录，结尾不带路径分隔符
    :param abs_path: 
    :return: 
    """
    return os.path.dirname(os.path.abspath(abs_path))


def cwd(abs_path):
    """
    计算abs_path当前工作路径，结尾带路径分隔符
    :param abs_path: 
    :return: 
    """
    return get_dir(abs_path) + path_sep


if __name__ == '__main__':
    print project_dir
    print path_sep
    print get_dir(__file__)
    print cwd(__file__)
