# In[1]: Import matplotlib
from matplotlib import pyplot as plt

# In[2]: No 2

x=[2,2,3]
y=[3,2,1]

plt.plot(x,y)

plt.show()

# In[2]: Fungs Bar

from matplotlib import pyplot as plt

plt.bar([2013.7,2014.7,2015.7,2016.7,2017.7,2018.7],[36000,40000,35000,37000,42000,40000],
label="Cengek",color='y',width=.3)
plt.bar([2013,2014,2015,2016,2017,2018],[42000,38000,39500,36000,38500,40000],
label="Cabe Merah",color='r',width=.3)
plt.bar([2013.3,2014.3,2015.3,2016.3,2017.3,2018.3],[42000,40000,41000,41500,42500,43000],
label="Cabe Hijau",color='g',width=.3)
plt.legend()
plt.xlabel('Tahun')
plt.ylabel('Harga /kg')
plt.title('Harga Cabe Dari Tahun Ke Tahun')
plt.show()

# In[3]: Fungsi Histogram

import matplotlib.pyplot as plt

jumlah = [10,10,20,30,22,100,25,40,60,70,80,90,99,43,12,12,12]
angka = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(jumlah, angka, histtype='bar', rwidth=0.8)
plt.xlabel('Angka')
plt.ylabel('Jumlah Angka Yang Keluar')
plt.title('Grafik Histogram')
plt.show()

# In[4]: Fungsi Scatter Plot

import matplotlib.pyplot as plt
x = [1,1.5,2,2.5,3,3.5,3.6]
y = [7.5,8,8.5,9,9.5,10,10.5]
 
x1=[8,8.5,9,9.5,10,10.5,11]
y1=[3,3.5,3.7,4,4.5,5,5.2]
 
plt.scatter(x,y, label='Tabungan 1',color='y')
plt.scatter(x1,y1,label='Tabungan 2',color='c')
plt.xlabel('Tabungan 2')
plt.ylabel('Tabungan 1')
plt.title('Grafik Scatter Plot')
plt.legend()
plt.show()

# In[5]: Fungsi Area plot

import matplotlib.pyplot as plt
Donwload_Game = [1,2,3,4,5]
  
Dota =[1,2,3,4,5]
ML = [5,4,3,2,1]
FF =[2,1,4,5,3]
PUBG = [3,5,4,1,2]
  
plt.plot([],[],color='r', label='Dota', linewidth=5)
plt.plot([],[],color='b', label='Mobile Legend', linewidth=5)
plt.plot([],[],color='g', label='Free Fire', linewidth=5)
plt.plot([],[],color='y', label='PUBG', linewidth=5)
  
plt.stackplot(Donwload_Game,Dota,ML,FF,PUBG, colors=['r','b','g','y'])
  
plt.xlabel('Sumbu x')
plt.ylabel('Sumbu y')
plt.title('Area Plot')
plt.legend()
plt.show()

# In[6]: Fungsi Pie Plot

import matplotlib.pyplot as plt
 
Donwload_Game = [1,2,3,4,5]
  
Dota =[1,2,3,4,5]
ML = [5,4,3,2,1]
FF =[2,1,4,5,3]
PUBG = [3,5,4,1,2]
potong = [3,1,1,12]
Game = ['Dota','Mobile Legend','Free Fire','PUBG']
kolom = ['r','b','g','y']
 
plt.pie(potong,
  labels=Game,
  colors=kolom,
  startangle=90,
  shadow= True,
  explode=(0,0,0.2,0),
  autopct='%1.1f%%')
 
plt.title('Pie Plot')
plt.show()

# In[7]: Fungsi Line

from matplotlib import pyplot as plt
 
y = [1,2,3,4,5,6]
x = [1,2,3,4,5,6]
plt.plot(x,y)
plt.title('Line')
plt.ylabel('Sumbu Y')
plt.xlabel('Sumbu X')
plt.show()

# In[8]: No 4

from matplotlib import pyplot as plt

x = [1,2,3,4,5,6]
y = [11,12,13,14,15,16]
x2 = [1,2,3,4,5,6]
y2 = [17,18,19,20,21,22]
plt.plot(x,y,'b',label='Label 1', linewidth=1)
plt.plot(x2,y2,'r',label='Label 2',linewidth=1)
plt.title('Penggunaan Legend Dan Label')
plt.ylabel('Sumbu Y')
plt.xlabel('Sumbu X')
plt.legend()
plt.grid(True,color='g')
plt.show()

# In[8]: No 5

import numpy as np
import matplotlib.pyplot as plt
 
t = np.arange(0.0, 9.0, 1)
s = [2,4,6,8,12,14,16,18,20]
 
for i in range(1, 5):
    plt.subplot(3,3,i)
    plt.xticks([]), plt.yticks([])
    plt.title('subplot(1, '+str(i)+')')
    plt.plot(t,s,'-y')
 
plt.show()

# In[5]: No 7

import matplotlib.pyplot as plt

jumlah = [10,10,20,30,22,100,25,40,60,70,80,90,99,43,12,12,12]
angka = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(jumlah, angka, histtype='bar', rwidth=0.8)
plt.xlabel('Angka')
plt.ylabel('Jumlah Angka Yang Keluar')
plt.title('Grafik Histogram')
plt.show()

from matplotlib import pyplot as plt

# In[06]:

bar = __import__('1164089_bar')
scat = __import__('1164089_scatter')
pie = __import__('1164089_pie')
plot = __import__('1164089_plot')

bar.bar()
scat.scatter()
pie.pie()
plot.plot()

# In[07] Fungsi TryExcept
def tryExceptError():
    try:
        b=[2,2,3]
        a=[3,2,1]        
        plt.plot(x,y)        
        plt.show()        
    except NameError:
        print("Tidak Ada Variabel Tersebut")
        
tryExceptError()