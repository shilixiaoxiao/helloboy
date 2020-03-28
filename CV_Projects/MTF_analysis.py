# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import re

path = "D:\\data\\20200310_CA50_500套量产\\data"
listDir = os.listdir(path)
#print(listDir)

#outPutData = open(path + "\\Ghost_result\\" + "Ghost.txt",'w')
number = 0
MTF_20_center = []
MTF_20_corner = []
for dir in listDir:
    if re.match(r'\d+'+"_multi",dir):
        Excel_path = path +"\\"+ dir
        print(Excel_path)
        number = number + 1
        data =pd.read_csv(Excel_path,error_bad_lines=False,sep=",",encoding='utf-8-sig',header = None,index_col = False,
                          names=['1','2','3','4','5','6','7','8','9','10','11'])
        df = pd.DataFrame(data)
        #print(df)
        #headers = pd.read_csv(Excel_path,  nrows=0).columns.tolist()
        #print(headers)
        #print(data['4'])
        list = df.loc[44:55,'11']
        sum_center = 0
        sum_corner = 0
        for i in range(4):
            sum_center = float(list[i+44])+sum_center
        for j in range(8):
            sum_corner = float(list[j+48])+sum_corner
        avg_center = round(sum_center/4,4)
        avg_corner = round(sum_corner/8,4)
        #print(avg)
        MTF_20_center.append(avg_center)
        MTF_20_corner.append(avg_corner)
        #data = pd.read_excel("")
        #outPutData.write( dir + ":\n")

print(number)
print(MTF_20_center)
print(MTF_20_corner)
MTF_20_center_mean =round(np.mean(MTF_20_center),2)
MTF_20_corner_mean =round(np.mean(MTF_20_corner),2)
print(MTF_20_center_mean)
print(MTF_20_corner_mean)

fig = plt.figure()
# 将画图窗口分成1行1列，选择第一块区域作子图
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
# 设置标题
ax1.set_title('MTF_Center Analysis')
# 设置横坐标名称
ax1.set_xlabel('index')
# 设置纵坐标名称
ax1.set_ylabel('MTF@20lp')

ax2.set_title('MTF_Corter Analysis')
# 设置横坐标名称
ax2.set_xlabel('index')
# 设置纵坐标名称
ax2.set_ylabel('MTF@20lp')
# 画散点图
y1 = np.array(MTF_20_center)
x1 = np.arange(0, y1.size)
ax1.scatter( x1, y1,s=10,  c='g', marker='.')

y2 = np.array(MTF_20_corner)
x2 = np.arange(0, y2.size)
ax2.scatter( x2, y2, s=10, c='g', marker='.')
# 画直线图

ax1.axhline(y=MTF_20_center_mean, c='b', ls='--') #添加水平直线
ax2.axhline(y=MTF_20_corner_mean, c='b', ls='--') #添加水平直线
ax2.axhline(y=MTF_20_corner_mean, c='b', ls='--') #添加水平直线


#ax2.plot(x2, MTF_20_corner_mean, c='b', ls='--')

# 调整横坐标的上下界
#plt.xlim(xmax=1200, xmin=-100)

ax1.grid(True)
ax2.grid(True)
#plt.text(10,20,"mean:"+ str(MTF_20_center_mean),color = "r", size = 15, alpha = 0.2,bbox = dict(facecolor = "r", alpha = 0.2))
plt.show()
# 显示




'''data = pd.read_table("D:\\data\\20200310_CA50_500套量产\\txt\\OutputData_MP.txt", delim_whitespace=True, header=0,
                     encoding='gb2312')
df = pd.DataFrame(data, columns=["Center(X)", "Center(Y)"])'''
