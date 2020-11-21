import csv
import pickle
import pandas
from tabulate import tabulate
import numpy as np
pandas.options.display.expand_frame_repr = False








class Package: #основной класс для csv/pickle load/save
    def __init__(self, file):#инициализация файлика(можно сделать и input'ом)
        self.file = file

    def load_table_csv(self): #загрузка во внутреннее представление модуля
        output_directory = r'C:\Users\79268\Dev\csvs\output.csv'
        directory = self.file
        frame = pandas.read_csv(directory)
        frame.to_csv(output_directory)

    def save_table_csv(self): #сохранение из внутреннего представления модуля
        directory = self.file
        frame = pandas.read_csv(directory)
        print(frame)

    def load_table_pickle(self):
        directory = self.file

    def save_table_pickle(self):
        directory = self.file

    def save_table_txt(self):
        directory = self.file


class Operations(Package): # Модули с базовыми операциями над таблицами:
    def __init__(self, file):
        super().__init__(file) # унаследовали файлик из родительского класса

    def get_rows_by_number(self, start, stop, copy_table):
        output_directory = r'C:\Users\79268\Dev\csvs\output.csv'
        directory = self.file
        if copy_table == True:
            frame = pandas.read_csv(directory)
            print(frame[start:stop + 1])

        elif copy_table == False:
            frame = pandas.read_csv(directory)
            frame[start:stop + 1].to_csv(output_directory, index=False)
            print(frame[start:stop + 1])
        '''
        get_rows_by_number(start, [stop], copy_table=False) – получение таблицы из одной строки или из строк из интервала по номеру строки.
        Функция либо копирует исходные данные, либо создает новое представление таблицы, работающее с исходным набором данных (copy_table=False),
        таким образом изменения, внесенные через это представления будут наблюдаться и в исходной таблице.
        '''


    def get_rows_by_index(self, copy_table, **val):
        output_directory = r'C:\Users\79268\Dev\csvs\output.csv'
        directory = self.file
        key = val.values()
        if copy_table == True:
            frame = pandas.read_csv(directory)
            print(pandas.concat([frame[key]], ignore_index=True))
        elif copy_table == False:
            frame = pandas.read_csv(directory)
            frame[key].to_csv(output_directory, index=False)

        '''
        get_rows_by_index(val1, … , copy_table=False) – получение новой таблицы из одной строки или из строк со значениями в первом столбце,
        совпадающими с переданными аргументами val1, … , valN. Функция либо копирует исходные данные, либо создает новое представление таблицы,
        работающее с исходным набором данных (copy_table=False), таким образом изменения, внесенные через это представления будут наблюдаться и в исходной таблице.
        '''


    def get_column_types(self):
        directory = self.file
        frame = pandas.read_csv(directory)
        print(frame.info(null_counts=False, memory_usage=False)) #Object столбцы используются для хранения строковых данных
        #by_number уже включен(built-in)
        '''
        get_column_types(by_number=True) – получение словаря вида столбец:тип_значений. Тип значения: int, float, bool, str (по умолчанию для всех столбцов).
        Параметр by_number определяет вид значения столбец – целочисленный индекс столбца или его строковое представление.
        '''

    def set_column_types(self, types_dict):
        directory = self.file
        frame = pandas.read_csv(directory)
        if types_dict == 'int':
            frame_show = frame.select_dtypes(include=['int64'])
            #print(frame_show)
            print(frame_show.info(null_counts=False, memory_usage=False))
        elif types_dict == 'float':
            frame_show = frame.select_dtypes(include=['int64'])
            #print(frame_show)
            print(frame_show.info(null_counts=False, memory_usage=False))
        elif types_dict == 'bool':
            frame_show = frame.select_dtypes(include=['bool'])
            #print(frame_show)
            print(frame_show.info(null_counts=False, memory_usage=False))
        elif types_dict == 'str':
            frame_show = frame.select_dtypes(include=['object'])
            #print(frame_show)
            print(frame_show.info(null_counts=False, memory_usage=False))
        else:
            print('Введите тип значений')
        # by_number уже включен(built-in)
        '''
        set_column_types(types_dict, by_number=True) – задание словаря вида столбец:тип_значений.
        Тип значения: int, float, bool, str (по умолчанию для всех столбцов).
        Параметр by_number определяет вид значения столбец – целочисленный индекс столбца или его строковое представление.
        '''

    def get_values(self, column):
        directory = self.file
        frame = pandas.read_csv(directory)
        if type(column) == str:
            print(frame[column])
        elif type(column) == int:
            column_index = frame.columns[column]
            print(frame[column_index])
        '''
        get_values(column=0) – получение списка значений (типизированных согласно типу столбца)
        таблицы из столбца либо по номеру столбца (целое число, значение по умолчанию 0, либо по имени столбца)
        '''

    def get_value(self, column):
        directory = self.file
        frame = pandas.read_csv(directory)
        if type(column) == str:
            print(frame[column])
        elif type(column) == int:
            column_index = frame.columns[column]
            print(frame[column_index])
        '''
        get_value(column=0) – аналог get_values(column=0) для представления таблицы с одной строкой,
        возвращает не список, а одно значение (типизированное согласно типу столбца).
        '''

    def set_values(self, values, column):
        directory = self.file
        frame = pandas.read_csv(directory)
        if type(column) == str:
            frame.loc[:, column] = values #Set value for an entire column из документации
            print(frame)
        elif type(column) == int:
            column_index = frame.columns[column]
            frame.loc[:, column_index] = values
            print(frame)
        '''
        set_values(values, column=0) – задание списка значений values для столбца таблицы (типизированных согласно типу столбца)
        либо по номеру столбца (целое число, значение по умолчанию 0, либо по имени столбца).
        '''

    def set_value(self, values, column):
        directory = self.file
        frame = pandas.read_csv(directory)
        if type(column) == str:
            frame.loc[:, column] = values
            print(frame)
        elif type(column) == int:
            column_index = frame.columns[column]
            frame.loc[:, column_index] = values
            print(frame)
        '''
        set_value(column=0) – аналог set_values(value, column=0) для представления таблицы с одной строкой,
        устанавливает не список значений, а одно значение (типизированное согласно типу столбца).
        '''

    def print_table(self):
        directory = self.file
        frame = pandas.read_csv(directory)
        pandas.options.display.max_rows = len(frame)

        print(frame)

    def equall(self, **columns):
        directory = self.file
        frame = pandas.read_csv(directory)
        pandas.options.display.max_rows = len(frame)
        column = list(columns.values())
        if type(column[0]) == str:
            equality = frame[column[0]] == frame[column[1]]
            frame['equally'] = equality
            print(frame['equally'])
        elif type(column[0]) == int:
            column_index_1 = frame.columns[column[0]]
            column_index_2 = frame.columns[column[1]]
            equality = frame[column_index_1] == frame[column_index_2]
            frame['equally'] = equality
            print(frame['equally'])

    def greater(self, **columns):
        directory = self.file
        frame = pandas.read_csv(directory)
        pandas.options.display.max_rows = len(frame)
        column = list(columns.values())
        try:
            if type(column[0]) == str:
                greater_than = frame[column[0]] > frame[column[1]]
                frame['greater'] = greater_than
                print(frame['greater'])
            elif type(column[0]) == int:
                column_index_1 = frame.columns[column[0]]
                column_index_2 = frame.columns[column[1]]
                greater_than = frame[column_index_1] > frame[column_index_2]
                frame['greater'] = greater_than
                print(frame['greater'])
        except TypeError:
            print('Сравниваемые столбцы не должны быть строками и числами')

    def less(self, **columns):
        directory = self.file
        frame = pandas.read_csv(directory)
        pandas.options.display.max_rows = len(frame)
        column = list(columns.values())
        try:
            if type(column[0]) == str:
                less_than = frame[column[0]] < frame[column[1]]
                frame['less'] = less_than
                print(frame['less'])

            elif type(column[0]) == int:
                column_index_1 = frame.columns[column[0]]
                column_index_2 = frame.columns[column[1]]
                less_than = frame[column_index_1] < frame[column_index_2]
                frame['less'] = less_than
                print(frame['less'])

        except TypeError:
            print('Сравниваемые столбцы не должны быть строками и числами')

    def greater_or_equally(self, **columns):
        directory = self.file
        frame = pandas.read_csv(directory)
        pandas.options.display.max_rows = len(frame)
        column = list(columns.values())
        try:
            if type(column[0]) == str:
                ge = frame[column[0]] >= frame[column[1]]
                frame['greater_or_equally'] = ge
                print(frame['greater_or_equally'])
            elif type(column[0]) == int:
                column_index_1 = frame.columns[column[0]]
                column_index_2 = frame.columns[column[1]]
                ge = frame[column_index_1] >= frame[column_index_2]
                frame['greater_or_equally'] = ge
                print(frame['greater_or_equally'])
        except TypeError:
            print('Сравниваемые столбцы не должны быть строками и числами')

    def less_or_equall(self, **columns):
        directory = self.file
        frame = pandas.read_csv(directory)
        pandas.options.display.max_rows = len(frame)
        column = list(columns.values())
        try:
            if type(column[0]) == str:
                le = frame[column[0]] <= frame[column[1]]
                frame['less_or_equally'] = le
                print(frame['less_or_equally'])
            elif type(column[0]) == int:
                column_index_1 = frame.columns[column[0]]
                column_index_2 = frame.columns[column[1]]
                le = frame[column_index_1] <= frame[column_index_2]
                frame['less_or_equally'] = le
                print(frame['less_or_equally'])

        except TypeError:
            print('Сравниваемые столбцы не должны быть строками и числами')

    def not_equall(self, **columns):
        directory = self.file
        frame = pandas.read_csv(directory)
        pandas.options.display.max_rows = len(frame)
        column = list(columns.values())
        if type(column[0]) == str:
            ne = frame[column[0]] != frame[column[1]]
            frame['not_equall'] = ne
            print(frame['not_equall'])
        elif type(column[0]) == int:
            column_index_1 = frame.columns[column[0]]
            column_index_2 = frame.columns[column[1]]
            ne = frame[column_index_1] != frame[column_index_2]
            frame['not_equall'] = ne
            print(frame['not_equall'])

    def filter_rows(self, bool_list, copy_table):
        directory = self.file
        frame = pandas.read_csv(directory)
        if copy_table == True:
            bool_list = frame.loc[frame[bool_list] == True]
            print(bool_list)
        elif copy_table == False:
            bool_list = frame.loc[frame[bool_list] == True]
            bool_list.to_csv(r'C:\Users\79268\Dev\csvs\output1.csv')

    '''Пункт 6:
    6)	Добавить набор функций add, sub, mul, div, которые обеспечат выполнение арифметических операций для столбцов типа
     int, float, bool. Продумать сигнатуру функций и изменения в другие функции, которые позволят удобно выполнять арифметические операции 
     со столбцами и присваивать результаты выч. Реализовать реагирование на некорректные значения с помощью генерации исключительных ситуаций.
    '''
    ''' Наше задание:
    7)	По аналогии с п. 6 реализовать функции eq (==), gr (>), ls (<), ge (>=), le (<=), ne (!=), 
    которые возвращают список булевских значений длинной в количество строк сравниваемых столбцов. 
    Реализовать функцию filter_rows (bool_list, copy_table=False) – получение новой таблицы из строк для которых в bool_list (длинной в количество строк в таблице)
    находится значение True.
    '''

