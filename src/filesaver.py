import json
from abc import ABC, abstractmethod

from src.settings import TAGS_FOR_REMOVE
from src.vacancies import Vacancy


class MainSaver(ABC):
    __slots__ = ['__filepath', '__mode_open', '__file', '__method']

    @abstractmethod
    def __init__(self, filepath: str, mode_open: str):
        self.__filepath = filepath
        self.__mode_open = mode_open

    @abstractmethod
    def write_vacancies(self, list_vacancies):
        pass

    # @abstractmethod
    # def del_vacancy(self):
    #     pass


class JSONSaver(MainSaver):
    def __init__(self, filepath: str, mode_open: str, method):
        self.__filepath = filepath
        self.__mode_open = mode_open
        self.__method = method

    def __enter__(self):
        self.__file = open(self.__filepath, mode=self.__mode_open, encoding='utf-8')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__file.close()

    def write_vacancies(self, list_obj):
        json_string = json.dumps(list_obj, default=self.__method, ensure_ascii=False)
        # json_string = json_string.replace('"', "'")
        for x in TAGS_FOR_REMOVE:
            json_string = json_string.replace(x, '')

        self.__file.seek(0, 2)
        json.dump(json_string, self.__file, ensure_ascii=False)

    def load_vacancies(self) -> list:
        self.__file.seek(0)
        data = json.load(self.__file)
        data = json.loads(data)
        data = [Vacancy(**x) for x in data]
        return data

    def delete_all(self):
        self.__file.truncate(0)

