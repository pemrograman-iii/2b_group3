from matplotlib import pyplot as plt

def plot():
    
    x = [1,2,3,4,5,6]
    y = [11,12,13,14,15,16]
    x2 = [1,2,3,4,5,6]
    y2 = [17,18,19,20,21,22]
    
    for i in range(1, 3):
        plt.subplot(2,2,i)
        plt.plot(x,y,'b',label='Label 1', linewidth=1)
        plt.plot(x2,y2,'r',label='Label 2',linewidth=1)
        plt.title('Fungsi Plot')
        plt.ylabel('Sumbu Y')
        plt.xlabel('Sumbu X')
        plt.legend()
        plt.grid(True,color='g')
        plt.subplots_adjust(wspace=.4, hspace=.7)
    
    plt.show()
plot()
    
