
#Description:
# This script will look at every file in the main directory folder only.
# It sorts files into sub-folders based on their extension (all excel type files will go into a folder called 'excel')
	# It will not delete or overwrite anything, it just moves files in the top level to a folder matching the file's extension
	# New folders are created only if needed, and are placed in the same directory

##d = r"C:\Users\zestela53\Desktop\gulf_temp\59\Allfiles"
import os, shutil

def Extensions_to_folders(d):	

	# Initialize counter
	n = 0
	# Iterate through files in parent folder
	for item in os.listdir(d):
		# Check if file
		if os.path.isfile(os.path.join(d, item)):
			print item

			# Get extension
			iExt = os.path.splitext(item)[-1][1:]
			print iExt

			# If excel-type document, lump into "excel" folder 
			if "xls" in iExt:
				iExt = "Excel"

			# Create path for original	
			fullPath = d + "\\" + item
			# Create path for extension folder
			extDir = d + "\\" + iExt+ "\\"

			# Create extension folder if it doesn't exist
			if os.access(extDir,os.F_OK) == False:
				os.mkdir(extDir)

			#Create path for new item location 	
			finalPath = extDir + item

			# Move files to new folder
			if len(fullPath) >1 :
				shutil.move(fullPath,finalPath)
				n+=1
	print "%s Files were moved." %n



