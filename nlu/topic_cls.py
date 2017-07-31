# _*_ coding: utf-8 _*_

from biz.insurance import InsuranceTopic
from biz.maintenance import MaintenceTopic
from biz.manual import ManualTopic
from biz.qasystem import QASysTopic
from biz.trouble.trouble import BrokenDownTopic

# 将业务Topic类加入到列表中
TOPICS_CLS = [InsuranceTopic, ManualTopic,
              QASysTopic, BrokenDownTopic,
              MaintenceTopic]
