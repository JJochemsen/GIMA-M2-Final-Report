import arcpy,os
shpworkspace = r"C:\Users\Aaron Korver\Desktop\GIMA\Module 2\analyse"
arcpy.env.workspace = shpworkspace
arcpy.env.overwriteOutput = True
csvlist = arcpy.ListFiles("*.csv")
try:
	for csvfile in csvlist:
   	outlayer = "CSVEventLayer"
   	spatialreference = "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision"
   	arcpy.MakeXYEventLayer_management(csvfile,"X","Y",outlayer,spatialreference,"#")
   	shpfile = os.path.splitext(csvfile.replace('-', '_'))[0]
       arcpy.CopyFeatures_management(outlayer,shpfile)
	del outlayer
except:
	# If an error occurred print the message to the screen
	print arcpy.GetMessages()
