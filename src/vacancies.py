from src.api import Currency
from src.settings import TAGS_FOR_REMOVE


class Vacancy:
    """
    Класс описывающий вакансию
    """
    data_frame: dict

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.salary = kwargs.get('salary')
        self.area = kwargs.get('area')
        self.url = kwargs.get('url')
        self.employment = kwargs.get('employment')
        self.experience = kwargs.get('experience')
        self.schedule = kwargs.get('schedule')
        self.description = kwargs.get('description')

    def __str__(self):
        return f'{self.name}, {self.salary}, {self.area}, {self.url}'

    def __repr__(self):
        data = {x: getattr(self, x) for x in self.__dict__ if not x.startswith('__')}

        return f'{self.__class__.__name__}({data})'

    def __lt__(self, other):
        """
        Сравним две вакансии по средней от вилки зарплат
        :param other:
        :return:
        """
        left_obj = self.salary[:]
        right_obj = other.salary[:]
        for salary in [left_obj, right_obj]:
            if salary[1] == 0:
                salary[1] = salary[0]
        return sum(left_obj) / 2 < sum(right_obj) / 2

    @property
    def search_str(self):
        """
        Строка для орагнизации поиска по дополнительным ключевым словам
        :return:
        """
        return f'{self.area} {self.description}'.lower()

    @classmethod
    def get_salary(cls, data) -> list:
        """
        Переведем зарплату в валюте по текущему курсу
        :param data:
        :return:
        """
        if data is not None:
            if data['currency'] is not None and data['currency'] != 'RUR':
                rate = Currency.get_rate(data['currency'])
            else:
                rate = 1

            return [
                int(data['from'] / rate) if data['from'] is not None else 0,
                int(data['to'] / rate) if data['to'] is not None else 0
            ]
        else:
            return [0, 0]

    @classmethod
    def parse_from_hh(cls, json_text: [dict]) -> list:
        """
        Создание списка вакансий с необходимыми полями из JSON файла
        :param json_text:
        :return:
        """
        list_ = []
        for x in json_text:
            new_vacancy = cls(
                name=x['name'],
                salary=cls.get_salary(x['salary']),
                # "from": 249999, "to": 250000, "currency": "KZT"
                area=x['area']['name'],
                url=x['alternate_url'],
                employment=x['employment']['name'],
                experience=x['experience']['name'],
                schedule=x['schedule']['name'],
                description=(x['snippet']['requirement'] if x['snippet']['requirement'] is not None else '') +
                            (x['snippet']['responsibility'] if x['snippet']['responsibility'] is not None else '')
            )
            for element in TAGS_FOR_REMOVE:
                new_vacancy.description = new_vacancy.description.replace(element, '')
            list_.append(new_vacancy)
        return list_

    @staticmethod
    def vacancy_to_json(obj) -> dict:
        """
        Правило для сериализации объектов класса в JSON
        :param obj:
        :return:
        """
        dict_ = {}
        for x in obj.__dict__:
            if not x.startswith('__'):
                dict_[x] = getattr(obj, x)

        return dict_

    @classmethod
    def clear_data_frame(cls):
        cls.data_frame = {
           'name': [],
           'salary_min': [],
           'salary_max': [],
           'area': [],
           'url': [],
           'description': [],
           'employment': [],
           'experience': [],
           'schedule': [],
        }

    @classmethod
    def vacancy_to_data_frame(cls, obj):
        cls.data_frame['name'].append(obj.name)
        cls.data_frame['salary_min'].append(obj.salary[0])
        cls.data_frame['salary_max'].append(obj.salary[1])
        cls.data_frame['area'].append(obj.area)
        cls.data_frame['url'].append(obj.url)
        cls.data_frame['description'].append(obj.description)
        cls.data_frame['employment'].append(obj.employment)
        cls.data_frame['experience'].append(obj.experience)
        cls.data_frame['schedule'].append(obj.schedule)

