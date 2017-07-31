# _*_ coding: utf-8 _*_

from nlg.biz.insurance import InsuranceGeneration
from nlg.biz.maintenance import MaintenanceGeneration
from nlg.biz.manual import ManualGeneration
from nlg.biz.qasystem import QASysGeneration
from nlg.biz.trouble import BrokenDownGeneration

# 将继承于Generation类的业务子类，加入到该列表中
GENERATIONS_CLS = [InsuranceGeneration, ManualGeneration,
                   QASysGeneration, BrokenDownGeneration,
                   MaintenanceGeneration]
