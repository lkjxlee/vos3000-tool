#!/bin/python3


import requests
import pymysql
import json
import time
from datetime import date
import re



# 目标URL,填入vos3000的web 管理接口的ip和端口
api_url = "http://xxx.xxx.xxx.xxx:xxxx/external/server/GetGatewayRoutingOnline"

json_data = {
}


numbers_list= []                                                      #用来存放号码的信息
insert_list = []                                                      # 新增号码数据
update_list = []                                                      # 修改的号码数据

conn=pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='vos3000',
        port=3306,
        charset='utf8mb4'
        )
cursor = conn.cursor()

today = date.today().strftime("%Y%m%d")

table_name = 'e_cdr_'+today
current_time = int(time.time())
one_minutes_ago = current_time - 60

a=str(current_time)+'000'
b=str(one_minutes_ago)+'000'

sql1 = "select callertogatewaye164, count(callertogatewaye164), COUNT(CASE WHEN holdtime != 0 THEN 1 END) as valid_count from %s where stoptime >= %s and stoptime< %s  and callertogatewaye164 like '0%%' group by callertogatewaye164"%(table_name,b,a)

sql2 = "select caller from numbers_info"
update_sql = """
    UPDATE numbers_info 
    SET used_count = used_count + %s,
        valid_count = valid_count + %s
    WHERE caller = %s
    """
insert_sql = """
    INSERT INTO numbers_info 
    (caller, used_count, valid_count) 
    VALUES (%s, %s, %s)
    """

allnums=cursor.execute(sql1)
record_nums=cursor.rowcount

if (record_nums!=0):
	datas=cursor.fetchall()                         #话单信息
	cursor.execute(sql2)
	numbers = cursor.fetchall()                     #主叫次数信息
	for j in numbers:
		numbers_list.append(j[0])                #填充已经号码到内存		
	
	for i in datas:
		if i[0] in numbers_list:
			update_list.append((i[1],i[2],i[0]))
			
		else:
			insert_list.append((i[0],i[1],i[2]))
	if update_list != []:
		cursor.executemany(update_sql, update_list)
	if insert_list != []:
		cursor.executemany(insert_sql, insert_list)
	conn.commit()
					
cursor.close()
conn.close()
