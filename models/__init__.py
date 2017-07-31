# _*_ coding: utf-8 _*_

import sys

from model_mgr import mod_mgr
from models.model import SimpleModel
from utils.seg import segment

segment.seg('')

__import__('models.biz.biz_models')
models_module = sys.modules['models.biz.biz_models']
att_list = dir(models_module)
for att_name in att_list:
    att = getattr(models_module, att_name)
    if type(att) == type and issubclass(att, SimpleModel):
        mod_mgr.register(att())
