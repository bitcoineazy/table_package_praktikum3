from tkinter import *
import csv
import pickle
import pandas
from tkinter import filedialog as fd
from tabulate import tabulate
from IPython.display import HTML, display
import tkinter.ttk as ttk
#загрузка во внутреннее  потом функции потом результат
#2 нижние кнопки - загрузить(файловый менеджер), сохранить в файл(-csv,pickle,txt)
pandas.options.display.expand_frame_repr = False
import io

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.parent.title("Parser")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        self.initUI()

    def initUI(self):


        #self.text1 = Entry(self, height=15, width=15, font='Arial 14', wrap=WORD)

        self.entry = Label(self, width=50, height=50)
        #self.text1.grid(row=0, columnspan=4)
        self.get_rows_by_number = Button(self, text='get_rows_by_number', command=self.get_rows_by_number, width=16)
        self.get_rows_by_number.grid(row=1, column=0)
        self.get_rows_by_index = Button(self, text='get_rows_by_index', command=self.get_rows_by_index , width=16)
        self.get_rows_by_index.grid(row=1, column=1)
        self.get_column_types = Button(self, text='get_column_types',command=self.get_column_types , width=16)
        self.get_column_types.grid(row=1, column=2)
        self.set_column_types = Button(self, text='set_column_types',command=self.set_column_types, width=16)
        self.set_column_types.grid(row=1, column=3)
        self.get_values = Button(self, text='get_values', width=16)
        self.get_values.grid(row=2, column=3)
        self.set_values = Button(self, text='set_values', width=16)
        self.set_values.grid(row=2, column=2)




        self.print_table = Button(self, command=self.print_table, text='print_table', width=16)
        self.print_table.grid(row=2, column=1)
        self.open_file = Button(self, command=self.open_file,text='открыть', width=16)
        self.open_file.grid(row=2, column=0)
        self.pack()
       #self.get_rows_by_number.bind('<Button-1>', self.get_rows_by_number)
        #self.get_rows_by_index.bind('<Button-1>', self.get_rows_by_index)
        #self.get_column_types.bind('<Button-1>', self.get_column_types)
        #self.set_column_types.bind('<Button-1>', self.set_column_types)
        self.get_values.bind('<Button-1>', self.get_values)
        self.set_values.bind('<Button-1>', self.set_values)
        buttonExample = Button(self, text="Open",command=self.print_table, width=16)
        #self.print_table.bind('<Button-1>', self.print_table)
        #self.open_file.comman('<Button-1>', self.open_file)


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

    def button_save(self):
        files = [('All Files', '*.*'),
                 ('CSV Files', '*.csv'),
                 ('Text Document', '*.txt')]
        file = fd.asksaveasfile(filetypes=files, defaultextension=files)
        #file.write(str(self.csv))
        self.csv.to_csv(file)

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



        #labelForm = Entry(newWindow)
        #labelExample = Label(newWindow, text=self.text1)
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

        '''key = val.values()
        if copy_table == True:
            frame = pandas.read_csv(directory)
            print(pandas.concat([frame[key]], ignore_index=True))
        elif copy_table == False:
            frame = pandas.read_csv(directory)
            frame[key].to_csv(output_directory, index=False)'''


    '''def get_column_types_pandas(self):
        directory = self.file
        frame = pandas.read_csv(directory)
        print(frame.info(null_counts=False, memory_usage=False))
        '''
    def get_column_types(self):
        #by_number - built-in
        print('get_column_types')
        self.column_types = Toplevel(self)


        buffer = io.StringIO()
        self.csv.info(buf=buffer, null_counts=False, memory_usage=False)
        text = buffer.getvalue()
        #text = self.csv.info(null_counts=False, memory_usage=False)
        label = Text(self.column_types)
        label.insert(1.0, text)
        label.grid(row=2)


        '''values_arg_label = Label(self.by_index, text="values:")
        copy_table_label = Label(self.by_index, text='copy_table:')

        values_arg_label.grid(row=0, column=0, sticky="w")
        copy_table_label.grid(row=0, column=2, sticky="w")

        self.values_arg_entry = Entry(self.by_index)
        self.copy_table_entry = Entry(self.by_index)

        self.values_arg_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.copy_table_entry.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        button_ok = Button(self.by_index, command=self.get_rows_by_index_pandas, text='OK!', width=3)
        button_save = Button(self.by_index, command=self.button_save, text='SAVE', width=5)
        button_ok.grid(row=0, column=4, padx=5, pady=5, sticky="w")
        button_save.grid(row=0, column=5, padx=5, pady=5, sticky="w")'''


    def set_column_types_pandas(self):
        types_dict = self.set_entry.get()
        buffer = io.StringIO()
        '''self.csv.info(buf=buffer, null_counts=False, memory_usage=False)
        text = buffer.getvalue()'''
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

    def get_values(self, event):
        print('get_values')


    def set_values(self, event):
        print('set_values')


    def print_table(self):
        print('print_table')
        newWindow = Toplevel(self)

        frame = self.csv
        columns = frame.columns
        labelExample = Text(newWindow, width=150)
        labelExample.insert(1.0, tabulate(frame, headers=columns))
        labelExample.grid(row=2)

    def open_file(self):
        file_name = fd.askopenfilename()
        self.csv = pandas.read_csv(file_name)
        pandas.options.display.max_rows = len(self.csv)



    def package(self, var):
        pass



    def centerWindow(self):
        w = 488
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



