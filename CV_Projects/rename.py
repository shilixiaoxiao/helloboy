# -*- coding: utf-8 -*-
import os
dir = input(r'D:\data\20190722_无屏第一批量产CA50_太平洋')
print(dir)
for root, dirs, files in os.walk(dir):
    print(root)
    print(dirs)
    print(files)
