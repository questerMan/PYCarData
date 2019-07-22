#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 11:28:36 2019

@author: lixin
"""

import pandas as pd
import numpy as np
import os

#定义生成的文件名
collectName = 'GFcollectData.xlsx'

#定义文件路径
path1 = '/Users/lixingongsi/Desktop/PYCarData/广丰周数据汇总/'.strip()


#遍历读取某个文件夹下的文件信息
def getData(path):
    pathTmp = ''
    dataList = []
    fileList = os.listdir(path)   #获取path目录下的所以文件
    for fileName in fileList:
        pathTmp = os.path.join(path,fileName)  #获取path与fileName组合后的路径
        if '.xlsx' == fileName[-5:]:
            if fileName == collectName:
                 print("已删除===生成的collectData.xlsx文件====已删除")
                 os.remove(pathTmp)
            else:
                #print(pathTmp)
                dataFD = pd.read_excel(pathTmp,sep=" ",header = 0)
                dataList.append(dataFD)
    return dataList

def res_dataIndex(dataFrame):
    dataFrame.rename(columns={'Unnamed: 14':'月天数'}, inplace = True)
    #删除空行
    dataFrame.dropna(inplace=True)
    #删除重复行
    dataFrame.drop_duplicates(inplace=True)
    #合并数据后进行index重新排序，以免index值重复
    dataFrame = dataFrame.reset_index(drop = True)
    
    return dataFrame


#合并“/Users/lixingongsi/Desktop/运营数据/”下.xlsx的Excel表格 
collect_GFDataFrame = res_dataIndex(pd.concat(getData(path1),axis=0))

collect_GFDataFrame.to_excel('/Users/lixingongsi/Desktop/PYCarData/广丰周数据汇总/'+collectName)

df = pd.read_excel('/Users/lixingongsi/Desktop/PYCarData/广丰周数据汇总/'+collectName)
 
print(df.info())
