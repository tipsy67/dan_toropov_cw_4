from src.interactive import UserQuery


def test_text_query(test_user_query):
    assert test_user_query.text_query == 'java'

def test_search_fields(test_user_query):
    assert test_user_query.search_fields == ['1']

def test_top_n(test_user_query):
    assert test_user_query.top_n == '1'

def test_filter_words(test_user_query):
    assert test_user_query.filter_words == ['flask']

def test_salary_range(test_user_query):
    assert test_user_query.salary_range ==['100000', '150000']
def test_is_rewrite(test_user_query):
    assert test_user_query.is_rewrite == '2'

def test_remember_query(test_user_query):
    test_dict =  {
       'filter_words': [
           'flask',
       ],
       'is_rewrite': '2',
       'salary_range': [
           '100000',
           '150000',
       ],
       'search_fields': [
           '1',
       ],
       'text_query': 'java',
       'top_n': '1',
   }

    UserQuery.remember_query(test_user_query)
    assert test_user_query.last_user_query == test_dict


# def test_input_processing():
#     assert isinstance(UserQuery.input_processing('message', 'key'), str)
