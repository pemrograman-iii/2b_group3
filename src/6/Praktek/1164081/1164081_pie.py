from matplotlib import pyplot as plt

def pie():
    
    potong = [4,4,4,4]
    Game = ['Dota','Mobile Legend','Free Fire','PUBG']
    kolom = ['r','b','g','y']
    
    for i in range(1, 3):
        plt.subplot(2,2,i)
        plt.pie(potong,
        labels=Game,
        colors=kolom,
        startangle=90,
        shadow= True,
        explode=(0,0,0,0.2),
        autopct='%1.1f%%')        
        plt.title('Pie Plot')
        plt.subplots_adjust(hspace=.4)
    
    plt.show()
pie()
    