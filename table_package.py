import csv
import pickle
import pandas
import numpy

class Package: #основной класс для csv/pickle load/save
    def __init__(self, file):#инициализация файлика(можно сделать и input'ом)
        self.file = file

    def load_table_csv(self): #загрузка во внутреннее представление модуля
        directory = self.file

    def save_table_csv(self): #сохранение из внутреннего представления модуля
        directory = self.file
        election = pandas.read_csv(directory)
        # print(election)
        election_modified = election.set_index('state')
        print(election_modified)


        '''
        directory = self.file
        representation_dictionary = {} #наше представление(ключи - заголовки, значения - списки)
        with open(directory, newline='') as File:
            reader = csv.reader(File)
            csv_headings = next(reader)
            print(len(csv_headings))
            csv_values = []
            for row in reader:
                col = list(row[i] for i in range(len(csv_headings)))
                csv_values.append(col)
            for keys in csv_headings:
                representation_dictionary.update({keys:csv_values})
            print(representation_dictionary)
        '''
    def load_table_pickle(self):
        directory = self.file

    def save_table_pickle(self):
        directory = self.file

    def save_table_txt(self):
        directory = self.file


class Operations(Package): # Модули с базовыми операциями над таблицами:
    # тут функции будут уже из родительского класса брать load,save и че-то делать...
    def __init__(self, file, column, types):
        super().__init__(file) # унаследовали файлик из родительского класса
        self.column = column # проинициализировали новые свойства column и types
        self.types = types
        # Тут в перспективне будут инициализоровать подаваемые аргументы в функции ниже#
        # ниже во всех функциях доработаю подаваемые аргументы(types, column, values, copy_table, by_number и тд
        # также будем в функции будем подавать функции из главного класса - self.load_table_csv() и тд.
    def get_rows_by_number(self):
        '''
        get_rows_by_number(start, [stop], copy_table=False) – получение таблицы из одной строки или из строк из интервала по номеру строки.
        Функция либо копирует исходные данные, либо создает новое представление таблицы, работающее с исходным набором данных (copy_table=False),
        таким образом изменения, внесенные через это представления будут наблюдаться и в исходной таблице.
        '''
        pass

    def get_rows_by_index(self):
        '''
        get_rows_by_index(val1, … , copy_table=False) – получение новой таблицы из одной строки или из строк со значениями в первом столбце,
        совпадающими с переданными аргументами val1, … , valN. Функция либо копирует исходные данные, либо создает новое представление таблицы,
        работающее с исходным набором данных (copy_table=False), таким образом изменения, внесенные через это представления будут наблюдаться и в исходной таблице.
        '''
        pass

    def get_column_types(self):
        '''
        get_column_types(by_number=True) – получение словаря вида столбец:тип_значений. Тип значения: int, float, bool, str (по умолчанию для всех столбцов).
        Параметр by_number определяет вид значения столбец – целочисленный индекс столбца или его строковое представление.
        '''
        pass
    def set_column_types(self):
        '''
        set_column_types(types_dict, by_number=True) – задание словаря вида столбец:тип_значений.
        Тип значения: int, float, bool, str (по умолчанию для всех столбцов).
        Параметр by_number определяет вид значения столбец – целочисленный индекс столбца или его строковое представление.
        '''
        pass

    def get_values(self):
        '''
        get_values(column=0) – получение списка значений (типизированных согласно типу столбца)
        таблицы из столбца либо по номеру столбца (целое число, значение по умолчанию 0, либо по имени столбца)
        '''
        pass

    def get_value(self):
        '''
        get_value(column=0) – аналог get_values(column=0) для представления таблицы с одной строкой,
        возвращает не список, а одно значение (типизированное согласно типу столбца).
        '''
        pass

    def set_values(self):
        '''
        set_values(values, column=0) – задание списка значений values для столбца таблицы (типизированных согласно типу столбца)
        либо по номеру столбца (целое число, значение по умолчанию 0, либо по имени столбца).
        '''
        pass

    def set_value(self):
        '''
        set_value(column=0) – аналог set_values(value, column=0) для представления таблицы с одной строкой,
        устанавливает не список значений, а одно значение (типизированное согласно типу столбца).
        '''
        pass

    def print_table(self):
        '''
        print_table() – вывод таблицы на печать.
        '''
        pass

    ''' Наше задание:
    7)	По аналогии с п. 6 реализовать функции eq (==), gr (>), ls (<), ge (>=), le (<=), ne (==), 
    которые возвращают список булевских значений длинной в количество строк сравниваемых столбцов. 
    Реализовать функцию filter_rows (bool_list, copy_table=False) – получение новой таблицы из строк для которых в bool_list (длинной в количество строк в таблице)
    находится значение True.
    '''

if __name__ == "__main__":
    #our_file = Package(r'C:\Users\79268\table_package\123123.csv.txt') #даём главному классу на вход наш файлик
    #our_file.load_table_csv() #наш файлик пройдёт через функцию и че-то сделает в перспективе(проверка главного класса)
    #functions = Operations(r'C:\Users\79268\table_package\123123.csv.txt', column= , types= ) #тут уже работаем с нашими настройками и функциями, как в задании и делаем что-то соответственно
    ourfile = Package(r'C:\Users\79268\Dev\csvs\governors_county.csv')
    ourfile.save_table_csv()
