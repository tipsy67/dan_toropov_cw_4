from abc import ABC, abstractmethod
import requests

from src.interactive import UserQuery
from src.settings import VACANCY_SEARCH_FIELDS, VACANCY_SEARCH_PER_PAGE, VACANCY_SEARCH_PAGE, TAGS_FOR_REMOVE


class MainAPI(ABC):
    """
    Обяжем создавать метод со дним названием для получения JSON
    из разных ресурсов
    """

    @abstractmethod
    def load_vacancies(self, *args, **kwargs):
        pass


class HeadHunterAPI(MainAPI):
    """
    Класс для получения списка вакансий с ресурса НН
    """
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': VACANCY_SEARCH_PER_PAGE, 'search_field': ''}
        self.vacancies = []

    def load_vacancies(self, user_query: UserQuery):
        """
        Получаем список вакансий в виде словаря
        :param user_query: пользовательский запрос
        'text_query' - текст запроса
        'search_fields' - 1 по названию вакансии
                        - 2 по названию вакансии и описанию
        :return:
        """
        self.params['text'] = user_query.text_query
        self.params['search_field'] = VACANCY_SEARCH_FIELDS[user_query.search_fields]
        while self.params.get('page') != VACANCY_SEARCH_PAGE:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
        return self.vacancies


class Currency:
    """
    Для получения курса валют по заданной ссылке на JSON файл
    """
    __slots__ = ['user_url']
    currency_rate = {}

    def __init__(self, user_url):
        self.user_url = user_url

    def update(self):
        Currency.currency_rate = requests.get(self.user_url).json()

    @classmethod
    def get_rate(cls, currency) -> float | int:
        """
        Вернем коэффициент отношения заданной валюты к рублю
        :param currency: трехбуквенный валютный код
        :return:
        """
        currency = currency.lower()
        if currency == 'byr':
            currency = 'byn'
        return cls.currency_rate['rub'].get(currency, 1)

