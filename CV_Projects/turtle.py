# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def plotLine():
    fig = plt.figure()
    x = linspace(-2, 2)

    plt.subplot(111)
    x = np.arange(-960, 960, 1)
    plt.plot(x,0.1*x)
    left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
    ax1 = fig.add_axes([left, bottom, width, height])
    ax1.plot(x, y, 'r')
    ax1.set_title('area1')

    print(x)
    y1 = 0.067*x
    y2 = -0.067*x
    plt.figure(figsize=(1920,1080),dpi=1)
    plt.subplots_adjust(left=0,right=1, bottom=0, top=1)
    plt.plot(x,y1,y2,linewidth=150)
    plt.axis('off')
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)
    plt.savefig('a.png',format='png',  dpi=1, pad_inches=0)
    plt.show()
    plt.close()




    plt.plot(x, y)
    plt.show()
def plotTriangle():
    x = [1,3,1,1]
    y = [1,1,3,1]
    plt.figure(figsize=(100,100),dpi=1)
    plt.plot(x,y,linewidth=150)
    plt.axis('off')
    plt.savefig('b.png',dpi=1)
    plt.show()
    plt.close()
def plotSquare():
    x = [1,3,3,1,1]
    y = [1,1,3,3,1]
    plt.figure(figsize=(100,100),dpi=1)
    plt.plot(x,y,linewidth=150)
    plt.axis('off')
    plt.savefig('c.png',dpi=1)
    plt.show()
    plt.close()
plotLine()
plotTriangle()
plotSquare()



