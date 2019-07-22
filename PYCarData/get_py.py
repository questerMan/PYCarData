#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 00:14:51 2019

@author: lixin
"""
import pandas as pd
import numpy as np
import os

'''
获取指定目录及其子目录下的py文件路径说明：l用于存储找到的py文件路径  get_py函数，递归查找并存储py文件路径于l
'''
def delegate_DataFrame(dataFrame,qName="取车时间",hName='还车时间',xName='下单日期'):
    #删除错误订单，即取车时间大于还车时间的订单
    for index,row in dataFrame.iterrows():

        if str(row[hName]) != 'NaT' and str(row[qName]) != 'NaT':
            interval1 = np.timedelta64(row[hName]-row[qName],'D').astype(int)
            if interval1<0:
                dataFrame.drop([index],inplace=True)  #删除改变内存inplace=True
                continue
        '''
        elif str(row[qName]) != 'NaT':#补录订单的下单日期以取车日期为准
            interval2 = np.timedelta64(row[qName]-row[xName],'D').astype(int)
            if interval2<0:
                print("===2=============={}".format(row[qName]))
                
                XD_T=''
                QX_T=''
                XD_T = row[xName]
                QX_T = row[qName]
                dataFrame.at[index,xName] = QX_T
                dataFrame.at[index,qName] = XD_T
                print("+++2+++++++++++++{}".format(row[qName]))
                continue
        '''
  
l = []
dataList = []
def get_py(path,l):
    fileList = os.listdir(path)   #获取path目录下的所以文件
    for fileName in fileList:

        pathTmp = os.path.join(path,fileName)  #获取path与fileName组合后的路径
        if '.xlsx' == fileName[-5:]:
            if fileName == 'intergre.xlsx':
                 print("已删除=======已删除")
                 os.remove(pathTmp)
            else:
                l.append(pathTmp)
                #print(pathTmp)
                dataFD = pd.read_excel(pathTmp,sep=" ",header = 1)
                dataList.append(dataFD)
           
'''
        if os.path.isdir(pathTmp):  #如果是目录  进行递归
            get_py(pathTmp,l)
        elif '.xlsx' == fileName[-5:]:
            l.append(pathTmp)
'''
       
            
path = '/Users/lixingongsi/Desktop/表格整合/'.strip()

get_py(path,l)

#print(l,sep=",")

#合并两个Excel 表格
result = pd.concat(dataList,axis=0)

#删除订单状态为“已取消”的订单
result_Data = result[~result["订单状态"].isin(["已取消"])]


cs = []
for i in range(len(result_Data['订单号'])):
    cs.append('广丰项目')
    
gfxm_dic={
     '店代码':'',
     '店名':result_Data['取车店'],
     '订单号':result_Data['订单号'],
     '下单日期':result_Data['下单日期'],
     '客户':result_Data['客户姓名'],
     '租用开始时间':result_Data['租用开始时间'],
     '租用结束时间':result_Data['租用结束时间'],
     '租用时长':result_Data['租用时长'],
     '车型':result_Data['车型'],
     '车辆':result_Data['车牌号'],
     '费用':'',
     '订单状态':result_Data['订单状态'],
     '订单确认时间':'',
     '取车时间':result_Data['租用开始时间'],
     '取车里程':'',
     '还车时间':result_Data['租用结束时间'],
     '还车里程':'',
     '超里程费用':'',
     '燃油费用':'',
     '套餐优惠费用':'',
     '增值服务费用':'',
     '基础服务费用':'',
     '尊享服务费用':'',
     '超时费用':'',
     '其他费用':'',
     '优惠卷费用':'',
     '其他说明':'',
     '续租全部费用':'',
     '全部费用':result_Data['费用总额'],
     '车辆店代码':'',
     '已付费用':'',
     '已付押金费用':'',
     '订单来源':'',
     '业务员':'',
     '项目':cs,
}

#使用字典创建一个DataFrame
new_Data = pd.DataFrame(data=gfxm_dic)

#print(new_Data)

allData_List = []

allData_List.append(new_Data)

#读取丽新短租数据
l2 = []
dataList2 = []
def get_py2(path2,l2):
    fileList = os.listdir(path2)   #获取path目录下的所以文件
    for fileName in fileList:

        pathTmp = os.path.join(path2,fileName)  #获取path与fileName组合后的路径
        if '.xlsx' == fileName[-5:]:
            l2.append(pathTmp)
            #print(pathTmp)
            dataFD = pd.read_excel(pathTmp,sep=" ",header = 1)
            dataList2.append(dataFD)
                
path2 = '/Users/lixingongsi/Desktop/表格整合/丽新短租'.strip()
get_py2(path2,l2)


#合并两个Excel 表格
result2 = pd.concat(dataList2,axis=0).dropna(how='all')
#删除订单状态为“已取消”的订单
result_Data2 = result2[~result2["订单状态"].isin(["已取消"])]

delegate_DataFrame(result_Data2)


cs2 = []
#print(result_Data2.info())

for j in range(len(result_Data2['订单号'])):
    cs2.append('丽新短租') 
lxzc_dic = {
     '店代码':result_Data2['店代码'],
     '店名':result_Data2['店名'],
     '订单号':result_Data2['订单号'],
     '下单日期':result_Data2['下单日期'],
     '客户':result_Data2['客户'],
     '租用开始时间':result_Data2['租用开始时间'],
     '租用结束时间':result_Data2['租用结束时间'],
     '租用时长':result_Data2['租用时长'],
     '车型':result_Data2['车型'],
     '车辆':result_Data2['车辆'],
     '费用':result_Data2['费用'],
     '订单状态':result_Data2['订单状态'],
     '订单确认时间':result_Data2['订单确认时间'],
     '取车时间':result_Data2['取车时间'],
     '取车里程':result_Data2['取车里程'],
     '还车时间':result_Data2['还车时间'],
     '还车里程':result_Data2['还车里程'],
     '超里程费用':result_Data2['超里程费用'],
     '燃油费用':result_Data2['燃油费用'],
     '套餐优惠费用':result_Data2['套餐优惠费用'],
     '增值服务费用':result_Data2['增值服务费用'],
     '基础服务费用':result_Data2['基础服务费用'],
     '尊享服务费用':result_Data2['尊享服务费用'],
     '超时费用':result_Data2['超时费用'],
     '其他费用':result_Data2['其他费用'],
     '优惠卷费用':result_Data2['优惠卷费用'],
     '其他说明':result_Data2['其他说明'],
     '续租全部费用':result_Data2['续租全部费用'],
     '全部费用':result_Data2['全部费用'],
     '车辆店代码':result_Data2['车辆店代码'],
     '已付费用':result_Data2['已付费用'],
     '已付押金费用':result_Data2['已付押金费用'],
     '订单来源':result_Data2['订单来源'],
     '业务员':result_Data2['业务员'],
     '项目':cs2,
}

#使用字典创建一个DataFrame
new_Data2 = pd.DataFrame(data=lxzc_dic)

allData_List.append(new_Data2)

#合并两个Excel 表格
All_Result = pd.concat(allData_List,axis=0)


All_Result.to_excel('/Users/lixingongsi/Desktop/表格整合/intergre.xlsx'.strip(),index=False)

df = pd.read_excel('/Users/lixingongsi/Desktop/表格整合/intergre.xlsx')

print(df.info())

        