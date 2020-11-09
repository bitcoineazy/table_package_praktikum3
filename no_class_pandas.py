import pandas


def save_table_csv():
    file = r'C:\Users\79268\Dev\csvs\governors_county.csv'
    election = pandas.read_csv(file)
    #print(election)
    election_modified = election.set_index('state')
    print(election_modified)
save_table_csv()