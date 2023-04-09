from abc import ABC, abstractmethod
import requests
from classes.connector import Connector


class Engine(ABC):
    @abstractmethod
    def get_request(self, data):
        pass

    @staticmethod
    def get_connector(file_name):
        """ Возвращает экземпляр класса Connector """
        connector = Connector(file_name)
        return connector


    def save_to_json(self, file_path, vacancies_list):
        connector = self.get_connector(file_path)
        connector.insert(vacancies_list)

class HH(Engine):

    @staticmethod
    def _get_salary(salary_info: dict):
        if salary_info:
            if salary_info.get('to'):
                return salary_info['to']
            if salary_info.get('from'):
                return salary_info['from']
        return 0

    def get_request(self, data):
        vacancies_list_hh = []
        for page in range(5):
            request_hh = requests.get(f"https://api.hh.ru/vacancies?text={data}", params={'per_page': '100', 'page': page}).json()
            for vacancy in request_hh['items']:
                vacancies_list_hh.append({
                    "name": vacancy['name'],
                    "company": vacancy['employer']['name'],
                    "url": vacancy['alternate_url'],
                    "description": vacancy['snippet']['requirement'],
                    "salary": self._get_salary(vacancy.get('salary', {})),
                })
       # print(len(vacancies_list_hh))
        return vacancies_list_hh


class SuperJob(Engine):
    def __init__(self, api_key):
        self.api_key = api_key


    def get_request(self):
        self.name = None
