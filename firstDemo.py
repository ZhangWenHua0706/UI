#coding:utf8
#file:firstDemo.py 
'''
@author:sir
@date:2017.04.17
使用python+uiautomation实现Android 的UI自动化
(1)python下安装uiautomator模块
(2)windows下安装adb，用于与手机设备通信
(3)连接真机或者打开虚拟机
(4)编写脚本，运行脚本
'''
from uiautomator import device as d
from uiautomator import Device
from time import sleep

print ("test start")
#若有多台设备时，需指定设备serial number
# d = Device('6LPVLBAMJFSOSKAU')
#打开屏幕
d.screen.on()
#输出设备信息，包括分辨率
# print d.info
#点击home键
d.press.home()
#查看正在运行的app
# d.press.recent()

#通过text定位
if d(text="林安班车").exists:
	d(text="林安班车").click()
	sleep(3)

	if d(text="登录").exists:
		#清空账号文本框，通过resourceId定位
		d(resourceId='com.linan.owner:id/phone').clear_text()
		#输入账号
		d(resourceId='com.linan.owner:id/phone').set_text("13512753101")

		#清空密码
		d(resourceId='com.linan.owner:id/password').clear_text()
		#输入密码
		d(resourceId='com.linan.owner:id/password').set_text("a1234567")

		#返回键，将键盘收起
		d.press.back()
		#点击登录按钮
		d(resourceId='com.linan.owner:id/ok').click()

		sleep(5)

		print ("test pass")