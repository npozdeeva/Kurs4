import json


class Connector:
    """
    Класс коннектор к файлу, обязательно файл должен быть в json формате
    не забывать проверять целостность данных, что файл с данными не подвергся
    внешнего деградации
    """
    __data_file = None


    def __init__(self, filename):
        self.data_file = filename


    @property
    def data_file(self):
        return self.__data_file

    @data_file.setter
    def data_file(self, value):
        # тут должен быть код для установки файла
        self.__data_file = value
        self.__connect()

    def __connect(self):
        """
        Проверка на существование файла с данными и
        создание его при необходимости
        Также проверить на деградацию и возбудить исключение
        если файл потерял актуальность в структуре данных
        """
        with open(self.__data_file, 'a+', encoding='utf8') as f:
            f.seek(0)
            first_line = f.readline()
            if first_line:
                try:
                    f.seek(0)
                    data = json.load(f)
                    assert type(data) == list
                    for item in data:
                        assert type(item["name"]) == str
                        assert type(item["company_name"]) == str
                        assert type(item["url"]) == str
                        assert type(item["remote_work"]) == str
                        assert type(item["salary"]) == int
                except:
                    raise Exception()
            else:
                json.dump([], f)

    def insert(self, data):
        """
        Запись данных в файл с сохранением структуры и исходных данных
        """
        # self.__connect()
        # with open('df.json', encoding='utf-8') as f:
        #     data = json.load(f)
        #     with open('df.json', encoding='utf-8') as outfile:
        #         json.dump(data, outfile, ensure_ascii=False)
        with open(self.__data_file, 'r', encoding='utf-8') as f:
            file_data = json.load(f)
        if type(data) == dict:
            file_data.append(data)
        elif type(data) == list:
            file_data.extend(data)
        with open(self.__data_file, 'w', encoding='utf8') as f:
            json.dump(file_data, f, ensure_ascii=False, indent=4)

    def select(self, query):
        """
        Выбор данных из файла с применением фильтрации
        query содержит словарь, в котором ключ это поле для
        фильтрации, а значение это искомое значение, например:
        {'price': 1000}, должно отфильтровать данные по полю price
        и вернуть все строки, в которых цена 1000
        """
        search_key, search_value = query.items()[0]

        with open(self.__data_file, 'r', encoding='utf8') as f:
            file_data = json.load(f)

        result = []
        for vacancy in file_data:
            if vacancy[search_key] == search_value:
                result.append(vacancy)
        return result


    def delete(self, query):
        """
        Удаление записей из файла, которые соответствуют запрос,
        как в методе select. Если в query передан пустой словарь, то
        функция удаления не сработает
        """
        pass




if __name__ == '__main__':
    df = Connector('df.json')

    data_for_file = {'id': 1, 'title': 'tet'}

    df.insert(data_for_file)
    data_from_file = df.select(dict())
    assert data_from_file == [data_for_file]

    df.delete({'id':1})
    data_from_file = df.select(dict())
    assert data_from_file == []