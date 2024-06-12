from src.utils import filter_vacancies_by_words, filter_vacancies_by_salary


def test_filter_vacancies_by_words(test_list_vacancies, test_user_query):
    assert filter_vacancies_by_words(test_list_vacancies, test_user_query) == [test_list_vacancies[1]]
    test_user_query._UserQuery__filter_words = []
    assert filter_vacancies_by_words(test_list_vacancies, test_user_query) == test_list_vacancies


def test_filter_vacancies_by_salary(test_list_vacancies, test_user_query):
    assert filter_vacancies_by_salary(test_list_vacancies, test_user_query) == test_list_vacancies
    test_user_query._UserQuery__salary_range = ['90000', '100000']
    assert filter_vacancies_by_salary(test_list_vacancies, test_user_query) == [test_list_vacancies[0]]
