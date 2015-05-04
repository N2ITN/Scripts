#This script creates a CSV with 3 columns: 
#1) for all file paths below the given directory, 
#2) the size of each file 
#3) file size units (KB)


import os

from os import listdir
from os.path import isfile, join
from os import walk
import glob

make = []
#mypath = 'L:\A0006_City_of_Seattle\15_Terminal_117\15A_Construction_Oversight\LiveLink_flat'
mypath = r"C:\Users\zestela53\Desktop\gulf_temp\Leg1"

BURN = 5
# how many \\ to not include starting from left (recursion depth notwithstanding)



N = mypath.split("\\") 
N1= str(N[len(N)-1:])
csvname = N1

print  N1

def makelist(path,bin):

	make = []
	#file only: Bin = 0
	if bin == 0:
		make = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
	if bin == 1:
		
		for path, subdirs, files in walk(path):
			#print len(files)
			# for x in subdirs:
				
			# 	make.append(x)
			for i in range(len(files)):
				

				justpath =  path+"\\"+files[i] 
				wholepath = (justpath.split("\\")[BURN:])
				wholepath = "\\".join(wholepath)
				
				

				wholepathq= '"' + wholepath + "\\"'"'
				
				size = (os.path.getsize(justpath))/float(1024)
				if size > 1000:
					byte = "MB"
					size = size/float(1000)
				else: byte = "KB"


				sizestring = "%.2f" % size

				size =  "," + sizestring + ", " + byte
				make.append(join(str(wholepath),size))
				
				
				
				
			
	make.insert(0,glob.glob(mypath))
	
	
	return make




from CSVnamelist import csvmaker


mylist = makelist(mypath,1,)



csvmaker(csvname,mylist)

import os
os.startfile(csvname + ".csv")

print "done"


