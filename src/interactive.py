from src.exceptions import ExitException


class UserQuery:
    """
    Класс для формирования пользовательского запроса:
        text_query      - текст запроса для поиска вакансии
        search_fields   - номер в справочнике поля/полей по которым будет производится запрос
        top_n           - количество вакансий для вывода в топ N
        filter_words    - дополнительные ключевые слова для фильтрации вакансий
        salary_range    - диапазон зарплат [min, max]
    """

    # будем запоминать сюда данные предыдущего запроса
    # для подсказок пользователю при вводе новых данных
    last_user_query = {}

    def __init__(self):
        print("Поиск вакансий. Для выхода из программы в любой момент введите: exit")

        self.__text_query = self.input_processing("Введите текст запроса для поиска вакансии:",
                                                  'text_query')
        self.__search_fields = self.input_search_fields()
        print("Теперь введите данные для детального поиска:")
        self.__top_n = self.input_top_n()
        self.__filter_words = self.input_filter_words()
        self.__salary_range = self.input_salary_range()
        self.__is_rewrite = self.input_is_rewrite()

    @property
    def text_query(self):
        return self.__text_query

    @property
    def search_fields(self):
        return self.__search_fields

    @property
    def top_n(self):
        return self.__top_n

    @property
    def filter_words(self):
        return self.__filter_words

    @property
    def salary_range(self):
        return self.__salary_range

    @property
    def is_rewrite(self):
        return self.__is_rewrite

    @classmethod
    def input_processing(cls, message, key) -> str:
        """
        при каждом вводе данных, выводим подсказку если есть
        и отслеживаем команду выхода из программы
        """
        print(message)
        prompt_last_query = cls.last_user_query.get(key)
        if prompt_last_query is not None and len(prompt_last_query) > 0:
            print(f"предыдущий запрос '{prompt_last_query}'")
        user_input = input()
        if user_input.strip(' ').lower() == "exit":
            raise ExitException
        return user_input

    @classmethod
    def remember_query(cls, user_query) -> None:
        """
        запомним данные пользовательского запроса
        :param user_query: UserQuery
        :return:
        """
        list_ = [x.replace('_UserQuery__', '') for x in user_query.__dict__ if not callable(x)]
        for x in list_:
            cls.last_user_query[x] = getattr(user_query, x)

    def input_search_fields(self) -> str:
        search_fields = None
        while search_fields not in ('1', '2'):
            search_fields = self.input_processing("Ввведите цифру:\n"
                                                  " 1 - для поиска по наименованию вакансии\n"
                                                  " 2 - для поиска по наименованию и описанию вакансии",
                                                  'search_fields')

        return search_fields

    def input_is_rewrite(self) -> str:
        is_rewrite = None
        while is_rewrite not in ('1', '2'):
            is_rewrite = self.input_processing("Ввведите цифру:\n"
                                               " 1 - для детального поиска вместе со старыми запросами\n"
                                               " 2 - для детального поиска только по текущему запросу",
                                               'is_rewrite')

        return is_rewrite

    def input_top_n(self) -> str:
        top_n = ''
        while not top_n.isdigit():
            top_n = self.input_processing("Введите количество вакансий для вывода в топ N: ",
                                          'top_n')

        return top_n

    def input_filter_words(self) -> list[str]:
        filter_words = self.input_processing("Введите через пробел"
                                             " ключевые слова для фильтрации вакансий: ",
                                             'filter_words').lower().split()
        filter_words = [x.replace(' ', '') for x in filter_words]

        return filter_words

    def input_salary_range(self) -> list[int]:
        salary_range = ['', '']
        while len(salary_range) != 2 or not salary_range[0].isdigit() or not salary_range[1].isdigit():
            salary_range = self.input_processing("Введите диапазон зарплат через дефис: ",
                                                 'salary_range')
            if len(salary_range) > 0:
                salary_range = salary_range.replace(' ', '').split('-')

        return salary_range
