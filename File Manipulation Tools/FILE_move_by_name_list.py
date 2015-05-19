
## This script will move files with names that contain strings in the list 'moveList' to the destination
## folder of your choice 
import os, shutil
moveList = ['.xls', '20150519','cat_pics']


# Source folder to search in
source = r'C:/source_folder'
#Destination folder for matches
dest   = r'C:/destination_folder'
def getItems(source):

	for x,y,z in os.walk(source):
		for items in z:
			for name in moveList:
				lenName = len(name)
				if name == items[:lenName]:
					p = x.replace("\\","/")
					yield x+"/"+items, items

moveFiles = list(getItems(source))

for a in moveFiles:
	new = dest +"/" + a[1]
	old = a[0]

	shutil.move(old,new)


