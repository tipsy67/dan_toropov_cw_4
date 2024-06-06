from abc import ABC, abstractmethod
import requests


class MainAPI(ABC):
    """
    Родительский абстрактный метод, обязывающий создавать
    метод для получения JSON с определенным именем
    """

    @abstractmethod
    def load_vacancies(self, *args, **kwargs):
        pass


class HeadHunterAPI(MainAPI):

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies1'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100, 'search_field': ''}
        self.vacancies = []

    def load_vacancies(self, keyword, search_fields):
        self.params['text'] = keyword
        self.params['search_field'] = search_fields
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
        return self.vacancies[0]
