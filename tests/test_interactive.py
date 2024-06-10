def test_interactive_str(test_user_query):
    assert repr(test_user_query) == ''


def test_interactive_str(test_user_query):
    assert str(test_user_query) == ''


def test_text_query(test_user_query):
    assert test_user_query.text_query == 'java'