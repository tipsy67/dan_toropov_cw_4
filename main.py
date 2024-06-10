from src.api import HeadHunterAPI, Currency
from src.exceptions import ExitException
from src.filesaver import JSONSaver
from src.interactive import UserQuery
from src.settings import PATH_TO_JSON, URL_CURRENCY
from src.utils import filter_vacancies_by_words, filter_vacancies_by_salary
from src.vacancies import Vacancy


def user_interaction() -> None:
    """
    Функция взаимодействия с пользователем
    :return:
    """
    print("Немного подождите, загружаем курсы валют...")
    currency = Currency(URL_CURRENCY)
    currency.update()

    new_user_query = UserQuery()
    UserQuery.remember_query(new_user_query)

    print(new_user_query.__dict__)

    print("Немного подождите, идет загрузка...")
    hh_api = HeadHunterAPI()
    json_vacancies = hh_api.load_vacancies(new_user_query)

    list_vacancies = Vacancy.parse_from_hh(json_vacancies)

    with JSONSaver(PATH_TO_JSON, 'r+', Vacancy.vacancy_to_json) as js:
        if new_user_query.is_rewrite == '1':
            old_list = js.load_vacancies()
            list_vacancies.extend(old_list)
        js.delete_all()
        js.write_vacancies(list_vacancies)

    list_vacancies = filter_vacancies_by_words(list_vacancies, new_user_query)

    list_vacancies = filter_vacancies_by_salary(list_vacancies, new_user_query)

    list_vacancies = sorted(list_vacancies, reverse=True)

    upper_cut_limit = int(new_user_query.top_n)
    list_vacancies = list_vacancies[:upper_cut_limit]

    for vacancy in list_vacancies:
        print(vacancy)

    input("Для продолжения нажмите Enter или введите exit для выхода")


if __name__ == '__main__':
    try:
        while True:
            user_interaction()
    except ExitException:
        print("Поиск закончен.")
    except KeyError:
        print("Проблемы с загрузкой")
