#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 14:13:57 2019

@author: lixin
"""
import datetime
import time
import calendar


#返回天列表======
def getBetweenDay(begin_date):  
    date_list = []  
    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")  
    end_date = datetime.datetime.strptime(time.strftime('%Y-%m-%d',time.localtime(time.time())), "%Y-%m-%d")  
    while begin_date <= end_date:  
        date_str = begin_date.strftime("%Y-%m-%d")  
        print(date_str)
        date_list.append(date_str)  
        begin_date += datetime.timedelta(days=1)  
    return date_list 
print(getBetweenDay('2019-2-8'))

'''
#返回月列表======
def getBetweenMonth(begin_date):  
    date_list = []  
    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")  
    end_date = datetime.datetime.strptime(time.strftime('%Y-%m-%d', time.localtime(time.time())), "%Y-%m-%d")  
    while begin_date <= end_date:  
        date_str = begin_date.strftime("%Y%m")  
        date_list.append(date_str)  
        begin_date = add_months(begin_date,1)  
    return date_list  
  
def add_months(dt,months): 
    #返回dt隔months个月后的日期，months相当于步长 
    month = dt.month - 1 + months  
    year = dt.year + month / 12  
    month = month % 12 + 1  
    day = min(dt.day, calendar.monthrange(year, month)[1])  
    return dt.replace(year=year, month=month, day=day)  

def getBetweenMonth(begin_date, end_date):
#返回所有月份，以及每月的起始日期、结束日期，字典格式
    date_list = {}
    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m")
        date_list[date_str] = ['%d-%d-01'%(begin_date.year, begin_date.month),
                               '%d-%d-%d'%(begin_date.year, begin_date.month, calendar.monthrange(begin_date.year, begin_date.month)[1])]
        begin_date = add_months(begin_date,1)
    return date_list


#获取所有季度，返回一个列表======
def getBetweenMonth(begin_date):  
    date_list = []  
    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")  
    end_date = datetime.datetime.strptime(time.strftime('%Y-%m-%d', time.localtime(time.time())), "%Y-%m-%d")  
    while begin_date <= end_date:  
        date_str = begin_date.strftime("%Y-%m")  
        date_list.append(date_str)  
        begin_date = add_months(begin_date,1)  
    return date_list  
  
def add_months(dt,months):  
    month = dt.month - 1 + months  
    year = dt.year + month / 12  
    month = month % 12 + 1  
    day = min(dt.day, calendar.monthrange(year, month)[1])  
    return dt.replace(year=year, month=month, day=day)  
  
def getBetweenQuarter(begin_date):  
    quarter_list = []  
    month_list = getBetweenMonth(begin_date)  
    for value in month_list:  
        tempvalue = value.split("-")  
        if tempvalue[1] in ['01','02','03']:  
            quarter_list.append(tempvalue[0] + "Q1")  
        elif tempvalue[1] in ['04','05','06']:  
            quarter_list.append(tempvalue[0] + "Q2")  
        elif tempvalue[1] in ['07', '08', '09']:  
            quarter_list.append(tempvalue[0] + "Q3")  
        elif tempvalue[1] in ['10', '11', '12']:  
            quarter_list.append(tempvalue[0] + "Q4")  
    quarter_set = set(quarter_list)  
    quarter_list = list(quarter_set)  
    quarter_list.sort()  
    return quarter_list  

def getBetweenQuarter(begin_date, end_date):
#加上每季度的起始日期、结束日期
    quarter_list = {}
    month_list = getBetweenMonth(begin_date, end_date)
    for value in month_list:
        tempvalue = value.split("-")
        year = tempvalue[0]
        if tempvalue[1] in ['01', '02', '03']:
            quarter_list[year + "Q1"] = ['%s-01-01' % year, '%s-03-31' % year]
        elif tempvalue[1] in ['04','05','06']:
            quarter_list[year + "Q2"] = ['%s-04-01' % year, '%s-06-30' % year]
        elif tempvalue[1] in ['07', '08', '09']:
            quarter_list[year + "Q3"] = ['%s-07-31' % year, '%s-09-30' % year]
        elif tempvalue[1] in ['10', '11', '12']:
            quarter_list[year + "Q4"] = ['%s-10-01' % year, '%s-12-31' % year]
    # quarter_set = set(quarter_list)
    # quarter_list = list(quarter_set)
    # quarter_list.sort()
    return quarter_list
'''