# -*- coding:utf-8 -*-
import requests
import loglog
import configparser
import pymysql
import time,os
def PostInfo(VehicleNumber):
	errmsg='查不到该车辆信息'
	VehicleNumber=VehicleNumber
	urlstring='http://credit.logink.org/gateway/directQuery!qry.htm'
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	headers={'User-Agent':user_agent}
	data={'ActionType':'VehicleQuery','LogisticsExchangeCode':'14471','userToken':'YmUzNTk4YTItNGQwYy00MjFmLTg2ZWUtYWYyZTg4NzA4MmUxVF9UXzFBU19JRF9sb2dpbmtfMA',
	'VehicleNumber':VehicleNumber,'RoadTransportCertificateNumber':'','LicensePlateTypeCode':'黄色'}
	response=requests.post(urlstring,data=data,headers=headers)
	if errmsg in response.text:
		#loglog.logging.info(VehicleNumber +' not found')
		return 0
	else:
		pos=response.text.index('道路运输证号:</td><td>')
		start=pos+16
		end=start+12
		return response.text[start:end]

def GetConnection(sqlscript):
	cf=configparser.ConfigParser()
	cf.read('D:\Python34\interface\config.ini',encoding="utf-8-sig")
	host=cf.get('MySqlDB','host')
	user=cf.get('MySqlDB','user')
	password=cf.get('MySqlDB','password')
	port=cf.get('MySqlDB','port')
	db=cf.get('MySqlDB','dbname')
	Conn = pymysql.connect(host=host,user=user,passwd=password,port=int(port),db=db,charset='utf8')
	cur=Conn.cursor()
	cur.execute(sqlscript)
	output = open('chepai10019.txt','a')
	for r in cur.fetchall():
		if r[0] == '':
			continue
		else:
			print (r[0])
			final_string=str(r[0])+' '+str(PostInfo(r[0]))
			output.writelines(final_string+"\n")
			#pickle.dump(output,final_string)
			time.sleep(1)
	output.close()
	cur.close()
	Conn.close()
	

	
if __name__=='__main__':
	#PostInfo('湘B06879')
	GetConnection('SELECT a.license_plate from veh_vehicle_info a,cust_customer_base b where a.customer_id=b.customer_Id and b.reexamine=2  and a.id>47721 limit 105581,10000')