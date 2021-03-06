import datetime
import os
class createLogs:
	#global declarations of class createlog
	#system time
	osTime = None
    #filename generated by year month and day
	filename = None
	#channellog time generated by hours and minutes
	currTime = None

	directory = "logs/channels/"

	#constructor for class createlog
	def __init__(self):
		self.osTime = datetime.datetime.now()

		self.filename = self.osTime.strftime("%Y-%m-%d")
		self.currTime = self.osTime.strftime("%H:%M")

		if not os.path.exists(self.directory):
			os.makedirs(self.directory)
	#writelog helper
	def writeserverlog(self, log):
		filea = open("logs/" + self.filename  + ".txt","a") 
		filea.write("[" + self.currTime + "]" + ":" + log + "\n")
		filea.close() 

	#functions
	def printandwriteserverlog(self, msg):
		print(msg)
		self.writeserverlog(msg)

	def writechannellog(self, log, channel):
		logtowrite = "[" + self.currTime + "]" + ":" + log + "\n"

		if not os.path.exists(self.directory + channel):
			os.makedirs(self.directory + channel)
			filea = open(self.directory + channel + "/" + self.filename + ".txt","a")
			filea.write(logtowrite)
			filea.close() 
		else:
			filea = open(directory + "/" + self.filename + ".txt","a") 
			filea.write(logtowrite)
			filea.close()