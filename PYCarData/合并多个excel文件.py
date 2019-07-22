#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 15:56:44 2019

@author: lixin
"""

import os

import pandas as pd

import numpy as np

dir_path = "/Users/lixingongsi/Desktop/2/"
filename_excel = []
frames = []
for  root, dirs, files in os.walk(dir_path):
    for file in files:
        if ".xlsx" in file:
            print(file)
            filename_excel.append(os.path.join(root,file))

            df = pd.read_excel(os.path.join(root,file))
            frames.append(df)

print(filename_excel)

#合并多个文件
result = pd.concat(frames)

result.head()

result.shape
result.to_excel("/Users/lixingongsi/Desktop/2/ceshi.xlsx",index=False)
#result.to_csv("/Users/lixingongsi/Desktop/1/ceshi.csv",sep = ",",index=False)