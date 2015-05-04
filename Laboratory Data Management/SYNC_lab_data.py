import os, shutil
import time




flash = r'E:\data'

drop = r'C:\drop'

def noDash():
	n=0
	for F in [flash,drop]:
		for x, y, z in os.walk(F):
			
			for item in z:
				fullPath = x + "\\" + item
				newName = fullPath.replace("-","_")
				if "-" in item:
					os.rename(fullPath,newName)
					print "renamed:"
					print fullPath
					print newName
					print
					n+=1
	return  'renamed %s files' %n
print noDash()





def getFiles(input):
	defList = []
	for x, y, z in os.walk(input):

		for item in z:
			dirPath = x.rsplit("\\",1).pop()+ "\\"+ item
			# print dirPath
			defList.append(dirPath)
			# print dirPath
	
	return defList		

fList = getFiles(flash)
dList = getFiles(drop)


cList = list(set(fList).difference(dList))
if len(cList)>0:
	# print 
	# print cList

	for item in cList:

		fold = drop + "\\" + item.split("\\").pop(0)
		# continue
		if os.access(fold,os.F_OK) == False:
		    os.mkdir(fold)
		    print 'made new folder: %s' %fold
		
		shutil.copy(flash + "\\" + item, drop + "\\" + item)
		print "Copied: "'"%s"'" to folder: %s" %(item, drop)



# format:
# 	data_4_13_2015_24samples





