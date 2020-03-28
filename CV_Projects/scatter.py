# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

# 定义画散点图的函数
'''    
    :param n: 点的数量，整数
    :param s:点的大小，整数
    :return: None
'''

    # 加载数据
    #data = np.loadtxt('D:\\data\\20200310_CA50_500套量产\\txt\\OutputData_MP.txt',skiprows=1 ,encoding='utf-8', delimiter=' ')

'''    fr = open("D:\\data\\20200310_CA50_500套量产\\txt\\OutputData_MP.txt", 'r')
    # frw = open("Train_1.csv", 'w')

    line = fr.readlines()
    for L in line:
        string = L.strip("\n").split(" ")
        a = np.float64(string[0])
        b = np.float64(string[1])
        c = np.float64(string[2])
        d = np.float64(string[3])
'''

def draw_scatter(v_pixel,h_pixel):
    data = pd.read_table("D:\\data\\20200310_CA50_500套量产\\txt\\OutputData_2MP.txt",delim_whitespace=True ,header= 0,encoding='gb2312')
    df = pd.DataFrame(data,columns=["QRcode","Center(X)","Center(Y)","Rotation(deg)"])
    # 通过切片获取横坐标x1
    #print(df.info())
    df = df.apply(pd.to_numeric, errors='coerce')#将dataframe 的object转换为float 类型
    #print(df.info())

    #添加左右眼坐标散点颜色不同，根据QRcode的尾数
    #同时添加Rotation的散点图
    avg_x = np.mean(df["Center(X)"])
    avg_y = np.mean(df["Center(Y)"])
    up_x = avg_x + v_pixel*0.335/100
    down_x = avg_x - v_pixel*0.335/100
    up_y = avg_y + h_pixel*0.335/100
    down_y = avg_y - h_pixel*0.335/100
    up_x2 = avg_x + v_pixel*0.67/100
    down_x2 = avg_x - v_pixel*0.67/100
    up_y2 = avg_y + h_pixel*0.67/100
    down_y2 = avg_y - h_pixel*0.67/100

    #fig = plt.figure()
    #ax = fig.add_subplot(1, 1, 1)
    #for i in df['QRcode']:
     #   if i%2 != 0:
     #       df_left = df[i]
    df_left = df.loc[df['QRcode']%2 == 0]
    df_right = df.loc[df['QRcode']%2 != 0]
    #print(df_left.info())
    #print(df_right.info())
    ax = df_left.plot.scatter(x = "Center(X)",y = "Center(Y)")
    df_right.plot.scatter(x = "Center(X)",y = "Center(Y)",ax = ax, c = '#DC143C' )

    #df.plot.scatter(x = "Center(X)",y = "Center(Y)")
    plt.axhline(y=avg_y, c='b', ls='--')
    plt.axhline(y=up_y, c='g', ls='--')
    plt.axhline(y=up_y2, c='r', ls='--')
    plt.axhline(y=down_y, c='g', ls='--')
    plt.axhline(y=down_y2, c='r', ls='--')

    plt.axvline(x=avg_x, c='b', ls='--')
    plt.axvline(x=up_x, c='g', ls='--')
    plt.axvline(x=up_x2, c='r', ls='--')
    plt.axvline(x=down_x, c='g', ls='--')
    plt.axvline(x=down_x2, c='r', ls='--')

    plt.show()
    plt.pause(1)
    plt.close()
'''    x1 = df["Center(X)"]
    print(x1)
    # 通过切片获取纵坐标R
    y1 = df["Center(Y)"]
    print(y1)

    fig = plt.figure()
    # 将画图窗口分成1行1列，选择第一块区域作子图
    ax1 = fig.add_subplot(1, 1, 1)
    # 设置标题
    ax1.set_title('Result Analysis')
    # 设置横坐标名称
    ax1.set_xlabel('X')
    # 设置纵坐标名称
    ax1.set_ylabel('Y')
    # 画散点图
    ax1.scatter(x1, y1, s=s, c='k', marker='.')
    # 画直线图
    #ax1.plot(x2, y2, c='b', ls='--')
    # 调整横坐标的上下界
    #plt.xlim(xmax=5, xmin=0)
    # 显示
    plt.show()'''


# 主模块
if __name__ == "__main__":
    # 运行
    v_pixel = 2154.51
    h_pixel = 1206.34
    draw_scatter(v_pixel,h_pixel)
