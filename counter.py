#!/usr/local/bin/python

# TimeTracking Program for Projects
from datetime import datetime
import time
from decimal import *
import sys
import os
import select
from termcolor import colored


os.system('cls' if os.name == 'nt' else 'clear')


# Set path for datafile
PATH='./tTrackData.txt'
getcontext().prec = 2


def openDatafile():
	if os.path.isfile(PATH):
		print "Datafile exists"
		file = open("tTrackData.txt", 'r')
		mins_old = file.readlines()
		return mins_old
	else:
		file = open(PATH, 'w')
		file.write("0")
		print "New datafile created"
		mins_old = [0]
		return mins_old

	file.close

def timer(mins_old):
	print "You already worked for %s hours\n" % (Decimal(mins_old[0])/60)
	run = raw_input("Press Enter to start / 'no' to abort > ")
	now = datetime.now()

	mins_old = mins_old[0]
	secs = 0

	if run == "no":
		print "Program terminated"
		sys.exit()
	else:
		while True:
			os.system('cls' if os.name == 'nt' else 'clear')
			print "Process started at %s:%s" %(now.hour, now.minute)
			print colored("%s minute(s)" %(int(secs)/60),'green')
			print '\n Press Enter to stop'
			time.sleep(1)
			secs += 1
			if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
				line = raw_input()
				return secs
				break

def printFile(mins_old, secs):
	print "Final time: %s hours" %(Decimal((secs/60) + int(mins_old[0]))/60)
	file = open(PATH, "w")
	file.write(repr(int(mins_old[0]) + secs/60 + 1))
	file.close()


print "TimeTracking Program \n -------------------"
mins_old = openDatafile()
secs = timer(mins_old)
printFile(mins_old, secs)