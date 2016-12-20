import numpy as np #importing numpy with np as "class"
import matplotlib.pyplot as plt #importing matplot as plt

#graphs the sin function with two different parameters
def showSin():
    x = np.linspace(0,2*np.pi,100)
    plt.plot(x, np.sin(x), x, np.sin(2*x))
    plt.show()

#colormapped scatter plot
def showScatter():    
    x = np.random.rand(200)
    y = np.random.rand(200)
    size = np.random.rand(200) * 30
    color = np.random.rand(200)
    plt.scatter(x, y, size, color)
    plt.colorbar()
    plt.show()

def main():
    showScatter()

main()