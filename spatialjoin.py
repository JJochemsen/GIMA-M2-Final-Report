import arcpy
#Define workspace environment
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:/Users/Aaron Korver/Desktop/GIMA/Module 2/joinedtracks/"
pointlist = arcpy.ListFiles("*.shp")

#Define input paths
a = "C:/Users/Aaron Korver/Desktop/GIMA/Module 2/Geodatabase/geodatabase.gdb/buurtkaart"
b = "C:/Users/Aaron Korver/Desktop/GIMA/Module 2/Geodatabase/geodatabase.gdb/OutputPandas3"
c = "C:/Users/Aaron Korver/Desktop/GIMA/Module 2/Geodatabase/geodatabaseoutput.gdb/CaseList"

#Execute spatial join
try:
	for shpfile in pointlist:
   	arcpy.SpatialJoin_analysis(b, a, c)
