
from classes.engine import HH

user_choice = "Python"
h = HH()
response = h.get_request(user_choice)
into_file_hh = h.save_to_json('new_vacancies_list.json', response)
