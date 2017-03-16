import pandas as pd
import os
import glob
path = "C:\Users\Aaron Korver\Desktop\GIMA\Module 2\joinedtracks\utilitarian\joinedtracks"
allfiles = glob.glob(os.path.join(path,"*.csv"))
mapping = {'diensten': 1, 'home': 1, 'sociaal': 0, 'betaaldwerk': 1, 'niet-dagelijkeboodschappen': 1, 'vrijetijd': 0, 'recreatie': 0, 'dagelijkeboodschappen': 1, 'studie': 1}
for file_ in allfiles:
	df1 = pd.read_csv(file_)
	df2 = df1[['person','purto','track']] 
	df3 = df2.drop_duplicates(subset=['track'])
	df4 = df3.replace({'purto':mapping})
	df5 = df4.convert_objects(convert_numeric=True)
	df6 = df5.dropna(subset=['purto'])
	df6['Utilitarian'] = df5['purto'].mean()
	df6['NonU'] = 1 - df6['Utilitarian']
	print df6
 	df6.to_csv(file_)
	del df1
	del df2
	del df3
	del df4
	del df5
	del df6
