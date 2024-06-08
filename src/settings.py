from pathlib import Path

PATH = Path(__file__).parent.parent
PATH_TO_JSON = PATH.joinpath('data', 'vacancies.json')

URL_CURRENCY = 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/rub.json'

# https://api.hh.ru/openapi/redoc#tag/Poisk-vakansij/operation/get-vacancies
VACANCY_SEARCH_FIELDS = {'1': {'name'}, '2': {'name', 'description'}}
VACANCY_SEARCH_PER_PAGE = 100 #100
VACANCY_SEARCH_PAGE = 20 # 20

TAGS_FOR_REMOVE = {'<highlighttext>', '</highlighttext>'}

