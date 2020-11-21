from tkinter import *
import csv
import pickle
import pandas
from tkinter import filedialog as fd
import tkinter.ttk as ttk
#загрузка во внутреннее  потом функции потом результат
#2 нижние кнопки - загрузить(файловый менеджер), сохранить в файл(-csv,pickle,txt)
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


        #self.text1 = Entry(self, height=15, width=15, font='Arial 14', wrap=WORD)

        self.entry = Label(self, width=50, height=50)
        #self.text1.grid(row=0, columnspan=4)
        self.get_rows_by_number = Button(self, text='get_rows_by_number', command=self.get_rows_by_number, width=16)
        self.get_rows_by_number.grid(row=1, column=0)
        self.get_rows_by_index = Button(self, text='get_rows_by_index', width=16)
        self.get_rows_by_index.grid(row=1, column=1)
        self.get_column_types = Button(self, text='get_column_types', width=16)
        self.get_column_types.grid(row=1, column=2)
        self.set_column_types = Button(self, text='set_column_types', width=16)
        self.set_column_types.grid(row=1, column=3)
        self.get_values = Button(self, text='get_values', width=16)
        self.get_values.grid(row=2, column=3)
        self.set_values = Button(self, text='set_values', width=16)
        self.set_values.grid(row=2, column=2)




        self.print_table = Button(self, command=self.print_table, text='print_table', width=16)
        self.print_table.grid(row=2, column=1)
        self.open_file = Button(self, command=self.open_file,text='открыть', width=8)
        self.open_file.grid(row=2, column=0)
        self.pack()
       #self.get_rows_by_number.bind('<Button-1>', self.get_rows_by_number)
        self.get_rows_by_index.bind('<Button-1>', self.get_rows_by_index)
        self.get_column_types.bind('<Button-1>', self.get_column_types)
        self.set_column_types.bind('<Button-1>', self.set_column_types)
        self.get_values.bind('<Button-1>', self.get_values)
        self.set_values.bind('<Button-1>', self.set_values)
        buttonExample = Button(self, text="Open",command=self.print_table)
        #self.print_table.bind('<Button-1>', self.print_table)
        #self.open_file.comman('<Button-1>', self.open_file)

        #

    def get_rows_by_number1(self):


        frame = self.csv
        start = int(self.start_arg_entry.get())
        stop = int(self.stop_arg_entry.get())
        copy_table = bool(self.copy_table_entry.get())
        copy_table = True
        output_directory = r'C:\Users\79268\Dev\csvs\output.csv'
        if copy_table == True:
            text1 = frame[start:stop + 1]
        elif copy_table == False:
            text1 = frame[start:stop + 1]

        label = Label(self.newWindow, text=text1)
        label.grid(row=1)

    def button_save(self):
        files = [('All Files', '*.*'),

                 ('CSV Files', '*.csv'),

                 ('Text Document', '*.txt')]

        file = fd.asksaveasfile(filetypes=files, defaultextension=files)



    def get_rows_by_number(self):

        self.newWindow = Toplevel(self)
        start_type = IntVar()
        stop_type = IntVar()
        copy_type = BooleanVar()

        start_arg_label = Label(self.newWindow,text="start:")
        stop_arg_label = Label(self.newWindow, text="stop:")
        copy_table_label = Label(self.newWindow, text='copy_table:')

        start_arg_label.grid(row=0, column=0, sticky="e")
        stop_arg_label.grid(row=0, column=2, sticky="e")
        copy_table_label.grid(row=0, column=4, sticky="e")

        self.start_arg_entry = Entry(self.newWindow, textvariable=start_type)
        self.stop_arg_entry = Entry(self.newWindow, textvariable=stop_type)
        self.copy_table_entry = Entry(self.newWindow, textvariable=copy_type)

        self.start_arg_entry.grid(row=0,column=1, padx=5, pady=5)
        self.stop_arg_entry.grid(row=0,column=3, padx=5, pady=5)
        self.copy_table_entry.grid(row=0,column=5, padx=5, pady=5)

        button = Button(self.newWindow, command=self.get_rows_by_number1, text='OK!', width=3)
        button_save = Button(self.newWindow, command=self.button_save, text='SAVE', width=5)
        button.grid(row=0, column=6, padx=5, pady=5)
        button_save.grid(row=0, column=7, padx=5, pady=5)



        #labelForm = Entry(newWindow)
        #labelExample = Label(newWindow, text=self.text1)
        self.mainloop()


    def get_rows_by_index(self, event):
        print('get_rows_by_index')


    def get_column_types(self, event):
        print('get_column_types')


    def set_column_types(self, event):
        print('set_column_types')


    def get_values(self, event):
        print('get_values')


    def set_values(self, event):
        print('set_values')


    def print_table(self):
        print('print_table')
        newWindow = Toplevel(self)


        labelExample = Label(newWindow, text=self.csv)
        labelExample.pack()

    def open_file(self):
        file_name = fd.askopenfilename()


        self.csv = pandas.read_csv(file_name)
        pandas.options.display.max_rows = len(self.csv)



    def package(self, var):
        pass



    def centerWindow(self):
        w = 800
        h = 800
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



