import arcpy
import os
import time



print "starting..."
mxd = arcpy.mapping.MapDocument(r"N:\GIS\Projects\C1374_AlliedEng_Artthaus\Working_MXDs\2015_sampling_locs.mxd")
path = mxd.filePath
path =  os.path.basename(path)[:-4]
fold = "H:\\_TEMP_PDF\\C1374_AlliedEng_Artthaus\\"
pdf = ".pdf"
date = (time.strftime("_%Y.%d.%m"))
newPdf = fold + path + date + pdf
if os.access(fold,os.F_OK) == False:
    os.mkdir(fold)
arcpy.mapping.ExportToPDF(mxd, newPdf)
mxd.save()


import winsound
winsound.Beep(440, 250)
print "done"