# _*_ coding: utf-8 _*_
# import pymysql
# from conf.const import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from conf.const import sqlalchemy_engine, sqlalchemy_kwargs
import sys

reload(sys)
sys.setdefaultencoding('utf8')
ENGINE = create_engine(sqlalchemy_engine, **sqlalchemy_kwargs)
Session = sessionmaker(autocommit=True, bind=ENGINE, autoflush=False)
db = Session()


class DataBaseQuery(object):
    """MySQL相关操作"""

    def __init__(self):
        pass

    @staticmethod
    def get(sql):
        # db = pymysql.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWD, MYSQL_DB, charset='utf8')
        # cursor = db.cursor(pymysql.cursors.DictCursor)
        # cursor.execute(sql)
        # data = cursor.fetchall()
        # db.close()
        data = db.execute(sql).fetchall()
        db.close()
        return data


db_query = DataBaseQuery()
