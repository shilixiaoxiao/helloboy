# -*- coding: utf-8 -*-

import pandas as pd
import os

list = os.listdir(r"D:\20190722_无屏第一批量产CA50_太平洋\第7周")
result = []
for i in list:
    result.append(i)
print(result)
for i in result:
    print(i)
