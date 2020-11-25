import pandas


directory = r'C:\Users\79268\Dev\csvs\governors_county.csv'
frame = pandas.read_csv(directory)
textz = frame.info(null_counts=False, memory_usage=False)
string = str(textz)
print(string)
