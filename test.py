# -*- coding:utf-8 -*-
from uiautomator import device as d
import loglog

def unfreezescreen():
	'''d.wakeup()
	d.swipe(200,300,660,1060)
	d.swipe(200,300,660,1060)
	d.click(171.8,1056.1)'''
	p1 = (171.8,1056.1)
	p2 = (360.5,855.2)
	p3 = (551.2,658.5)
	p4 = (551.2,855.2)
	p5 = (360.5,1056.1)
	p = {p1,p2,p3,p4,p5}
	d.swipePoints(p,20)

if __name__=='__main__':
	'''print (d.info)
	d.screen.on()
	d.screen.off()
	loglog.logging.info('This is a log info')'''
	unfreezescreen()