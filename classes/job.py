import json


class Vacancy:
    __slots__ = ('name', 'company', 'url', 'description', 'salary')

    def __init__(self, name, company, url, description, salary, *args):
        self.name = name
        self.company = company
        self.url = url
        if type(description) == str:
            self.description = description[:200]
        else:
            self.description = description
        self.salary = salary
        super().__init__(*args)


    def __repr__(self):
        return f'Наименование вакансии: {self.name}\nРаботодатель: {self.company}\nСсылка на вакансию:' \
               f' {self.url}\nОписание вакансии: {self.description}\nЗарплата:' \
               f' {self.salary}\n'


    def __gt__(self, other) -> bool:
        return self.salary > other.salary


    def __lt__(self, other) -> bool:
        if other.salary is None:
            return False
        if self.salary is None:
            return True
        return self.salary < other.salary


class CountMixin:

    def __init__(self, file_name=None):
        self.file_name = file_name

    def get_count_of_vacancy(self):
        """
        Вернуть количество вакансий от текущего сервиса.
        Получать количество необходимо динамически из файла.
        """
        with open(self.file_name, "r", encoding="UTF-8") as file:
            data = json.load(file)
            counter = 0
            for i in data:
                counter += 1
        return counter


