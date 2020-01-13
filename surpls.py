# -*- coding: utf-8 -*-
import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta
from operator import itemgetter
import time
import datetime
import calendar


def sort_csv(csv_filename):
    with open(csv_filename) as input_file:
        table = []
        for line in input_file:
            if line:
                col = line.split(',') #每行分隔为列表，好处理列格式
                ccol = col[0:3]
                ccol[1] = col[1] if col[1] > col[2] else col[2]
                ccol[2] = str(col[3][1:-1]) #各行没有先strip 末位是\n
                table.append(ccol) 

        table_sorted = sorted(table, key=itemgetter(2, 0))  #先后按列索引 tranceId,unixTime 排序

        time_num_id = {}
        ids =[]
        for row in table_sorted:
            if row and row[2]:
                if row[2] not in time_num_id.keys():
                    time_num_id[row[2]] =[] 
                    time_num_id[row[2]].append(row[:2])
                else:
                    time_num_id[row[2]].append(row[:2]) 
        return time_num_id   # a dict  {tranceId-1:[[],[],[]],tranceID-21:[[],[],[]],tranceID-31:[[],[],[]]}


class bandwith():
    def __init__(self,name,list_data):
        self.name = name
        self.list_data = list_data

    def timeToDate(self,unixTimeXargs):
        timeYear = time.strftime("%Y", time.localtime(unixTimeXargs))
        timeMonth = time.strftime("%m", time.localtime(unixTimeXargs))
        timeDay = time.strftime("%d", time.localtime(unixTimeXargs))
        initTime = datetime.date(int(timeYear), int(timeMonth), int(timeDay)) #年，月，日 datetime.date(2017, 7, 20)
        return initTime 
    
    def get_next_day(self,initTime):
        next_day = initTime + datetime.timedelta(days = 1) 
        next_day = str(next_day) + " 00:00:00"
        next_day = time.mktime(time.strptime(next_day,"%Y-%m-%d %H:%M:%S"))
        return next_day  # unix_time

    def list_spilt_by_month(self): #按月 切割成dict
        bandwith_month = {}
        for time_bandwith_list in self.list_data:
            year_month = time.strftime("%Y-%m", time.localtime(float(time_bandwith_list[0])))
            if year_month not in bandwith_month.keys():
                bandwith_month[year_month] = []
                bandwith_month[year_month].append(time_bandwith_list)
            else:
                bandwith_month[year_month].append(time_bandwith_list)
        return bandwith_month

    def enhance_bandwidth_month(self,bandwith_month):  # 增强型
        everymonth_bandwit_dict ={}
        for year_month in bandwith_month.keys():
            everymonth_bandwit_dict[year_month] =[]
            everyday_bandwith_dict = {}
            for time_bandwith in bandwith_month[year_month]:
                today_time = tanceId.timeToDate(float(time_bandwith[0]))
                unix_time_next_day = tanceId.get_next_day(today_time)
                while float(time_bandwith[0]) < unix_time_next_day:
                    if today_time not in everyday_bandwith_dict.keys():
                        everyday_bandwith_dict[today_time] = []
                        everyday_bandwith_dict[today_time].append(float(time_bandwith[-1]))
                    else:
                        everyday_bandwith_dict[today_time].append(float(time_bandwith[-1]))
            for today_time in everyday_bandwith_dict.keys():
                everyday_bandwith_dict[today_time].sort()
                everymonth_bandwit_dict[year_month].append(everyday_bandwith_dict[today_time][-5])
        
        final_every_bandwith_dict ={}
        for year_month in everymonth_bandwit_dict.keys():
            everymonth_bandwit_dict[year_month].sort()
            final_every_bandwith_dict[year_month] = sum(everymonth_bandwit_dict[year_month][-5:])//5  # 增强型
        return final_every_bandwith_dict

    def tradition_bandwidth_month(self,bandwith_month):  # 传统型
        everymonth_bandwit_dict ={}
        for year_month in bandwith_month.keys():
            everymonth_bandwit_dict[year_month] =[]
            for time_bandwith in bandwith_month[year_month]:
                everymonth_bandwit_dict[year_month].append(float(time_bandwith[-1]))
        
        final_every_bandwith_dict ={}
        for year_month in everymonth_bandwit_dict.keys():
            everymonth_bandwit_dict[year_month].sort()
            final_every_bandwith_dict[year_month] = everymonth_bandwit_dict[year_month][432] # 传统型
        return final_every_bandwith_dict
             


if __name__ == '__main__':
    csv_filename = "csv_alibaba.csv"    # 你的 csv文件。
    time_num_id = sort_csv(csv_filename)  
    for trance_id in time_num_id.keys():
        tanceId = bandwith(trance_id,time_num_id[trance_id])
        bandwith_month = tanceId.list_spilt_by_month()
        enhance_final_every_bandwith_dict = tanceId.enhance_bandwidth_month(bandwith_month)
        print(trance_id,"的增强型带宽峰值  ： ",enhance_final_every_bandwith_dict)
        tradition_final_every_bandwith_dict = tanceId.tradition_bandwidth_month(bandwith_month)
        print(trance_id,"的传统型带宽峰值  ： ",tradition_final_every_bandwith_dict)


        
    # def get_first_day_next_month(self,initTime):
    #     first_day = datetime.date(initTime.year, initTime.month, 1)
    #     days_num = calendar.monthrange(first_day.year, first_day.month)[1] #获取一个月有多少天
    #     first_day_of_next_month = first_day + datetime.timedelta(days = days_num) #当月的最后一天只需要days_num-1即可
    #     first_day_of_next_month = str(first_day_of_next_month) + " 00:00:00"
    #     first_day_of_next_month = time.mktime(time.strptime(first_day_of_next_month,"%Y-%m-%d %H:%M:%S"))
    #     return first_day_of_next_month # unix_time

    # def get_first_day_this_month(self,initTime):
    #     first_day = datetime.date(initTime.year, initTime.month, 1)
    #     first_day = str(first_day) + " 00:00:00"
    #     first_day = time.mktime(time.strptime(first_day,"%Y-%m-%d %H:%M:%S"))
    #     return first_day  # unix_time