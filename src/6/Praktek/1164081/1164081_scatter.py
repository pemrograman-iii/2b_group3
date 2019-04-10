from matplotlib import pyplot as plt

def scatter():

    x = [1,1.1,1.2,1.3,1.4,1.5,1.6]
    y = [5,5.1,5.2,5.3,5.4,5.5,5.6]
 
    x1=[8,8.5,9,9.5,10,10.5,11]
    y1=[3,3.5,3.7,4,4.5,5,5.2]
    
    for i in range(1, 3):
        plt.subplot(2,2,i)
        plt.scatter(x,y, label='Contoh 1',color='y')
        plt.scatter(x1,y1,label='Contoh 2',color='c')
        plt.xlabel('Contoh 2')
        plt.ylabel('Contoh 1')
        plt.title('Grafik Scatter Plot')
        plt.legend()
        plt.subplots_adjust(wspace=1.1, hspace=.7)
    
    plt.show()
scatter()
    