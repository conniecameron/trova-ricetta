import abc
#from db.mysql_repository import *

class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_ricetta(self):
        raise NotImplementedError