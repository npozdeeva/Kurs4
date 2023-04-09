import json
from pprint import pprint
from classes.engine import HH
from classes.job import Vacancy

def formatting_file(file_name):
    # очищение содержимого файла
    with open(file_name, 'w'):
        pass

def user_interaction():
    formatting_file('vacancies_list.json')
    # Запрос ключевого слова.
    word_for_search = input('Введите ключевое слово для поиска: ')

    # парсинг 500 вакансий по заданному слову с сайта HeadHunter и сохранение их в файл vacancies_list.json
    h = HH()
    response = h.get_request(word_for_search)
    into_file_hh = h.save_to_json('vacancies_list.json', response)


    print('По вашему запросу собрано 500 вакансий с HeadHunter.\nВыберите '
          "следующее действие:\nВывести список всех вакансий: нажмите 1\nВывести 10 самых высокооплачиваемых вакансий: "
          "нажмите 2\nЗавершить программу: "
          "нажмите 3")

    # чтение общего списка вакансий спарсенных с двух сайтов
    with open('vacancies_list.json', 'r', encoding='utf8') as f:
        vacancies_from_json = json.load(f)
        vacancy_subjects = []
        for vac in vacancies_from_json:
            if vac["salary"] is not None:
                v = Vacancy(vac["name"], vac["company"], vac["url"], vac["description"], vac["salary"])
                vacancy_subjects.append(v)

    # выбор пользователем варианта из меню
    user_choice = input()
    while user_choice != '3':
        if user_choice == '1':
            # вывод списка всех вакансий
            for i in vacancy_subjects:
                print(i)
            user_choice = input('Введите следующую команду ')
        if user_choice == '2':
            # вывод 10 самых высокооплачиваемых вакансий
            sorted_vacancies = sorted(vacancy_subjects, reverse=True)[:10]
            for i in sorted_vacancies:
                print(i)
            user_choice = input('Введите следующую команду ')
        else:
            # обработка неверного значения, введенного пользователем
            print('Вы ввели неверное значение. Пожалуйста, попробуйте еще раз или нажмите 3 для завершения программы')
            user_choice = input()

if __name__ == "__main__":
    user_interaction()
    print('Программа завершена')