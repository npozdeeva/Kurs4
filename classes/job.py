import json


class Vacancy:
    __slots__ = ('url', 'name_vac', 'company', 'city', 'salary', 'description', 'responsibility')

    def __init__(self, data: dict):
        self.url = data['url']
        self.name_vac = data['name_vac']
        self.company = data['company']
        self.city = data['city']
        self.salary = int(data['salary']) # заменил на 'salary_from': path_vacancy.get('payment_from', 0) - д.б. ноль
        self.description = data['description']
        self.responsibility = data['responsibility']


    def __gt__(self, other):
        return self.salary > other.salary


    def __str__(self):
        pass


class CountMixin:

    def __init__(self, file_name=None):
        self.file_name = file_name

    @property
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
