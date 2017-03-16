import pandas as pd
import os
import glob
path = "C:/Users/Aaron Korver/Desktop/GIMA/Module 2/joinedtracks/joinedtracks"
allfiles = glob.glob(os.path.join(path,"*.csv"))
df5 = pd.read_csv('C:\Users\Aaron Korver\Downloads\Cases-met-buurtdata.csv')
for file_ in allfiles:
	df1 = pd.read_csv(file_)
	df2 = df1[['track','datetime','person']]       	
	df2['A'] = 1
	df2['count'] = df2.groupby('A')['track'].unique().apply(lambda x: len(x))
	df2.to_csv(file_)
	del df1
	del df2
