from src.interactive import UserQuery
from src.vacancies import Vacancy


def filter_vacancies_by_words(list_vacancies: [Vacancy], new_user_query: UserQuery) -> [Vacancy]:
    """
    Вернем список вакансий, отсортированный по ключевым словам
    :param list_vacancies: список вакансий
    :param new_user_query: экземпляр класса, содержащий запрос пользователя для поиска
    :return: отфильрованный список вакансий
    """
    if len(new_user_query.filter_words) > 0:
        new_list_vacancies = []
        for vacancy in list_vacancies:
            for filter_word in new_user_query.filter_words:
                if filter_word in vacancy.search_str:
                    new_list_vacancies.append(vacancy)
                    break
    else:
        new_list_vacancies = list_vacancies
    return new_list_vacancies


def filter_vacancies_by_salary(list_vacancies: [Vacancy], new_user_query: UserQuery) -> [Vacancy]:
    """
    Вернем список вакансий, отсортированный по вилке зарплаты
    Если вилка вакансии попадает одной из границ в границы вилки зарплат в запросе,
    либо обе границы вакансии находится внутри вилки в запросе - то ОК
    :param list_vacancies: список вакансий
    :param new_user_query: экземпляр класса, содержащий запрос пользователя для поиска
    :return: отфильрованный список вакансий
    """
    new_list_vacancies = []
    min_salary = int(new_user_query.salary_range[0])
    max_salary = int(new_user_query.salary_range[1])
    for vacancy in list_vacancies:
        if min_salary <= vacancy.salary[0] <= max_salary or \
                min_salary <= vacancy.salary[1] <= max_salary or \
                (vacancy.salary[0] < min_salary and vacancy.salary[1] > max_salary):
            new_list_vacancies.append(vacancy)

    return new_list_vacancies