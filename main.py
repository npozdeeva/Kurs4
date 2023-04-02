import json
from pprint import pprint
from classes.engine import HH
from classes.job import Vacancy


def user_interaction():

    filter_words = input("Введите ключевое слово для фильтрации вакансий: ").split()
    h = HH()
    response = h.get_request(filter_words)
    into_file_hh = h.save_to_json('vacancies_list.json', response)

    with open('vacancies_list.json', 'r', encoding='utf8') as f:
        vacancies_from_json = json.load(f)
        vacancy_subjects = []
        for vac in vacancies_from_json:
            v = Vacancy(vac["url"], vac["name"], vac["company"], vac["salary"], vac["description"])
            vacancy_subjects.append(v)
        print("Список вакансий, найденных по ключевому слову:")
        for i in vacancy_subjects:
            pprint(i)

if __name__ == "__main__":
    user_interaction()
