import json


class Vacancy:
    __slots__ = ('url', 'name', 'company', 'salary', 'description')

    def __init__(self, url, name, company, salary, description):
        self.url = url
        self.name = name
        self.company = company
        self.salary = salary
        self.description = description


    def __repr__(self):
        return f'Наименование вакансии: {self.name}\nРаботодатель: {self.company}\nСсылка на вакансию:' \
               f' {self.url}\nОписание вакансии: {self.description}\nЗарплата:' \
               f' {self.salary}\n'


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
