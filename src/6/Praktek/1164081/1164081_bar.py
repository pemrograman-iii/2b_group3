from matplotlib import pyplot as plt

def bar():
    
    for i in range(1, 3):
        plt.subplot(2,1,i)
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
        plt.subplots_adjust(wspace=1.1, hspace=.7)
        plt.show()
        
bar()
