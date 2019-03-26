# In[01]: Melakukan import pada library pandas 
import pandas as pd

# In[02]: Membaca file csv dengan mode list
def ReadModelListPd():
    df = pd.read_csv('1164081.csv')
    print(df)

# In[02]: membaca file csv dengan mode dictionary
def ReadModelDictPd():
    df = pd.read_csv('1164081.csv')
    dt = pd.DataFrame.from_dict(df)
    print(dt)

# In[03]: Mengubah format tanggal menjadi standar DataFrame
def MengubahFormat():
    df = pd.read_csv('1164081.csv', parse_dates=['Tanggal Daftar'])
    print(df)


# In[04]: Mengubah Index Kolom 
def MengubahIndexKolom():
    df = pd.read_csv('1164081.csv')
    df.index = ['Row_1', 'Row_2']
    print(df)
# In[05]: Mengubah atribut 
def MengubahAtribut():
    df = pd.read_csv('1164081.csv')
    df.columns =['Colom_1', 'Colom_2', 'Colom_3', 'Colom_4'] 
    print(df)

# In[06]:
def WritePd():
    df = pd.read_csv('1164081.csv', 
            index_col='Name', 
            parse_dates=['Date'],
            header=0, 
            names=['Name', 'Class', 'Date', 'Region'])
    df.to_csv('1164081_M.csv')

# In[07]:
def TryExcept():
    try:
        df = pd.read_csv('1164081.csv')
        print(df)
    except SyntaxError:
        print("Kesalahan Dalam Penulisan Atribute")