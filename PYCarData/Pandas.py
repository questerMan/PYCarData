#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 15:01:30 2019

@author: lixin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
s1 = pd.Series(["a","b","c"])
print(s1)

s2 = pd.Series(["a","b","c"],index = ["1","2","3"])

print(s2)

df1 = pd.DataFrame([["a","b","c"],["aa","bb","cc"]])

print(df1)

df2 = pd.DataFrame([["a","b","c"],["aa","bb","cc"]],
                   columns = ["第一列","第二列","第三列"],
                   index = ["第一行","第二行"])
print(df2)

data = {"大写":["A","B","C"],"小写":["a","b","c"]}
df3 = pd.DataFrame(data)
print(df3)

print(df2.index)