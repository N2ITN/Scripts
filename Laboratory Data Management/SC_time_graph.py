
# from __future__ import print_function
from matplotlib import mlab
from pylab import figure, show
import matplotlib.cbook as cbook
import os, shutil, time
import re
import datetime

fileList= []
timeList = []
d = r"E:\untouched_data\4_22_15"
qcList = []
for x, y, z in os.walk(d):

	for item in z:
		fullPath = x + "\\" + item
		if u"$av" in item:


			if "trial"in item.lower() or "test"in item.lower() or "control"in item.lower() :
				qcList.append(item)

			fileList.append(item)

			datetime = time.ctime(os.path.getmtime(fullPath))
			# print item
			time_ = datetime.split(" ").pop(3)


			mins = sum(int(x) * 60 ** i for i,x in enumerate(reversed(time_.split(":"))))/60

			if mins != "None":
				# print mins

				timeList.append(mins)
a = zip (fileList, timeList)
timeList.sort()

deltaList = []
for t in range(len(timeList)):
	u = t+1
	try:
		delta = timeList[u]-timeList[t]
		if delta==0:
			# print timeList[u], timeList[t]
			# print fileList[u]
			# print fileList[t]

			print delta
			print
		if delta > 40:
			pass
		else:deltaList.append(delta)

	except IndexError:
		pass


totalTime = sum(deltaList)


import numpy as np
import matplotlib.pyplot as plt


x = range(len(deltaList))
y = deltaList


print y
x1 = range(1,int(len(deltaList)))
y1  =  [int(np.mean(deltaList))] *int(len(deltaList)-1)




MIN = min(deltaList)

x2=range(len(deltaList)-1)
y2= [MIN] *int(len(deltaList)-1)
# print x1
# print y1

totalTime = round((totalTime/60.0),1)
ave = int(np.mean(deltaList))

print "Ave: %s mins" % ave
print "Actual samples: %s" %int(len(deltaList))

plt.plot(x1, y1,"--",  linewidth=2, label="Mean: %s mins" %ave)

plt.plot(x, y, linewidth=2, label = "Total: %s hours" %totalTime)

# print x2
# print y2

plt.plot(x2, y2,"--", linewidth=1, label = "Min: %s" %MIN)

font = {
        'color'  : 'black',
        'weight' : 'normal',
        'size'   : 18,
        }

total_ = len(deltaList)+int(len(qcList)-1)

anno = "Actual samples: %s" %str(len(deltaList)-len(qcList)+1) + "\n"  + "QC samples: %s" %len(qcList)  + "\n" + "Total samples: %s" %total_


plt.annotate( anno, (.025, .845), xycoords='axes fraction', backgroundcolor='w',bbox=dict(pad=10.0,alpha=1), fontsize='large')


plt.xlabel('number of samples', fontdict=font)
plt.ylabel('time (m)', fontdict=font)


legend = plt.legend(loc='upper right', shadow=False)


plt.show()