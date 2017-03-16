import pandas as pd
import os
import glob
import numpy as np
path = "C:\Users\Aaron Korver\Desktop\GIMA\Module 2\joinedtracks\utilitarian\joinedtracks"
allfiles = glob.glob(os.path.join(path,"*.csv"))
for file_ in allfiles:
	df1 = pd.read_csv(file_)    	
	df2= df1.dropna()
   df3=df2.drop_duplicates(subset=['person'])
	columns = ["","track", "datetime", "person", "A", "count"]
	df3.to_csv('C:/Users/Aaron Korver/Desktop/GIMA/Module 2/joinedtracks/joinedtracks/outputloop.csv',mode='a',header=columns)
	del df1
	del df2
