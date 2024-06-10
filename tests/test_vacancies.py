from src.vacancies import Vacancy


def test_vacancy_str(test_00_vacancy):
    assert (str(test_00_vacancy) == 'Back-End Engineer - Python, Django, AWS, Integrations, [89051, 445257], '
                                    'Великобритания, https://hh.ru/vacancy/101501668')


def test_vacancy_repr(test_00_vacancy):
    assert (repr(test_00_vacancy) == "Vacancy({'name': 'Back-End Engineer - Python, Django, AWS, Integrations', "
                                     "'salary': [89051, 445257], 'area': 'Великобритания', 'url': 'https://hh.ru/"
                                     "vacancy/101501668', 'employment': 'Частичная занятость', 'experience': 'От "
                                     "3 до 6 лет', 'schedule': 'Полный день', 'description': '2+ years of working "
                                     "experience in backend development...'})")


def test_vacancy_lt(test_00_vacancy, test_01_vacancy):
    assert test_00_vacancy > test_01_vacancy
    test_00_vacancy.salary = [150000, 0]
    assert test_00_vacancy < test_01_vacancy


def test_get_salary(test_currency):
    test_data = {"from": 350000, "to": 450000, "currency": "RUR", "gross": False}
    assert Vacancy.get_salary(test_data) == [350000, 450000]
    test_data = {"from": None, "to": 450000, "currency": "RUR", "gross": False}
    assert Vacancy.get_salary(test_data) == [0, 450000]
    test_data = {"from": 350000, "to": None, "currency": "RUR", "gross": False}
    assert Vacancy.get_salary(test_data) == [350000, 0]
    test_data = {"from": 935, "to": 945, "currency": "USD", "gross": False}
    assert Vacancy.get_salary(test_data) == [93500, 94500]
    test_data = None
    assert Vacancy.get_salary(test_data) == [0, 0]


def test_parse_from_hh():
    text = [{"id": "93353083", "premium": False, "name": "Тестировщик комфорта квартир", "department": None,
            "has_test": False,
            "response_letter_required": False,
            "area": {"id": "26", "name": "Воронеж", "url": "https://api.hh.ru/areas/26"},
            "salary": {"from": 350000, "to": 450000, "currency": "RUR", "gross": False},
            "type": {"id": "open", "name": "Открытая"},
            "address": None, "response_url": None, "sort_point_distance": None,
            "published_at": "2024-02-16T14:58:28+0300",
            "created_at": "2024-02-16T14:58:28+0300", "archived": False,
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=93353083",
            "branding": {"type": "CONSTRUCTOR", "tariff": "BASIC"}, "show_logo_in_search": True,
            "insider_interview": None,
            "url": "https://api.hh.ru/vacancies/93353083?host=hh.ru", "alternate_url": "https://hh.ru/vacancy/93353083",
            "relations": [], "employer": {"id": "3499705", "name": "Специализированный застройщик BM GROUP",
                                          "url": "https://api.hh.ru/employers/3499705",
                                          "alternate_url": "https://hh.ru/employer/3499705",
                                          "logo_urls": {
                                              "original": "https://hhcdn.ru/employer-logo-original/1214854.png",
                                              "240": "https://hhcdn.ru/employer-logo/6479866.png",
                                              "90": "https://hhcdn.ru/employer-logo/6479865.png"},
                                          "vacancies_url": "https://api.hh.ru/vacancies?employer_id=3499705",
                                          "accredited_it_employer": False, "trusted": True},
            "snippet": {"requirement": "Занимать активную жизненную позицию",
                        "responsibility": "Оценивать вид из окна"},
            "contacts": None, "schedule": {"id": "flexible", "name": "Гибкий график"}, "working_days": [],
            "working_time_intervals": [], "working_time_modes": [], "accept_temporary": False,
            "professional_roles": [{"id": "107", "name": "Руководитель проектов"}], "accept_incomplete_resumes": False,
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "employment": {"id": "full", "name": "Полная занятость"},
            "adv_response_url": None, "is_adv_vacancy": False, "adv_context": None}]

    test_vacancy = [Vacancy(**{'name': 'Тестировщик комфорта квартир', 'salary': [350000, 450000], 'area': 'Воронеж',
                               'url': 'https://hh.ru/vacancy/93353083', 'employment': 'Полная занятость',
                               'experience': 'Нет опыта', 'schedule': 'Гибкий график',
                               'description': 'Занимать активную жизненную позициюОценивать вид из окна'})]


    assert repr(Vacancy.parse_from_hh(text)[0]) == repr(test_vacancy[0])

def test_vacancy_to_json(test_00_vacancy) -> dict:
    test_dict =  {
       'area': 'Великобритания',
       'description': '2+ years of working experience in backend development...',
       'employment': 'Частичная занятость',
       'experience': 'От 3 до 6 лет',
       'name': 'Back-End Engineer - Python, Django, AWS, Integrations',
       'salary': [
           89051,
           445257,
       ],
       'schedule': 'Полный день',
       'url': 'https://hh.ru/vacancy/101501668',
   }
    assert Vacancy.vacancy_to_json(test_00_vacancy) == test_dict
