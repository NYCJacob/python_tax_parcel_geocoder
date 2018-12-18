import pandas as pd


# create new csv file to save data
new_csv_file= open('new_marbletown_agass', 'a')

# process original csv file
################################################# this range throwing error
# df_csv = pd.read_csv('tmarble_export.csv', header=0, skiprows=range(1, 3073), nrows=27)
mtagass_csv = pd.read_csv('marbletown_agass.csv')
for row in mtagass_csv.itertuples(index=True, name='Pandas'):
    row_sbl= getattr(row, "SBL")
    if row_sbl:
        sblist= row_sbl.split("-")
        print(sblist)
        sblist[0]


# close open file stream
new_csv_file.close()