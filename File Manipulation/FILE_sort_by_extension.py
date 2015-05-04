
#Description:
# This script will look at every file in the main directory folder only.
# It sorts files into sub-folders based on their extension (all excel type files will go into a folder called 'excel')
	# It will not delete or overwrite anything, it just moves files in the top level to a folder matching the file's extension
	# New folders are created only if needed, and are placed in the same directory

import os, shutil

d = r"C:\Users\zestela53\Desktop\gulf_temp\59\Allfiles"
n = 0

for item in os.listdir(d):
	if os.path.isfile(os.path.join(d, item)):
		
		print item

		iExt = os.path.splitext(item)[-1][1:]
		print iExt

		if "xls" in iExt:
			iExt = "Excel"
		fullPath = d + "\\" + item
		extDir = d + "\\" + iExt+ "\\" 
		
		if os.access(extDir,os.F_OK) == False:
			os.mkdir(extDir)

		finalPath = extDir + item
  	
		if len(fullPath) >1 :

			shutil.move(fullPath,finalPath)
			n+=1

print "%s Files were moved." %n



