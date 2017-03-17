Name: csvfilter.py
import pandas as pd
import glob
import os
 
path = "C:/Users/Aaron Korver/Desktop/GIMA/Module 2/joinedtracks/joinedtracks/joinedtracks"
allfiles = glob.glob(os.path.join(path,"*.csv"))
 
for file_ in allfiles:
	df1=pd.read_csv(file_)
	df2=df1[df1.purpose == "home"]
	df3=df2[df2.accuracy < 11]
	df3['xmean'] = df3['X'].mean()
	df3['ymean'] = df3['Y'].mean()
	df4=df3.drop_duplicates(subset=['person'])E
	df4.to_csv(file_)
