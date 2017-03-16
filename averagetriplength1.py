import pandas as pd
import numpy as np
import glob
import os
path = "C:/Users/joach/Documents/GIMA/Module 2/joinedtracks/"
allfiles = glob.glob(os.path.join(path,"*.csv"))
for file_ in allfiles:
	df1 = pd.read_csv(file_)
	df2 = df1[['person', 'track','datetime']]
	df3 = df2.groupby(['track']).nth((0, -1)).reset_index()    	
	df3['datetime'] = pd.to_datetime(df3['datetime'], format= '%Y/%m/%d %H:%M:%S')
	df3['triplength'] = df3.sort_values(['track','datetime']).groupby('track')['datetime'].diff()
	df4 = df3.dropna(subset=['triplength'])
	df5 = df4[['person', 'track', 'triplength']].reset_index()
	df6 = df5[['person', 'track', 'triplength']]
	df6['triplengthmin'] = df6.triplength /np.timedelta64(1, 'm')
	df6['meantriplength'] = df6["triplengthmin"].mean()
	df6.to_csv(file_)
	del df1
	del df2
	del df3
	del df4
	del df5
   del df6
