# This snippet can be excecuted from the Python window in GIS
# It will change the legend so taht only items visible in the current map extent are shown.

import arcpy
import arcpy.mapping
mxd = arcpy.mapping.MapDocument("CURRENT")


legend = arcpy.mapping.ListLayoutElements(mxd,"LEGEND_ELEMENT")[0]

for lyr in legend.listLegendItemLayers():
        legend.updateItem(lyr, use_visible_extent = True)
        print 'updateItem' 
arcpy.RefreshActiveView()