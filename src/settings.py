from pathlib import Path

PATH = Path(__file__).parent.parent
PATH_TO_JSON = PATH.joinpath('data', 'vacancies.json')
PATH_TO_EXCEL = PATH.joinpath('data', 'report.xlsx')

URL_CURRENCY = 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/rub.json'

# Описание полей поиска вакансий для НН. Можно посмотреть по ссылке
# https://api.hh.ru/openapi/redoc#tag/Poisk-vakansij/operation/get-vacancies
VACANCY_SEARCH_FIELDS = {'1': {'name'}, '2': {'name', 'description'}}
VACANCY_SEARCH_PER_PAGE = 100  # 100
VACANCY_SEARCH_PAGE = 20  # 20

# Что удалять из полученного с удаленного ресурса JSON файла
TAGS_FOR_REMOVE = {'<highlighttext>', '</highlighttext>'}
