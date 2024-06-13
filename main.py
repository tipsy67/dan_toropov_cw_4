import pandas as pd

from src.api import HeadHunterAPI, Currency
from src.exceptions import ExitException
from src.filesaver import JSONSaver
from src.interactive import UserQuery
from src.settings import PATH_TO_JSON, URL_CURRENCY, PATH_TO_EXCEL
from src.utils import filter_vacancies_by_words, filter_vacancies_by_salary
from src.vacancies import Vacancy


def user_interaction() -> None:
    """
    Функция взаимодействия с пользователем
    :return:
    """
    new_user_query = UserQuery()

    print("Немного подождите, идет загрузка...")
    hh_api = HeadHunterAPI()
    json_vacancies = hh_api.load_vacancies(new_user_query)

    list_vacancies = Vacancy.parse_from_hh(json_vacancies)

    with JSONSaver(PATH_TO_JSON, 'a+', Vacancy.vacancy_to_json) as js:
        if new_user_query.is_rewrite == '1' and not js.is_file_not_empty():
            old_list = js.load_vacancies()
            list_vacancies.extend(old_list)
        js.delete_all()
        js.write_vacancies(list_vacancies)

    try:
        while True:
            new_user_query.get_data_for_details()
            UserQuery.remember_query(new_user_query)

            filtered_vacancies = filter_vacancies_by_words(list_vacancies, new_user_query)

            filtered_vacancies = filter_vacancies_by_salary(filtered_vacancies, new_user_query)

            filtered_vacancies = sorted(filtered_vacancies, reverse=True)

            upper_cut_limit = int(new_user_query.top_n)
            filtered_vacancies = filtered_vacancies[:upper_cut_limit]
            print()
            print("Результат поиска")
            print("-" * 30)
            Vacancy.clear_data_frame()
            for vacancy in filtered_vacancies:
                print(vacancy)
                Vacancy.vacancy_to_data_frame(vacancy)
            print("-" * 30)

    except ExitException:
        print()

    df = pd.DataFrame(Vacancy.data_frame)
    df.to_excel(PATH_TO_EXCEL)

    print(f"\nРезультат сохранен в файл {PATH_TO_EXCEL}")
    print("-" * 30)


if __name__ == '__main__':
    try:
        print("Немного подождите, загружаем курсы валют...")
        currency = Currency(URL_CURRENCY)
        currency.update()

        while True:
            user_interaction()
    except ExitException:
        print("Поиск закончен.")
    except (KeyError, ConnectionError):
        print("Проблемы с загрузкой")
