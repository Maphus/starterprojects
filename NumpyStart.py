import numpy as np #importing numpy with np as "class"
import matplotlib.pyplot as plt #importing matplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.misc import ascent

#graphs the sin function with two different parameters
def showSin():
    x = np.linspace(0,2*np.pi,100)
    plt.plot(x, np.sin(x), x, np.sin(2*x))
    plt.show()

#simple scatter plot
def showSScatter():
    x = np.linspace(0, 2*np.pi, 50)
    y = np.sin(x)
    plt.scatter(x, y)
    plt.grid()
    plt.show()

#colormapped scatter plot
def showCMScatter():    
    x = np.random.rand(200)
    y = np.random.rand(200)
    size = np.random.rand(200) * 30
    color = np.random.rand(200)
    plt.scatter(x, y, size, color)
    plt.colorbar()
    plt.show()

#show picture with differnt color maps
def showPic():
    img = ascent()
    plt.imshow(img, extent=[-25,25,-25,25], cmap = plt.cm.bone)
    plt.colorbar()
    plt.show()

#show histogram
def showHist():
    plt.hist(np.random.randn(1000), 30)
    plt.show()

def showPara():
    t = np.linspace(0,30,1000)
    x, y, z = [t*np.cos(t), t*np.sin(t), t]
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(x, y, z)
    plt.show()

def show3DSurface():
    x, y = np.mgrid[-5:5:35j, 0:10:35j]
    z = x*np.sin(x)*np.cos(.25*y)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap = plt.cm.jet)
    plt.show()

def main():
    showPara()

main()