# _*_ coding: utf-8 _*_


class ModelMgr(object):
    """

    """

    def __init__(self):
        self._models = {}

    def register(self, model):
        if model.id not in self._models:
            self._models[model.id] = model

    def get(self, model_id):
        return self._models[model_id]


mod_mgr = ModelMgr()
