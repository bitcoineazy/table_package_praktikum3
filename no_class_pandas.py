import pandas


def save_table_csv(**columns):
    file = r'C:\Users\79268\Dev\csvs\governors_county.csv'
    frame = pandas.read_csv(file)
    #equality = frame['percent'].eq(['percent'])
    equality2 = frame['percent'] == frame['percent']
    frame['equally'] = equality2
    print(frame)

save_table_csv(column1='percent', column2='percent')