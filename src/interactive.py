from src.exceptions import ExitException


def input_processing(message: str) -> str:
    user_input = input(message)
    if user_input.strip(' ').lower() == "exit":
        raise ExitException
    return user_input


def input_search_fields() -> str:
    search_fields = None
    while search_fields not in ('1', '2'):
        search_fields = input_processing("Ввведите цифру:\n"
                                         " 1 - для поиска по наименованию вакансии\n"
                                         " 2 - для поиска по наименованию и описанию вакансии\n")

    return search_fields


def input_top_n() -> str:
    top_n = ''
    while not top_n.isdigit():
        top_n = input_processing("Введите количество вакансий для вывода в топ N: ")

    return top_n


def input_filter_words() -> str:
    filter_words = input_processing("Введите через пробел"
                                    "ключевые слова для фильтрации вакансий: ").split()
    filter_words = [x.replace(' ', '') for x in filter_words]

    return filter_words


def input_salary_range() -> list:
    salary_range = ['', '']
    while not salary_range[0].isdigit() or salary_range[1].isdigit():
        salary_range = input_processing("Введите диапазон зарплат через дефис: ")
        salary_range = salary_range.replace(' ', '').strip('-')

    return salary_range