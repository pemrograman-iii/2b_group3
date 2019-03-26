import pandas
df = pandas.read_csv('4.csv',index_col='Name',parse_dates=['Hire Date'])
print(df)
