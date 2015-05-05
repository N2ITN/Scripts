import fileinput
import os, shutil

d = r'C:\drop\_new'
# d = r'C:\drop\test'
n=0

##key_ = "$ls.xls"
##val_ = "xls"

key_ = '0BEWB_'
val_ = 'BEWB_'
# replaceDict = {}  #if more than one pair


def renameFile(file):


	newName = file.replace(key_,val_)
	print file, newName

	file = file.replace("\\","/")
	os.rename(file,newName)
	#print "to %s"% newName

def renameInternals(file_):


	for line in fileinput.input(file_, inplace=True):
		print line.replace(key_,val_),


def renameAll():
	send = []
	for x, y, z in os.walk(d):

		for item in z:
			fullPath = x + "\\" + item
			if key_ in item:
				print "processing %s" % item
				# send.append(item) #lets do it one by one for debug purposes
				renameInternals(fullPath)
				#print "renamed internals for: %s" % item
				renameFile(fullPath)


renameAll()