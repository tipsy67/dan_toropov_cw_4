import pytest

from src.exceptions import ExitException
from src.interactive import UserQuery
from tests.test_utils_from_github import set_keyboard_input


def test_text_query(test_user_query):
    assert test_user_query.text_query == 'java'


def test_search_fields(test_user_query):
    assert test_user_query.search_fields == '1'


def test_top_n(test_user_query):
    assert test_user_query.top_n == '1'


def test_filter_words(test_user_query):
    assert test_user_query.filter_words == ['flask']


def test_salary_range(test_user_query):
    assert test_user_query.salary_range == ['100000', '150000']


def test_is_rewrite(test_user_query):
    assert test_user_query.is_rewrite == '2'


def test_remember_query(test_user_query):
    test_dict = {
        'filter_words': [
            'flask',
        ],
        'is_rewrite': '2',
        'salary_range': [
            '100000',
            '150000',
        ],
        'search_fields': '1',
        'text_query': 'java',
        'top_n': '1',
    }

    UserQuery.remember_query(test_user_query)
    assert test_user_query.last_user_query == test_dict


def test_input_processing():
    set_keyboard_input(['java'])
    assert UserQuery.input_processing('message', 'key') == 'java'
    with pytest.raises(ExitException):
        set_keyboard_input(['exit'])
        assert UserQuery.input_processing('message', 'key') == 'java'


def test_input_search_fields(test_user_query):
    set_keyboard_input(['java', '7', '2'])
    assert UserQuery.input_search_fields(test_user_query) == '2'


def test_input_is_rewrite(test_user_query):
    set_keyboard_input(['java', '7', '2'])
    assert UserQuery.input_is_rewrite(test_user_query) == '2'


def test_input_top_n(test_user_query):
    set_keyboard_input(['java', '7', '2'])
    assert UserQuery.input_top_n(test_user_query) == '7'


def test_input_filter_words(test_user_query):
    set_keyboard_input(['java lava', '7', '2'])
    assert UserQuery.input_filter_words(test_user_query) == ['java', 'lava']


def test_input_salary_range(test_user_query):
    set_keyboard_input(['java lava', '7', '1- 100'])
    assert UserQuery.input_salary_range(test_user_query) == ['1', '100']


def test_user_query_class():
    set_keyboard_input(['java', '1', '10', 'python', '1-100', '2'])
    test_query = UserQuery()

    assert test_query.text_query == 'java'
    assert test_query.search_fields == '1'
    assert test_query.top_n == '10'
    assert test_query.filter_words == ['python']
    assert test_query.salary_range == ['1', '100']
    assert test_query.is_rewrite == '2'
