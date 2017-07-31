# _*_ coding: utf-8 _*_


from tgrocery import Grocery

from project_property import project_dir


class SimpleModel(object):
    """

    """

    def __init__(self):
        self._id = None
        self._model = None
        self._name = self.__class__.__name__
        self._train_data = ''

    @property
    def id(self):
        return self._id

    def predicate(self, query):
        if self._model is None:
            self._model = AutoGrocery(self._name, self._train_data)
        return self._model.predicate(query)


class AutoGrocery(object):
    """

    """

    def __init__(self, name, train_data):
        self._train_data = train_data
        self._grocery = Grocery(project_dir + '/models/model_data/' + name)

    def train(self):
        self._grocery.train(self._train_data)

    def save(self):
        self._grocery.save()

    def load(self):
        self._grocery.load()

    def predicate(self, src):
        if not self._grocery.get_load_status():
            try:
                self.load()
            except ValueError:
                self.train()
                self.save()
        pr = self._grocery.predict(src)
        label = pr.predicted_y
        return label, pr.dec_values[label]
