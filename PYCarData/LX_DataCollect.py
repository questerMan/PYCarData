#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 09:05:23 2019

@author: lixin
"""
import pandas as pd
import numpy as np
import os

#定义生成的文件名
collectName = 'collectData.xlsx'

#定义文件路径
path1 = '/Users/lixingongsi/Desktop/PYCarData/运营数据/'.strip()
path2 = '/Users/lixingongsi/Desktop/PYCarData/运营数据/丽新短租/'.strip()

#遍历读取某个文件夹下的文件信息
def getData(path):
    pathTmp = ''
    dataList = []
    fileList = os.listdir(path)   #获取path目录下的所以文件
    for fileName in fileList:
        pathTmp = os.path.join(path,fileName)  #获取path与fileName组合后的路径
        if '.xlsx' == fileName[-5:]:
            if fileName == collectName:
                 #print("已删除===生成的collectData.xlsx文件====已删除")
                 os.remove(pathTmp)
            else:
                #print(pathTmp)
                dataFD = pd.read_excel(pathTmp,sep=" ",header = 1)
                dataList.append(dataFD)
    return dataList


def res_dataIndex(dataFrame):
    #合并数据后进行index重新排序，以免index值重复
    dataFrame = dataFrame.reset_index(drop = True)
    return dataFrame

#合并“/Users/lixingongsi/Desktop/运营数据/”下.xlsx的Excel表格 
collectData1 = pd.concat(getData(path1),axis=0)

#合并“/Users/lixingongsi/Desktop/运营数据/丽新短租/”下.xlsx的Excel表格
collectData2 = pd.concat(getData(path2),axis=0)

#定义两个项目名称
projectName1 = '广丰项目'
projectName2 = '丽新短租'

#建立newList_DataFrame存放new_DataFrame
newDataFrame_List = []

def give_ProjectName(dataFrame,projectName):
    list_Name = []
    for item in dataFrame.iterrows():
        list_Name.append(projectName)
    return list_Name
    
#数据转化为同一个格式字段属性
dic1 = {
        '店代码':'',
        '店名':collectData1['取车店'],
        '订单号':collectData1['订单号'],
        '下单日期':collectData1['下单日期'],
        '客户':collectData1['客户姓名'],
        '租用开始时间':collectData1['租用开始时间'],
        '租用结束时间':collectData1['租用结束时间'],
        '租用时长':collectData1['租用时长'],
        '车型':collectData1['车型'],
        '车辆':collectData1['车牌号'],
        '费用':'',
        '订单状态':collectData1['订单状态'],
        '订单确认时间':'',
        '取车时间':collectData1['租用开始时间'],
        '取车里程':'',
        '还车时间':collectData1['租用结束时间'],
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
        '全部费用':collectData1['费用总额'],
        '车辆店代码':'',
        '已付费用':'',
        '已付押金费用':'',
        '订单来源':'',
        '待定':'',
        '项目':give_ProjectName(collectData1,projectName1),
        '区域':'',
        '城市':'',
        '门店':'',
        '组别':'',
        '业务员':''
        }
#生成新的dataFrame1
new_DataFrame1 = pd.DataFrame(data = dic1)

#存入newList_DataFrame
newDataFrame_List.append(new_DataFrame1)

dic2 = {
        '店代码':collectData2['店代码'],
        '店名':collectData2['店名'],
        '订单号':collectData2['订单号'],
        '下单日期':collectData2['下单日期'],
        '客户':collectData2['客户'],
        '租用开始时间':collectData2['租用开始时间'],
        '租用结束时间':collectData2['租用结束时间'],
        '租用时长':collectData2['租用时长'],
        '车型':collectData2['车型'],
        '车辆':collectData2['车辆'],
        '费用':collectData2['费用'],
        '订单状态':collectData2['订单状态'],
        '订单确认时间':collectData2['订单确认时间'],
        '取车时间':collectData2['取车时间'],
        '取车里程':collectData2['取车里程'],
        '还车时间':collectData2['还车时间'],
        '还车里程':collectData2['还车里程'],
        '超里程费用':collectData2['超里程费用'],
        '燃油费用':collectData2['燃油费用'],
        '套餐优惠费用':collectData2['套餐优惠费用'],
        '增值服务费用':collectData2['增值服务费用'],
        '基础服务费用':collectData2['基础服务费用'],
        '尊享服务费用':collectData2['尊享服务费用'],
        '超时费用':collectData2['超时费用'],
        '其他费用':collectData2['其他费用'],
        '优惠卷费用':collectData2['优惠卷费用'],
        '其他说明':collectData2['其他说明'],
        '续租全部费用':collectData2['续租全部费用'],
        '全部费用':collectData2['全部费用'],
        '车辆店代码':collectData2['车辆店代码'],
        '已付费用':collectData2['已付费用'],
        '已付押金费用':collectData2['已付押金费用'],
        '订单来源':collectData2['订单来源'],
        '待定':'',
        '项目':give_ProjectName(collectData2,projectName2),
        '区域':'',
        '城市':'',
        '门店':'',
        '组别':'',
        '业务员':collectData2['业务员']
        }

#生成新的dataFrame2
new_DataFrame2 = pd.DataFrame(data = dic2)

#存入newList_DataFrame
newDataFrame_List.append(new_DataFrame2)

#合并两个新的DataFrame数据
result_DataFrame = res_dataIndex(pd.concat(newDataFrame_List,axis=0).dropna(how='all'))

#读取基础信息匹配表【基础信息】
base_Data = pd.read_excel('/Users/lixingongsi/Desktop/PYCarData/运营数据/基础信息/基础信息.xlsx',sheet_name = "基础信息")
#转换成字典
dic_Base = base_Data.set_index('原门店').T.to_dict('list')
#print(dic_Base['总店'][1])

#读取基础信息匹配表【业务员组别】
base_YWYData = pd.read_excel('/Users/lixingongsi/Desktop/PYCarData/运营数据/基础信息/基础信息.xlsx',sheet_name = "业务员组别")
#转换成字典
dic_YWYBase = base_YWYData.set_index('业务员').T.to_dict('list')

#查找字典抽取对应方法
def find_Value(name,dic,num):
    for key,value in dic.items():
        if name == key:
            return value[num]
        
'''20190710165025132 GX20190711170050819
#数据清洗过滤  
1、删除 已取消订单
2、删除还车时间早于取车时间的已完成订单 已完成
3、更改取车时间早于下单日期订单，交换下单日期=取车时间
'''
def washData(DataFrame):
 
    #去订单号的重复值
    DataFrame.drop_duplicates(subset=['订单号'],keep='first',inplace=True)
    #1、删除 已取消的订单
    DataFrame_wash1 = res_dataIndex(DataFrame[~DataFrame["订单状态"].isin(["已取消"])])
    
    #缺省值自动添加空格
    #DataFrame_wash1.fillna('', inplace = True)
    #for row in DataFrame_wash1.rows:
     #   print(row)
    #print(DataFrame_wash1)
  
    for index,row in DataFrame_wash1.iterrows(): 
        if row['订单号'] == 'LX20190621144117063':
            ZX_T=''
            ZX_T = row['租用开始时间']
            DataFrame_wash1.at[index,'取车时间'] = ZX_T
            print('~~~~~~~~~~~~~~{}----{}'.format(row['订单号'],[index,'取车时间']))
        if pd.isnull(row['取车时间']) != True:
            interval2 = np.timedelta64(row['取车时间']-row['下单日期'],'ns').astype(float)
           
            if interval2 < 0:
                QX_T=''
                QX_T = row['取车时间']
                #print('{}-----{}'.format(index,QX_T))
                #DataFrame_wash1.ix[(DataFrame_wash1.订单号 == D_ID),'下单日期'] = D_ID
                DataFrame_wash1.at[index,'下单日期'] = QX_T
                #row['下单日期'] = QX_T
                #print('{}==={}=={}'.format(index,interval2,row['下单日期']))
            if pd.isnull(row['还车时间']) != True :
                interval1 = np.timedelta64(row['还车时间']-row['取车时间'],'ns').astype(float) 
                #print(interval1) 20190611143917993   20190621144117063 
                if interval1 < 0: 
                    #DataFrame_wash1.drop(DataFrame_wash1.index[k],inplace=True)
                    DataFrame_wash1.drop([index],inplace=True)  #删除改变内存inplace=True
                    #print('删除错误的XXXXXXX')
                    continue   
    
    res_dataIndex(DataFrame_wash1)
    
    for index,row in DataFrame_wash1.iterrows():
        #添加区域信息
        QU_Name = find_Value(row['店名'],dic_Base,2)
        DataFrame_wash1.at[index,'区域'] = QU_Name
        
        #添加城市信息
        CS_Name = find_Value(row['店名'],dic_Base,1)
        DataFrame_wash1.at[index,'城市'] = CS_Name
        
        #数据源门店信息转换
        MD_Name = find_Value(row['店名'],dic_Base,0)
        DataFrame_wash1.at[index,'门店'] = MD_Name
        
        #添加组别信息（根据门店一次筛选）
        #print('{}--1--{}'.format(index,row['组别']))
        ZB_Name = find_Value(row['店名'],dic_Base,3)
        DataFrame_wash1.at[index,'组别'] = ZB_Name
        
        #添加组别信息（根据业务员二次筛选）
        #print('{}--2--{}'.format(index,row['组别']))
        YWY_Name = find_Value(row['业务员'],dic_YWYBase,0)
        DataFrame_wash1.at[index,'组别'] = YWY_Name
        #print('{}--3--{}'.format(index,row['组别']))
    
    return res_dataIndex(DataFrame_wash1)

newResultCollect_DataFrame  = washData(result_DataFrame)

newResultCollect_DataFrame.to_excel('/Users/lixingongsi/Desktop/PYCarData/运营数据/'+collectName)

df = pd.read_excel('/Users/lixingongsi/Desktop/PYCarData/运营数据/'+collectName)
 
print(df.info())
'''
总数据：
订单租赁天数、订单平摊营收、
日数据：
新增订单、预约单、长租单、总订单、租赁状态（正在出租、预约订单、已结束单、未来订单）、平摊营收
月数据：
新增订单、预约单、长租单、总订单、订单租赁天数、平摊营收

'''