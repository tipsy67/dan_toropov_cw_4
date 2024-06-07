import json

from src.api import HeadHunterAPI
from src.exceptions import ExitException
from src.interactive import UserQuery
from src.settings import PATH_TO_JSON
from src.vacancies import Vacancy


def user_interaction() -> None:
    """
    Функция взаимодействия с пользователем
    :return:
    """
    new_user_query = UserQuery()
    UserQuery.remember_query(new_user_query)

    print("Немного подождите, идет загрузка...")
    hh_api = HeadHunterAPI()
    try:
        json_vacancies = hh_api.load_vacancies(new_user_query)
    except KeyError:
        print("Проблемы с загрузкой.")
        json_vacancies = {}

    list_vacancies = Vacancy.parse_from_hh(json_vacancies)
    json_string = json.dumps(list_vacancies, default=Vacancy.vacancy_to_json, ensure_ascii=False, indent=4)

    with open(PATH_TO_JSON, mode='w', encoding='utf-8') as file:
        json.dump(json_string, file, ensure_ascii=False)


if __name__ == '__main__':
    try:
        user_interaction()
        user_interaction()
    except ExitException:
        print("Поиск закончен.")
