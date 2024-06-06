from pathlib import Path

PATH = Path(__file__).parent.parent
PATH_TO_JSON = PATH.joinpath('data', 'vacancies.json')

# https://api.hh.ru/openapi/redoc#tag/Poisk-vakansij/operation/get-vacancies
VACANCY_SEARCH_FIELDS = {'1': {'name'}, '2': {'name', 'description'}}