import time
import os

not_executed = 1

while(not_executed):
	dt = list(time.localtime())
	hour = dt[3]
	minute = dt[4]
	
if hour == 00 and minute == 01:
	os.popen2("open /C:\Users\Rob\Pictures\busyPenguin.jpg")
	
not_executed = 0
