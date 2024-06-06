from abc import ABC, abstractmethod


class MainSaver(ABC):
    @abstractmethod
    def add_vacancy(self):
        pass

    @abstractmethod
    def del_vacancy(self):
        pass

class JSONSaver(MainSaver):

    def add_vacancy(self):
        pass

