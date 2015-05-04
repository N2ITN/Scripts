# MakeXYLayer.py
# Description: Creates an XY layer from an xy table and exports it to a layer file
# Requires arcpy

# import system modules 
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"
 
try:
    # Set the local variables
    in_Table = "XYData.xls"
    x_coords = "X"
    y_coords = "Y"
    z_coords = ""
    out_Layer = "Chem_layer"
    saved_Layer = r"c:\output\Chem_layer.lyr"
 
    # Set the spatial reference
    spRef = r"Coordinate Systems\Projected Coordinate Systems\Utm\Nad 1983\NAD 1983 UTM Zone 11N.prj"
 
    # Make the XY event layer...
    arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)
 
    # Print the total rows
    print arcpy.GetCount_management(out_Layer)
 
    # Save to a layer file
    arcpy.SaveToLayerFile_management(out_Layer, saved_Layer)
 
except:
    # If an error occurred print the message to the screen
    print arcpy.GetMessages()