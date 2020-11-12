import csv
import pickle
import pandas

class Package: #основной класс для csv/pickle load/save
    def __init__(self, file):#инициализация файлика(можно сделать и input'ом)
        self.file = file

    def load_table_csv(self): #загрузка во внутреннее представление модуля
        output_directory = r'C:\Users\79268\Dev\csvs\output.csv'
        self.save_table_csv()
        print(self.columns)
        new_frame = pandas.DataFrame(self.frame)
        new_frame.to_csv(output_directory)


    def save_table_csv(self): #сохранение из внутреннего представления модуля
        directory = self.file
        self.frame = pandas.read_csv(directory)
        # print(election)
        frame_modified = self.frame.set_index('state')
        print(self.frame)
        self.columns = self.frame.columns.tolist()


    def load_table_pickle(self):
        directory = self.file

    def save_table_pickle(self):
        directory = self.file

    def save_table_txt(self):
        directory = self.file


class Operations(Package): # Модули с базовыми операциями над таблицами:
    # тут функции будут уже из родительского класса брать load,save и че-то делать...
    def __init__(self, file):
        super().__init__(file) # унаследовали файлик из родительского класса

        # Тут в перспективне будут инициализоровать подаваемые аргументы в функции ниже#
        # ниже во всех функциях доработаю подаваемые аргументы(types, column, values, copy_table, by_number и тд
        # также будем в функции будем подавать функции из главного класса - self.load_table_csv() и тд.
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
    #functions = Operations(r'C:\Users\79268\table_package\123123.csv.txt') #тут уже работаем с нашими настройками и функциями, как в задании и делаем что-то соответственно
    #ourfile = Package(r'C:\Users\79268\Dev\csvs\governors_county.csv')
    #ourfile.save_table_csv()
    #ourfile.load_table_csv()
    operations = Operations(r'C:\Users\79268\Dev\csvs\governors_county.csv')
    #operations.get_rows_by_number(0,10,copy_table=False)
    #operations.get_rows_by_index(copy_table=True, val='state')
    #operations.get_column_types()
    #operations.set_column_types('str')
    operations.get_values(0) #get_values(0-4(только одно число без кавычек)) или get_values('state'-'percent')
    operations.get_values('percent')