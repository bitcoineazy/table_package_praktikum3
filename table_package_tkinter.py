from tkinter import *
import csv
import io
import pickle
import pandas
from tkinter import filedialog as fd
from tabulate import tabulate
from IPython.display import HTML, display
import tkinter.ttk as ttk
pandas.options.display.expand_frame_repr = False


class TablePackage(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.parent.title("Parser")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        self.initUI()

    def initUI(self):
        self.get_rows_by_number = Button(self, text='get_rows_by_number', command=self.get_rows_by_number, width=16)
        self.get_rows_by_number.grid(row=1, column=0)
        self.get_rows_by_index = Button(self, text='get_rows_by_index', command=self.get_rows_by_index , width=16)
        self.get_rows_by_index.grid(row=1, column=1)
        self.get_column_types = Button(self, text='get_column_types',command=self.get_column_types , width=16)
        self.get_column_types.grid(row=1, column=2)
        self.set_column_types = Button(self, text='set_column_types',command=self.set_column_types, width=16)
        self.set_column_types.grid(row=1, column=3)
        self.get_values = Button(self, text='get_values',command=self.get_values, width=16)
        self.get_values.grid(row=2, column=3)
        self.set_values = Button(self, text='set_values', command=self.set_values , width=16)
        self.set_values.grid(row=2, column=2)
        self.print_table = Button(self, command=self.print_table, text='print_table', width=16)
        self.print_table.grid(row=2, column=1)
        self.open_file = Button(self, command=self.open_file,text='открыть', width=16)
        self.open_file.grid(row=2, column=0)
        self.functions = Button(self, command=self.functions, text='Функции', width=16)
        self.functions.grid(row=1, column=4)
        self.filter_rows = Button(self, command=self.filter_rows, text='filter_rows', width=16)
        self.filter_rows.grid(row=2, column=4)
        self.refresh_button = Button(self, command=self.refresh_button, text='Обновить', width=16)
        self.refresh_button.grid(row=1, column=5)
        self.instruction = Button(self, command=self.instruction, text='Инструкция', width=16)
        self.instruction.grid(row=2, column=5)


    def get_rows_by_number_new_window(self):
        frame = self.csv
        start = int(self.start_arg_entry.get())
        stop = int(self.stop_arg_entry.get())
        text1 = frame[start:stop + 1]
        self.csv = frame[start:stop + 1]
        columns = text1.columns
        self.label.insert(1.0, tabulate(text1, headers=columns))

    def get_rows_by_number(self):
        info = '\n\n\nget_rows_by_number(start, [stop], copy_table=False) – получение таблицы из одной строки или из строк из интервала по номеру строки.' \
               ' Функция либо копирует исходные данные, либо создает новое представление таблицы, работающее с исходным набором данных (copy_table=False),' \
               ' таким образом изменения, внесенные через это представления будут наблюдаться и в исходной таблице.'
        self.newWindow = Toplevel(self)
        self.newWindow.title("get_rows_by_number")
        start_type = IntVar()
        stop_type = IntVar()
        copy_type = BooleanVar()
        start_arg_label = Label(self.newWindow,text="start:")
        stop_arg_label = Label(self.newWindow, text="stop:")
        start_arg_label.grid(row=0, column=0, sticky="e")
        stop_arg_label.grid(row=0, column=2, sticky="e")
        self.start_arg_entry = Entry(self.newWindow, textvariable=start_type)
        self.stop_arg_entry = Entry(self.newWindow, textvariable=stop_type)
        self.start_arg_entry.grid(row=0,column=1, padx=5, pady=5, sticky="e")
        self.stop_arg_entry.grid(row=0,column=3, padx=5, pady=5, sticky="e")
        self.label = Text(self.newWindow, width=150)
        self.label.insert(1.0, info)
        self.label.grid(row=2)
        button = Button(self.newWindow, command=self.get_rows_by_number_new_window, text='OK!', width=3)
        button_save = Button(self.newWindow, command=self.button_save, text='SAVE', width=5)
        button.grid(row=0, column=4, padx=5, pady=5, sticky="w")
        button_save.grid(row=0, column=5, padx=5, pady=5, sticky="w")


    def get_rows_by_index_pandas(self):
        key = self.values_arg_entry.get()
        split = key.split(',')
        try:
            text = pandas.concat([self.csv[split]])
        except KeyError:
            self.label.delete(0.0, END)
            text = 'Введите столбцы строкой(, через запятую)'
        except AttributeError:
            text = 'Введите столбцы, которые есть в таблице'
        except IndexError:
            text = 'Введите столбцы, которые есть в таблице'
        columns = self.csv.columns
        self.csv = text
        self.label.insert(1.0, text)

    def get_rows_by_index(self):
        info = '\n\n\nget_rows_by_index(val1, … , copy_table=False) – получение новой таблицы из одной строки или из строк со' \
               ' значениями в первом столбце, совпадающими с переданными аргументами val1, … , valN. Функция либо копирует ' \
               'исходные данные, либо создает новое представление таблицы, работающее с исходным набором данных (copy_table=False),' \
               ' таким образом изменения, внесенные через это представления будут наблюдаться и в исходной таблице.' \
               '\n\n\nВводить стольцы через запятую!'
        self.by_index = Toplevel(self)
        self.by_index.title("get_rows_by_index")
        values_arg_label = Label(self.by_index,text="values:")
        values_arg_label.grid(row=0, column=0, sticky="e")
        self.values_arg_entry = Entry(self.by_index)
        self.values_arg_entry.grid(row=0,column=1, padx=5, pady=5, sticky="e")
        self.label = Text(self.by_index, width=150)
        self.label.insert(1.0, info)
        self.label.grid(row=2)
        button_ok = Button(self.by_index, command=self.get_rows_by_index_pandas, text='OK!', width=3)
        button_save = Button(self.by_index, command=self.button_save, text='SAVE', width=5)
        button_ok.grid(row=0, column=4, padx=5, pady=5, sticky="w")
        button_save.grid(row=0, column=5, padx=5, pady=5, sticky="w")

    def get_column_types(self):
        #by_number - built-in
        info='\n\n\nget_column_types(by_number=True) – получение словаря вида столбец:тип_значений. ' \
             'Тип значения: int, float, bool, str (по умолчанию для всех столбцов). Параметр by_number ' \
             'определяет вид значения столбец – целочисленный индекс столбца или его строковое представление.' \
             '\n\n\n'
        self.column_types = Toplevel(self)
        self.column_types.title("get_column_types")
        buffer = io.StringIO()
        self.csv.info(buf=buffer, null_counts=False, memory_usage=False)
        text = buffer.getvalue()
        label = Text(self.column_types)
        label.insert(1.0, text)
        label.insert(END, info)
        label.grid(row=2)

    def set_column_types_pandas(self):
        types_dict = self.set_entry.get()
        buffer = io.StringIO()
        if types_dict == 'int':
            frame_show = self.csv.select_dtypes(include=['int64'])
            frame_show.info(buf=buffer, null_counts=False, memory_usage=False)
            text = buffer.getvalue()
        elif types_dict == 'float':
            frame_show = self.csv.select_dtypes(include=['int64'])
            frame_show.info(buf=buffer, null_counts=False, memory_usage=False)
            text = buffer.getvalue()
        elif types_dict == 'bool':
            frame_show = self.csv.select_dtypes(include=['bool'])
            frame_show.info(buf=buffer, null_counts=False, memory_usage=False)
            text = buffer.getvalue()
        elif types_dict == 'str':
            frame_show = self.csv.select_dtypes(include=['object'])
            frame_show.info(buf=buffer, null_counts=False, memory_usage=False)
            text = buffer.getvalue()
        self.label.insert(1.0, text)

    def set_column_types(self):
        info='\n\n\nset_column_types(types_dict, by_number=True) – задание словаря вида столбец:тип_значений.' \
             ' Тип значения: int, float, bool, str (по умолчанию для всех столбцов). Параметр by_number определяет ' \
             'вид значения столбец – целочисленный индекс столбца или его строковое представление.' \
             '\n\n\ntypes_dict:int, float, bool, str'
        self.column_types_set = Toplevel(self)
        self.column_types_set.title("column_types_set")
        self.set_label = Label(self.column_types_set, text="types_dict:")
        self.set_label.grid(row=0, column=0, sticky="e")
        self.set_entry = Entry(self.column_types_set)
        self.set_entry.grid(row=0, column=1, padx=5, pady=5, sticky="e")
        button_ok = Button(self.column_types_set, command=self.set_column_types_pandas, text='OK!', width=3)
        button_save = Button(self.column_types_set, command=self.button_save, text='SAVE', width=5)
        button_ok.grid(row=0, column=3, padx=5, pady=5, sticky="e")
        button_save.grid(row=0, column=4, padx=5, pady=5, sticky="e")
        self.label = Text(self.column_types_set)
        self.label.insert(1.0, info)
        self.label.grid(row=2)

    def get_values_pandas(self):
        column = self.get_entry.get()
        frame = self.csv
        try:
            column1 = int(column)
        except:
            column1 = column
        try:
            if type(column1) == str:
                text = frame[column]
                self.csv = text
            elif type(column1) == int:
                column_index = frame.columns[column1]
                text = frame[column_index]
                self.csv = text
        except KeyError:
            text = 'Введите столбцы, которые есть в таблице'
        except TypeError:
            text = 'Сравниваемые столбцы не должны быть строками и числами'
        except IndexError:
            text = 'Введите столбцы, которые есть в таблице'
        self.label.insert(1.0, text)

    def get_values(self):
        info='\n\n\nget_values(column=0) – получение списка значений ' \
             '(типизированных согласно типу столбца) таблицы из ' \
             'столбца либо по номеру столбца (целое число, значение ' \
             'по умолчанию 0, либо по имени столбца)'
        self.get_values = Toplevel(self)
        self.get_values.title("get_values")
        self.get_label = Label(self.get_values, text="column:")
        self.get_label.grid(row=0, column=0, sticky="e")
        self.get_entry = Entry(self.get_values)
        self.get_entry.grid(row=0, column=1, padx=5, pady=5, sticky="e")
        button_ok = Button(self.get_values, command=self.get_values_pandas, text='OK!', width=3)
        button_save = Button(self.get_values, command=self.button_save, text='SAVE', width=5)
        button_ok.grid(row=0, column=3, padx=5, pady=5, sticky="e")
        button_save.grid(row=0, column=4, padx=5, pady=5, sticky="e")
        self.label = Text(self.get_values)
        self.label.insert(1.0, info)
        self.label.grid(row=2)

    def set_values_pandas(self):
        values = self.value_entry.get()
        column = self.column_entry.get()
        frame = self.csv
        try:
            column1 = int(column)
        except:
            column1 = column
        try:
            if type(column1) == str:
                frame.loc[:, column1] = values  # Set value for an entire column из документации
                text = frame
            elif type(column1) == int:
                column_index = frame.columns[column1]
                frame.loc[:, column_index] = values
                text = frame
        except KeyError:
            text = 'Введите столбцы, которые есть в таблице'
        except TypeError:
            text = 'Сравниваемые столбцы не должны быть строками и числами'
        except IndexError:
            text = 'Введите столбцы, которые есть в таблице'
        self.label.insert(1.0, text)

    def set_values(self):
        info = '\n\n\nset_values(values, column=0) – задание списка значений values для столбца таблицы' \
               ' (типизированных согласно типу столбца) либо по номеру столбца (целое число, значение по умолчанию 0, либо по имени столбца).'
        self.set_values = Toplevel(self)
        self.set_values.title("set_values")
        self.value_label = Label(self.set_values, text="value:")
        self.column_label = Label(self.set_values, text='column:')
        self.value_label.grid(row=0, column=0, sticky="e")
        self.column_label.grid(row=0, column=2, sticky='e')
        self.value_entry = Entry(self.set_values)
        self.column_entry = Entry(self.set_values)
        self.value_entry.grid(row=0, column=1, padx=5, pady=5, sticky="e")
        self.column_entry.grid(row=0, column=3, padx=5, pady=5, sticky="e")
        self.label = Text(self.set_values)
        self.label.insert(1.0, info)
        self.label.grid(row=2)
        button_ok = Button(self.set_values, command=self.set_values_pandas, text='OK!', width=3)
        button_save = Button(self.set_values, command=self.button_save, text='SAVE', width=5)
        button_ok.grid(row=0, column=4, padx=5, pady=5, sticky="e")
        button_save.grid(row=0, column=5, padx=5, pady=5, sticky="e")

    def functions(self):
        # eq (==), gr (>), ls (<), ge (>=), le (<=), ne (!=)
        self.functions = Toplevel(self)
        self.eq_button = Button(self.functions, text='Equall ==', command=self.equall, width=16)
        self.gr_button = Button(self.functions, text='Greater >', command=self.greater, width=16)
        self.ls_button = Button(self.functions, text='Less <', command=self.less, width=16)
        self.ge_button = Button(self.functions, text='G or E >=', command=self.gr_or_eq, width=16)
        self.le_button = Button(self.functions, text='L or E <=', command=self.ls_or_eq,width=16)
        self.ne_button = Button(self.functions, text='Not Eq !=', command=self.not_eq, width=16)
        self.eq_button.grid(row=0, column=0)
        self.gr_button.grid(row=0, column=1)
        self.ls_button.grid(row=0, column=2)
        self.ge_button.grid(row=1, column=0)
        self.le_button.grid(row=1, column=1)
        self.ne_button.grid(row=1, column=2)

    def equall_pandas(self):
        column1 = self.first_entry.get()
        column2 = self.second_entry.get()
        try:
            column1 = int(column1)
            column2 = int(column2)
        except:
            column1 = column1
            column2 = column2
        frame = self.csv
        try:
            if type(column1) == str:
                equality = frame[column1] == frame[column2]
                frame['equally'] = equality
                text = frame['equally']
            elif type(column2) == int:
                column_index_1 = frame.columns[column1]
                column_index_2 = frame.columns[column2]
                equality = frame[column_index_1] == frame[column_index_2]
                frame['equally'] = equality
                text = frame['equally']
        except KeyError:
            text = 'Введите столбцы, которые есть в таблице'
        except IndexError:
            text = 'Введите столбцы, которые есть в таблице'
        self.label = Text(self.equall)
        self.label.insert(1.0, text)
        self.label.grid(row=2)

    def equall(self):
        self.equall = Toplevel(self.functions)
        self.first_col_label = Label(self.equall, text='Column 1:')
        self.second_col_label = Label(self.equall, text='Column 2:')
        self.first_entry = Entry(self.equall)
        self.second_entry = Entry(self.equall)
        self.first_col_label.grid(row=0, column=0, sticky="e")
        self.second_col_label.grid(row=0, column=2, sticky="e")
        self.first_entry.grid(row=0, column=1, padx=5, pady=5, sticky="e")
        self.second_entry.grid(row=0, column=3, padx=5, pady=5, sticky="e")
        button_ok = Button(self.equall, command=self.equall_pandas, text='OK!', width=3)
        button_save = Button(self.equall, command=self.button_save, text='SAVE', width=5)
        button_ok.grid(row=0, column=4, padx=5, pady=5, sticky="e")
        button_save.grid(row=0, column=5, padx=5, pady=5, sticky="e")

    def greater_pandas(self):
        column1 = self.first_entry.get()
        column2 = self.second_entry.get()
        try:
            column1 = int(column1)
            column2 = int(column2)
        except:
            column1 = column1
            column2 = column2
        frame = self.csv
        pandas.options.display.max_rows = len(frame)
        try:
            if type(column1) == str:
                greater_than = frame[column1] > frame[column2]
                frame['greater'] = greater_than
                text = frame['greater']
                self.csv = frame
            elif type(column1) == int:
                column_index_1 = frame.columns[column1]
                column_index_2 = frame.columns[column2]
                greater_than = frame[column_index_1] > frame[column_index_2]
                frame['greater'] = greater_than
                text = frame['greater']
        except KeyError:
            text = 'Введите столбцы, которые есть в таблице'
        except TypeError:
            text = 'Сравниваемые столбцы не должны быть строками и числами'
        except IndexError:
            text = 'Введите столбцы, которые есть в таблице'
        self.label = Text(self.greater)
        self.label.insert(1.0, text)
        self.label.grid(row=2)

    def greater(self):
        self.greater = Toplevel(self.functions)
        self.first_col_label = Label(self.greater, text='Column 1:')
        self.second_col_label = Label(self.greater, text='Column 2:')
        self.first_entry = Entry(self.greater)
        self.second_entry = Entry(self.greater)
        self.first_col_label.grid(row=0, column=0, sticky="e")
        self.second_col_label.grid(row=0, column=2, sticky="e")
        self.first_entry.grid(row=0, column=1, padx=5, pady=5, sticky="e")
        self.second_entry.grid(row=0, column=3, padx=5, pady=5, sticky="e")
        button_ok = Button(self.greater, command=self.greater_pandas, text='OK!', width=3)
        button_save = Button(self.greater, command=self.button_save, text='SAVE', width=5)
        button_ok.grid(row=0, column=4, padx=5, pady=5, sticky="e")
        button_save.grid(row=0, column=5, padx=5, pady=5, sticky="e")

    def less_pandas(self):
        frame = self.csv
        column1 = self.first_entry.get()
        column2 = self.second_entry.get()
        try:
            column1 = int(column1)
            column2 = int(column2)
        except:
            column1 = column1
            column2 = column2
        pandas.options.display.max_rows = len(frame)
        try:
            if type(column1) == str:
                greater_than = frame[column1] < frame[column2]
                frame['greater'] = greater_than
                text = frame['greater']
                self.csv = frame
            elif type(column1) == int:
                column_index_1 = frame.columns[column1]
                column_index_2 = frame.columns[column2]
                greater_than = frame[column_index_1] < frame[column_index_2]
                frame['greater'] = greater_than
                text = frame['greater']
        except KeyError:
            text = 'Введите столбцы, которые есть в таблице'
        except TypeError:
            text = 'Сравниваемые столбцы не должны быть строками и числами'
        except IndexError:
            text = 'Введите столбцы, которые есть в таблице'
        self.label = Text(self.less)
        self.label.insert(1.0, text)
        self.label.grid(row=2)

    def less(self):
        self.less = Toplevel(self.functions)
        self.first_col_label = Label(self.less, text='Column 1:')
        self.second_col_label = Label(self.less, text='Column 2:')
        self.first_entry = Entry(self.less)
        self.second_entry = Entry(self.less)
        self.first_col_label.grid(row=0, column=0, sticky="e")
        self.second_col_label.grid(row=0, column=2, sticky="e")
        self.first_entry.grid(row=0, column=1, padx=5, pady=5, sticky="e")
        self.second_entry.grid(row=0, column=3, padx=5, pady=5, sticky="e")
        button_ok = Button(self.less, command=self.less_pandas, text='OK!', width=3)
        button_save = Button(self.less, command=self.button_save, text='SAVE', width=5)
        button_ok.grid(row=0, column=4, padx=5, pady=5, sticky="e")
        button_save.grid(row=0, column=5, padx=5, pady=5, sticky="e")

    def gr_or_eq_pandas(self):
        frame = self.csv
        column1 = self.first_entry.get()
        column2 = self.second_entry.get()
        try:
            column1 = int(column1)
            column2 = int(column2)
        except:
            column1 = column1
            column2 = column2
        pandas.options.display.max_rows = len(frame)
        try:
            if type(column1) == str:
                greater_than = frame[column1] >= frame[column2]
                frame['greater'] = greater_than
                text = frame['greater']
                self.csv = frame
            elif type(column1) == int:
                column_index_1 = frame.columns[column1]
                column_index_2 = frame.columns[column2]
                greater_than = frame[column_index_1] >= frame[column_index_2]
                frame['greater'] = greater_than
                text = frame['greater']
        except KeyError:
            text = 'Введите столбцы, которые есть в таблице'
        except TypeError:
            text = 'Сравниваемые столбцы не должны быть строками и числами'
        except IndexError:
            text = 'Введите столбцы, которые есть в таблице'
        self.label = Text(self.gr_or_eq)
        self.label.insert(1.0, text)
        self.label.grid(row=2)

    def gr_or_eq(self):
        self.gr_or_eq = Toplevel(self.functions)
        self.first_col_label = Label(self.gr_or_eq, text='Column 1:')
        self.second_col_label = Label(self.gr_or_eq, text='Column 2:')
        self.first_entry = Entry(self.gr_or_eq)
        self.second_entry = Entry(self.gr_or_eq)
        self.first_col_label.grid(row=0, column=0, sticky="e")
        self.second_col_label.grid(row=0, column=2, sticky="e")
        self.first_entry.grid(row=0, column=1, padx=5, pady=5, sticky="e")
        self.second_entry.grid(row=0, column=3, padx=5, pady=5, sticky="e")
        button_ok = Button(self.gr_or_eq, command=self.gr_or_eq_pandas, text='OK!', width=3)
        button_save = Button(self.gr_or_eq, command=self.button_save, text='SAVE', width=5)
        button_ok.grid(row=0, column=4, padx=5, pady=5, sticky="e")
        button_save.grid(row=0, column=5, padx=5, pady=5, sticky="e")

    def ls_or_eq_pandas(self):
        frame = self.csv
        column1 = self.first_entry.get()
        column2 = self.second_entry.get()
        try:
            column1 = int(column1)
            column2 = int(column2)
        except:
            column1 = column1
            column2 = column2
        pandas.options.display.max_rows = len(frame)
        try:
            if type(column1) == str:
                greater_than = frame[column1] <= frame[column2]
                frame['greater'] = greater_than
                text = frame['greater']
                self.csv = frame
            elif type(column1) == int:
                column_index_1 = frame.columns[column1]
                column_index_2 = frame.columns[column2]
                greater_than = frame[column_index_1] <= frame[column_index_2]
                frame['greater'] = greater_than
                text = frame['greater']
        except KeyError:
            text = 'Введите столбцы, которые есть в таблице'
        except TypeError:
            text = 'Сравниваемые столбцы не должны быть строками и числами'
        except IndexError:
            text = 'Введите столбцы, которые есть в таблице'
        self.label = Text(self.ls_or_eq)
        self.label.insert(1.0, text)
        self.label.grid(row=2)

    def ls_or_eq(self):
        self.ls_or_eq = Toplevel(self.functions)
        self.first_col_label = Label(self.ls_or_eq, text='Column 1:')
        self.second_col_label = Label(self.ls_or_eq, text='Column 2:')
        self.first_entry = Entry(self.ls_or_eq)
        self.second_entry = Entry(self.ls_or_eq)
        self.first_col_label.grid(row=0, column=0, sticky="e")
        self.second_col_label.grid(row=0, column=2, sticky="e")
        self.first_entry.grid(row=0, column=1, padx=5, pady=5, sticky="e")
        self.second_entry.grid(row=0, column=3, padx=5, pady=5, sticky="e")
        button_ok = Button(self.ls_or_eq, command=self.ls_or_eq_pandas, text='OK!', width=3)
        button_save = Button(self.ls_or_eq, command=self.button_save, text='SAVE', width=5)
        button_ok.grid(row=0, column=4, padx=5, pady=5, sticky="e")
        button_save.grid(row=0, column=5, padx=5, pady=5, sticky="e")

    def not_eq_pandas(self):
        frame = self.csv
        column1 = self.first_entry.get()
        column2 = self.second_entry.get()
        try:
            column1 = int(column1)
            column2 = int(column2)
        except:
            column1 = column1
            column2 = column2
        pandas.options.display.max_rows = len(frame)
        try:
            if type(column1) == str:
                greater_than = frame[column1] != frame[column2]
                frame['greater'] = greater_than
                text = frame['greater']
                self.csv = frame
            elif type(column1) == int:
                column_index_1 = frame.columns[column1]
                column_index_2 = frame.columns[column2]
                greater_than = frame[column_index_1] != frame[column_index_2]
                frame['greater'] = greater_than
                text = frame['greater']
        except KeyError:
            text = 'Введите столбцы, которые есть в таблице'
        except IndexError:
            text = 'Введите столбцы, которые есть в таблице'
        self.label = Text(self.not_eq)
        self.label.insert(1.0, text)
        self.label.grid(row=2)

    def not_eq(self):
        self.not_eq = Toplevel(self.functions)
        self.first_col_label = Label(self.not_eq, text='Column 1:')
        self.second_col_label = Label(self.not_eq, text='Column 2:')
        self.first_entry = Entry(self.not_eq)
        self.second_entry = Entry(self.not_eq)
        self.first_col_label.grid(row=0, column=0, sticky="e")
        self.second_col_label.grid(row=0, column=2, sticky="e")
        self.first_entry.grid(row=0, column=1, padx=5, pady=5, sticky="e")
        self.second_entry.grid(row=0, column=3, padx=5, pady=5, sticky="e")
        button_ok = Button(self.not_eq, command=self.not_eq_pandas, text='OK!', width=3)
        button_save = Button(self.not_eq, command=self.button_save, text='SAVE', width=5)
        button_ok.grid(row=0, column=4, padx=5, pady=5, sticky="e")
        button_save.grid(row=0, column=5, padx=5, pady=5, sticky="e")

    def filter_rows_pandas(self):
        frame = self.csv
        bool_list = self.bool_list_entry.get()
        try:
            bool_list = frame.loc[frame[bool_list] == True]
            self.csv = bool_list
        except KeyError:
            bool_list = 'Введите столбцы, которые есть в таблице'
        except IndexError:
            bool_list = 'Введите столбцы, которые есть в таблице'
        self.label.insert(1.0, bool_list)

    def filter_rows(self):
        self.filter_rows = Toplevel(self)
        self.bool_list_label = Label(self.filter_rows, text='Boolean column:')
        self.bool_list_entry = Entry(self.filter_rows)
        self.bool_list_label.grid(row=0, column=0, sticky="e")
        self.bool_list_entry.grid(row=0, column=1, padx=5, pady=5, sticky="e")
        button_ok = Button(self.filter_rows, command=self.filter_rows_pandas, text='OK!', width=3)
        button_save = Button(self.filter_rows, command=self.button_save, text='SAVE', width=5)
        button_ok.grid(row=0, column=3, padx=5, pady=5, sticky="e")
        button_save.grid(row=0, column=4, padx=5, pady=5, sticky="e")
        self.label = Text(self.filter_rows)
        self.label.insert(1.0, '\n\n\nColumn может являться функцией [equally, greater, less, greater_or_equally, less_or_equally, not_equall]')
        self.label.grid(row=2)

    def print_table(self):
        print('print_table')
        newWindow = Toplevel(self)
        frame = self.csv
        frame_columns = frame.columns
        labelExample = Text(newWindow, width=150)
        labelExample.insert(1.0, tabulate(frame, headers=frame_columns))
        labelExample.grid(row=2)

    def button_save(self):
        files = [('CSV Files', '*.csv'),
                 ('Text Document', '*.txt'),
                 ('Pickle Files', '*.pkl')]
        file_name = fd.asksaveasfile(filetypes=files, defaultextension=files)
        if '.csv' in str(file_name):
            self.csv.to_csv(file_name)
        elif '.pkl' in str(file_name):
            with open(file_name.name, 'wb') as file_obj:
                self.csv.to_pickle(file_obj)
        elif '.txt' in str(file_name):
            with open(file_name.name, 'a') as file_obj:
                file_obj.write(
                    self.csv.to_string(header=True, index=False)
                )

    def open_file(self):
        files = [('CSV Files', '*.csv'),
                 ('Text Document', '*.txt'),
                 ('Pickle Files', '*.pkl')]
        self.file_name = fd.askopenfilename(filetypes=files, defaultextension=files)
        if '.csv' in self.file_name:
            self.csv = pandas.read_csv(self.file_name)
        elif '.pkl' in self.file_name:
            self.csv = pandas.read_pickle(self.file_name)
        elif '.txt' in self.file_name:
            self.csv = pandas.read_csv(self.file_name)
        pandas.options.display.max_rows = len(self.csv)

    def refresh_button(self):
        if '.csv' in self.file_name:
            self.csv = pandas.read_csv(self.file_name)
        elif '.pkl' in self.file_name:
            self.csv = pandas.read_pickle(self.file_name)
        elif '.txt' in self.file_name:
            self.csv = pandas.read_csv(self.file_name)

    def instruction(self):
        self.instruction = Toplevel(self)
        instruction_text = Text(self.instruction)
        text = 'Инструкция:\n\n!После выполнения каждой функции надо нажать на главном окне обновить!\n' \
               '\nЕсли хотим изменить внутреннее представление таблицы в программе не нажимаем обновить\n\n' \
               'Описание работы функций:eq (==), gr (>), ls (<), ge (>=), le (<=), ne (==),' \
               ' которые возвращают список булевских значений длинной в количество строк сравниваемых столбцов.' \
               ' Реализовать функцию filter_rows (bool_list, copy_table=False) – получение новой таблицы из строк ' \
               'для которых в bool_list (длинной в количество строк в таблице) находится значение True.\n\n\n' \
                'Имена новых столбцов при выполнении функций:eq (==), gr (>), ls (<), ge (>=), le (<=), ne (==)' \
               'и сохранении в файл находятся в окне функции filter_rows\n\n\n' \
               'Программа работает с файлами типа .csv, .pkl, .txt\n' \
               'Чтобы сохранить результат выполнения функции - надо нажать SAVE в окне'
        instruction_text.insert(1.0, text)
        instruction_text.grid(row=1)

    def centerWindow(self):
        w = 732
        h = 51
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

def main():
    root = Tk()
    ex = TablePackage(root)
    root.mainloop()

if __name__ == '__main__':
    main()

