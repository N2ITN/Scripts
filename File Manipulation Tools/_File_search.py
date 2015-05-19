import os, shutil
import time



d = r'C:\Users\zestela53\Desktop\dot_py'



MATCH = 'combine'
n=0
f=0
for x, y, z in os.walk(d):
	
	for item in z:
		fullPath = x + "\\" + item
		if MATCH.lower() in item.lower():
			print fullPath
			n+=1
		f+=1
print "found %s files with MATCH" %n
print "%s files searched" %f


