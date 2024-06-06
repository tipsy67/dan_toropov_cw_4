import json

from src.api import HeadHunterAPI
from src.exceptions import ExitException
from src.interactive import input_processing, input_search_fields, input_top_n, input_filter_words, input_salary_range
from src.settings import PATH_TO_JSON, VACANCY_SEARCH_FIELDS

def user_interaction() -> None:
    """
    Функция взаимодействия с пользователем
    :return:
    """
    print("Поиск вакансий. Для выхода из программы в любой момент введите: exit")

    text_query = input_processing("Введите текст запроса для поиска вакансии:")
    search_fields = input_search_fields()
    top_n = input_top_n()
    filter_words = input_filter_words()
    salary_range = input_salary_range()

    print("Немного подождите, идет загрузка...")
    hh_api = HeadHunterAPI()
    try:
        json_vacancies = hh_api.load_vacancies(text_query, VACANCY_SEARCH_FIELDS[search_fields])
    except KeyError:
        print("Проблемы с загрузкой.")
        json_vacancies = {}

    print(json_vacancies)

    with open(PATH_TO_JSON, mode='w', encoding='utf-8') as file:
        json.dump(json_vacancies, file, ensure_ascii=False)


if __name__ == '__main__':
    try:
        user_interaction()
    except ExitException:
        print("Поиск закончен.")