if __name__ == "__main__":
    #our_file = Package(r'C:\Users\79268\Dev\csvs\governors_county.csv') #даём главному классу на вход наш файлик
    #our_file.load_table_csv() #наш файлик пройдёт через функцию и че-то сделает в перспективе(проверка главного класса)
    #functions = Operations(r'C:\Users\79268\table_package\123123.csv.txt') #тут уже работаем с нашими настройками и функциями, как в задании и делаем что-то соответственно
    #ourfile = Package(r'C:\Users\79268\Dev\csvs\governors_county.csv')
    #ourfile.save_table_csv()
    #ourfile.load_table_csv()
    #operations = Operations(r'C:\Users\79268\Dev\csvs\bestsellers_with_categories.csv')
    #operations = Operations(r'C:\Users\79268\Dev\csvs\bestsellers_with_categories.csv')
    operations = Operations(r'C:\Users\79268\Dev\csvs\governors_county.csv')
    operations.get_rows_by_number(0,25,copy_table=True)
    #operations.get_rows_by_index(copy_table=True, val='total_votes')
    #operations.get_column_types()
    #operations.set_column_types('int')
    #operations.get_values(0) #get_values(0-4(только одно число без кавычек)) или get_values('state'-'percent')
    #operations.get_values('percent')
    #operations.set_values(values='123bc', column=0) #столбец = числу
    #operations.set_values(values='everything', column='state') #столбец = строке
    #operations.print_table()
    #operations.equall(columns1='Price', columns2='Year')
    #operations.equall(da='state', daa='state')
    #operations.greater(first=3, second=5)
    #operations.less(first=3, second=5)
    #operations.greater_or_equally(first='Year', second='Year')
    #operations.less_or_equall(first_column='Year', second='Reviews')
    #operations.not_equall(f='Author', s='Year')
    #operations.filter_rows(bool_list='less', copy_table=True)