# -*- coding: utf-8 -*-

import os
import pandas as pd

filepath = r"D:\data\20190722_无屏第一批量产CA50_太平洋\20190927_第一-三次旋转NG遗留.xlsx"
df = pd.read_excel(filepath,header=0,usecols=[3,8])


list_new = []
for item in df["QR Code"]:
  list_new.append(item)
for item in df["Matched module"]:
  list_new.append(item)
print (list_new)
searchList = []
for i in list_new:
     searchList.append('0' + str(i) + '_multi.xlsx')

print(searchList)

inputList = input(r'D:\data\20190722_无屏第一批量产CA50_太平洋')



