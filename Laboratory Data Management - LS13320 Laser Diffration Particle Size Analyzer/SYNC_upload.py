import os
def iterator():
	for x, y, z in os.walk(r'C:\upload'):

		for Y in range(len(y)):
			if 'samples' in x + "\\"+ y[Y]:
				pass
##				print 'Folder already renamed: ',
##				print y[Y]
			else: rename(x + "\\"+ y[Y])

def rename(arg):
	n=0
	for x, y, z in os.walk(arg):


		# exit()
		for item in z:
			# print item

			if "av" in item[-2:]:
				# print item
				if "CONTROL" in item or "rerun" in item.lower() or "test" in item.lower():
					continue
				n+=1
				myDir = x
				# print item

		newname=  x[:-7]  + "data_" + x[-7:-2]+ "2015_" +  str(n) + 'samples'
	print newname
	print n

	print os.access(x,os.F_OK)


	os.rename(x,newname)


iterator()
