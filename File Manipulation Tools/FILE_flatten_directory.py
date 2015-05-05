import os, shutil

## This moves all of the files in a directory to the main directory
## If you want to export the files to a different folder, just write a different path for 
## 


mypath = r"C:\Users\zestela53\Desktop\_LL_TEMP\_renamed\\"




for path, subdirs, files in os.walk(mypath):
	
	for x in files:
		current= path + "\\" + x
		new = mypath +"\\" + x
		print current
		print new
		print

		shutil.move(current,new)

## Its good to print first to test the paths, then you can un-comment shitutil.move() when
## you're sure it's what you need
		
