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

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.parent.title("Parser")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        self.initUI()

    def initUI(self):
        self.entry = Label(self, width=50, height=50)
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
        self.pack()

    def get_rows_by_number_new_window(self):
        frame = self.csv
        start = int(self.start_arg_entry.get())
        stop = int(self.stop_arg_entry.get())
        copy_table = bool(self.copy_table_entry.get())
        copy_table = True
        if copy_table == True:
            text1 = frame[start:stop + 1]
            self.csv = frame[start:stop + 1]
        elif copy_table == False:
            text1 = frame[start:stop + 1]
            self.csv = frame[start:stop + 1]
        label = Text(self.newWindow, width=150)
        columns = text1.columns
        label.insert(1.0, tabulate(text1, headers=columns))
        label.grid(row=2)

    def get_rows_by_number(self):
        self.newWindow = Toplevel(self)
        start_type = IntVar()
        stop_type = IntVar()
        copy_type = BooleanVar()
        start_arg_label = Label(self.newWindow,text="start:")
        stop_arg_label = Label(self.newWindow, text="stop:")
        copy_table_label = Label(self.newWindow, text='copy_table:')
        start_arg_label.grid(row=0, column=0, sticky="w")
        stop_arg_label.grid(row=0, column=2, sticky="w")
        copy_table_label.grid(row=0, column=4, sticky="w")
        self.start_arg_entry = Entry(self.newWindow, textvariable=start_type)
        self.stop_arg_entry = Entry(self.newWindow, textvariable=stop_type)
        self.copy_table_entry = Entry(self.newWindow, textvariable=copy_type)
        self.start_arg_entry.grid(row=0,column=1, padx=5, pady=5, sticky="w")
        self.stop_arg_entry.grid(row=0,column=3, padx=5, pady=5, sticky="w")
        self.copy_table_entry.grid(row=0,column=5, padx=5, pady=5, sticky="w")
        button = Button(self.newWindow, command=self.get_rows_by_number_new_window, text='OK!', width=3)
        button_save = Button(self.newWindow, command=self.button_save, text='SAVE', width=5)
        button.grid(row=0, column=6, padx=5, pady=5, sticky="w")
        button_save.grid(row=0, column=7, padx=5, pady=5, sticky="w")
        self.mainloop()

    def get_rows_by_index_pandas(self):
        key = self.values_arg_entry.get()
        split = key.split(',')
        print(pandas.concat([self.csv[split]], ignore_index=True))
        text = pandas.concat([self.csv[split]])
        label = Text(self.by_index, width=150)
        columns = self.csv.columns
        self.csv = text
        label.insert(1.0, text)
        label.grid(row=2)

    def get_rows_by_index(self):
        print('get_rows_by_index')
        self.by_index = Toplevel(self)
        values_arg_label = Label(self.by_index,text="values:")
        copy_table_label = Label(self.by_index, text='copy_table:')
        values_arg_label.grid(row=0, column=0, sticky="w")
        copy_table_label.grid(row=0, column=2, sticky="w")
        self.values_arg_entry = Entry(self.by_index)
        self.copy_table_entry = Entry(self.by_index)
        self.values_arg_entry.grid(row=0,column=1, padx=5, pady=5, sticky="w")
        self.copy_table_entry.grid(row=0,column=3, padx=5, pady=5, sticky="w")
        button_ok = Button(self.by_index, command=self.get_rows_by_index_pandas, text='OK!', width=3)
        button_save = Button(self.by_index, command=self.button_save, text='SAVE', width=5)
        button_ok.grid(row=0, column=4, padx=5, pady=5, sticky="w")
        button_save.grid(row=0, column=5, padx=5, pady=5, sticky="w")

    def get_column_types(self):
        #by_number - built-in
        print('get_column_types')
        self.column_types = Toplevel(self)
        buffer = io.StringIO()
        self.csv.info(buf=buffer, null_counts=False, memory_usage=False)
        text = buffer.getvalue()
        label = Text(self.column_types)
        label.insert(1.0, text)
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
        self.label = Text(self.column_types_set)
        self.label.insert(1.0, text)
        self.label.grid(row=2)

    def set_column_types(self):
        print('set_column_types')
        self.column_types_set = Toplevel(self)
        self.set_label = Label(self.column_types_set, text="types_dict:")
        self.set_label.grid(row=0, column=0, sticky="w")
        self.set_entry = Entry(self.column_types_set)
        self.set_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        button_ok = Button(self.column_types_set, command=self.set_column_types_pandas, text='OK!', width=3)
        button_save = Button(self.column_types_set, command=self.button_save, text='SAVE', width=5)
        button_ok.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        button_save.grid(row=0, column=4, padx=5, pady=5, sticky="w")

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
        self.label = Text(self.get_values)
        self.label.insert(1.0, text)
        self.label.grid(row=2)

    def get_values(self):
        print('get_values')
        self.get_values = Toplevel(self)
        self.get_label = Label(self.get_values, text="column:")
        self.get_label.grid(row=0, column=0, sticky="w")
        self.get_entry = Entry(self.get_values)
        self.get_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        button_ok = Button(self.get_values, command=self.get_values_pandas, text='OK!', width=3)
        button_save = Button(self.get_values, command=self.button_save, text='SAVE', width=5)
        button_ok.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        button_save.grid(row=0, column=4, padx=5, pady=5, sticky="w")

    def set_values_pandas(self):
        print('set_values')
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
        self.label = Text(self.set_values)
        self.label.insert(1.0, text)
        self.label.grid(row=2)

    def set_values(self):
        self.set_values = Toplevel(self)
        self.value_label = Label(self.set_values, text="value:")
        self.column_label = Label(self.set_values, text='column:')
        self.value_label.grid(row=0, column=0, sticky="w")
        self.column_label.grid(row=0, column=2, sticky='w')
        self.value_entry = Entry(self.set_values)
        self.column_entry = Entry(self.set_values)
        self.value_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.column_entry.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        button_ok = Button(self.set_values, command=self.set_values_pandas, text='OK!', width=3)
        button_save = Button(self.set_values, command=self.button_save, text='SAVE', width=5)
        button_ok.grid(row=0, column=4, padx=5, pady=5, sticky="w")
        button_save.grid(row=0, column=5, padx=5, pady=5, sticky="w")

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
        column1 = self.first_entry.get().lower()
        column2 = self.second_entry.get().lower()
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
            #try:
                equality = frame[column1] == frame[column2]
                frame['equally'] = equality
                text = frame['equally']
                '''except:
                    column_index_1 = frame.columns[column1]
                    column_index_2 = frame.columns[column2]
                    equality = frame[column_index_1] == frame[column_index_2]
                    frame['equally'] = equality
                    text = frame['equally']'''

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
        self.first_col_label.grid(row=0, column=0, sticky="w")
        self.second_col_label.grid(row=0, column=2, sticky="w")
        self.first_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.second_entry.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        button_ok = Button(self.equall, command=self.equall_pandas, text='OK!', width=3)
        button_save = Button(self.equall, command=self.button_save, text='SAVE', width=5)
        button_ok.grid(row=0, column=4, padx=5, pady=5, sticky="w")
        button_save.grid(row=0, column=5, padx=5, pady=5, sticky="w")

    def greater_pandas(self):
        column1 = self.first_entry.get().lower()
        column2 = self.second_entry.get().lower()
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
        self.first_col_label.grid(row=0, column=0, sticky="w")
        self.second_col_label.grid(row=0, column=2, sticky="w")
        self.first_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.second_entry.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        button_ok = Button(self.greater, command=self.greater_pandas, text='OK!', width=3)
        button_save = Button(self.greater, command=self.button_save, text='SAVE', width=5)
        button_ok.grid(row=0, column=4, padx=5, pady=5, sticky="w")
        button_save.grid(row=0, column=5, padx=5, pady=5, sticky="w")

    def less_pandas(self):
        frame = self.csv
        column1 = self.first_entry.get().lower()
        column2 = self.second_entry.get().lower()
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
        self.first_col_label.grid(row=0, column=0, sticky="w")
        self.second_col_label.grid(row=0, column=2, sticky="w")
        self.first_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.second_entry.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        button_ok = Button(self.less, command=self.less_pandas, text='OK!', width=3)
        button_save = Button(self.less, command=self.button_save, text='SAVE', width=5)
        button_ok.grid(row=0, column=4, padx=5, pady=5, sticky="w")
        button_save.grid(row=0, column=5, padx=5, pady=5, sticky="w")

    def gr_or_eq_pandas(self):
        frame = self.csv
        column1 = self.first_entry.get().lower()
        column2 = self.second_entry.get().lower()
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
        self.first_col_label.grid(row=0, column=0, sticky="w")
        self.second_col_label.grid(row=0, column=2, sticky="w")
        self.first_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.second_entry.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        button_ok = Button(self.gr_or_eq, command=self.gr_or_eq_pandas, text='OK!', width=3)
        button_save = Button(self.gr_or_eq, command=self.button_save, text='SAVE', width=5)
        button_ok.grid(row=0, column=4, padx=5, pady=5, sticky="w")
        button_save.grid(row=0, column=5, padx=5, pady=5, sticky="w")

    def ls_or_eq_pandas(self):
        frame = self.csv
        column1 = self.first_entry.get().lower()
        column2 = self.second_entry.get().lower()
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
        self.first_col_label.grid(row=0, column=0, sticky="w")
        self.second_col_label.grid(row=0, column=2, sticky="w")
        self.first_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.second_entry.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        button_ok = Button(self.ls_or_eq, command=self.ls_or_eq_pandas, text='OK!', width=3)
        button_save = Button(self.ls_or_eq, command=self.button_save, text='SAVE', width=5)
        button_ok.grid(row=0, column=4, padx=5, pady=5, sticky="w")
        button_save.grid(row=0, column=5, padx=5, pady=5, sticky="w")

    def not_eq_pandas(self):
        frame = self.csv
        column1 = self.first_entry.get().lower()
        column2 = self.second_entry.get().lower()
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
        self.first_col_label.grid(row=0, column=0, sticky="w")
        self.second_col_label.grid(row=0, column=2, sticky="w")
        self.first_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.second_entry.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        button_ok = Button(self.not_eq, command=self.not_eq_pandas, text='OK!', width=3)
        button_save = Button(self.not_eq, command=self.button_save, text='SAVE', width=5)
        button_ok.grid(row=0, column=4, padx=5, pady=5, sticky="w")
        button_save.grid(row=0, column=5, padx=5, pady=5, sticky="w")

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
        self.bool_list_label.grid(row=0, column=0, sticky="w")
        self.bool_list_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        button_ok = Button(self.filter_rows, command=self.filter_rows_pandas, text='OK!', width=3)
        button_save = Button(self.filter_rows, command=self.button_save, text='SAVE', width=5)
        button_ok.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        button_save.grid(row=0, column=4, padx=5, pady=5, sticky="w")
        self.label = Text(self.filter_rows)
        self.label.insert(1.0, 'Column может являться функцией [equally, greater, less, greater_or_equally, less_or_equally, not_equall]')
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
                #pickle.dump(self.csv, file_obj)
        elif '.txt' in str(file_name):
            with open(file_name.name, 'a') as file_obj:
                file_obj.write(
                    self.csv.to_string(header=False, index=False)
                )

    def open_file(self):
        files = [('CSV Files', '*.csv'),
                 ('Text Document', '*.txt'),
                 ('Pickle Files', '*.pkl')]
        file_name = fd.askopenfilename(filetypes=files, defaultextension=files)
        if '.csv' in file_name:
            self.csv = pandas.read_csv(file_name)
        elif '.pkl' in file_name:
            self.csv = pandas.read_pickle(file_name)
        elif '.txt' in file_name:
            self.csv = pandas.read_csv(file_name)
        pandas.options.display.max_rows = len(self.csv)
        #if

    def centerWindow(self):
        w = 610
        h = 60
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

def main():
    root = Tk()
    ex = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()

