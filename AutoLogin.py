# -*- coding: UTF-8 -*-
import requests
import time
def login():
	urlstring='http://192.168.29.2/ac_portal/login.php'
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'
	headers={'User-Agent':user_agent}
	Name='张文华'
	passwd='123456'
	data={'opr':'pwdLogin','userName':Name,'pwd':passwd,'rememberPwd':0}

	response=requests.post(urlstring,data=data,headers=headers)

def runLogin():
	while True:
		login()
		time.sleep(10800)


if __name__=='__main__':
	runLogin()