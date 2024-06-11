import pytest

from src.api import Currency
from src.interactive import UserQuery
from src.vacancies import Vacancy


@pytest.fixture
def test_currency():
    currency = Currency('test_url')
    Currency.currency_rate = {
        "date": "2024-06-10",
        "rub": {
            "byn": 0.02,
            "byr": 200.33285834,
            "rub": 1,
            "usd": 0.01,
        }
    }
    return currency


@pytest.fixture
def test_00_vacancy():
    return Vacancy(**{"name": "Back-End Engineer - Python, Django, AWS, Integrations",
                      "salary": [89051, 445257], "area": "Великобритания",
                      "url": "https://hh.ru/vacancy/101501668",
                      "employment": "Частичная занятость",
                      "experience": "От 3 до 6 лет",
                      "schedule": "Полный день",
                      "description": "2+ years of working experience in backend development..."}
                   )


@pytest.fixture
def test_01_vacancy():
    return Vacancy(**{"name": "Senior / middle Python (наставник) для junior part-time",
                      "salary": [150000, 250000],
                      "area": "Москва",
                      "url": "https://hh.ru/vacancy/101324026",
                      "employment": "Частичная занятость",
                      "experience": "От 3 до 6 лет",
                      "schedule": "Удаленная работа",
                      "description": "Опыт работы backend-разработчиком flask от 3 лет... "}
                   )


@pytest.fixture
def test_list_vacancies(test_00_vacancy, test_01_vacancy):
    return [test_00_vacancy, test_01_vacancy]


@pytest.fixture
def test_user_query():
    user_query = UserQuery.__new__(UserQuery)
    print(user_query.__dict__)
    user_query._UserQuery__text_query = 'java'
    user_query._UserQuery__search_fields = ['1']
    user_query._UserQuery__top_n = '1'
    user_query._UserQuery__filter_words = ['flask']
    user_query._UserQuery__salary_range = ['100000', '150000']
    user_query._UserQuery__is_rewrite = '2'

    return user_query