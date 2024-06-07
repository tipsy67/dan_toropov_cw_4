class Vacancy:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.salary = kwargs.get('salary')
        self.area = kwargs.get('area')
        self.url = kwargs.get('url')
        self.employment = kwargs.get('employment')
        self.experience = kwargs.get('experience')
        self.schedule = kwargs.get('schedule')
        self.description = kwargs.get('description')

    @classmethod
    def parse_from_hh(cls, json_text: dict) -> list:
        list_ = []
        for x in json_text:
            list_.append(
                cls(
                    name=x['name'],
                    salary=[x['salary']['from'], x['salary']['to']] if x['salary'] is not None else 0,
                    # "from": 249999, "to": 250000, "currency": "KZT"
                    area=x['area']['name'],
                    url=x['alternate_url'],
                    employment=x['employment']['name'],
                    experience=x['experience']['name'],
                    schedule=x['schedule']['name'],
                    description=x['snippet']['requirement'] if x['snippet']['requirement'] is not None else ''
                            + x['snippet']['responsibility'] if x['snippet']['requirement'] is not None else ''
                )
            )
        return list_

    def vacancy_to_json(self) -> dict:
        dict_ = {}
        for x in self.__dict__:
            if not x.startswith('__'):
                dict_[x] = getattr(self, x)

        return dict_






