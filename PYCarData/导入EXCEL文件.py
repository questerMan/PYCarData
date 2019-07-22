#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 15:17:11 2019

@author: lixin
"""

import pandas as pd

df = pd.read_excel("/Users/lixingongsi/Desktop/1/订单.xlsx",
                   sep = " ",
                   header = 2)

print(df.read())