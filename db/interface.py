import abc
#from db.mysql_repository import *

class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_ingredients(self):
        raise NotImplementedError