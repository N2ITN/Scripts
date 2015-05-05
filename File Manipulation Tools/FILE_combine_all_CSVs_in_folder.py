##This program scans through multiple CSV documents in a folder and combines them into one

import csv
import os, shutil
try:
	os.remove('C:\Users\zestela53\Desktop\gulf_temp\82\output.csv')
except WindowsError:
	pass
f_new = open('C:\Users\zestela53\Desktop\gulf_temp\82\output.csv','a')

d = r"C:\Users\zestela53\Desktop\gulf_temp\82\NOAA_fileList"
d = d.replace("\\","/")
for x, y, z in os.walk(d):
	
	for item in z:

		if item[-4:] == '.csv':
			fullPath = x + "/" + item

			print fullPath
			f = open(fullPath, 'r')
			contents = f.read()
			lines = contents.split('\n')    # split file into seperate lines

			for line in lines:
				f_new.write(line +  "\r") 
f_new.close()			

