import pandas as pd
import os
import glob
path = "C:/Users/Aaron Korver/Desktop/GIMA/Module 2/joinedtracks/joinedtracks/joinedtracks"
allfiles = glob.glob(os.path.join(path,"*.csv"))
mapping = {'diensten': 2, 'home': 2, 'sociaal': 2, 'betaaldwerk': 2, 'niet-dagelijkeboodschappen': 2, 'vrijetijd': 2, 'recreatie': 2, 'dagelijkeboodschappen': 2, 'studie': 2, 'EBIKE': 1, 'BIKE': 0}
 
for file_ in allfiles:
	df1 = pd.read_csv(file_)
	df2 = df1[['track','purpose','person']]
	df3 = df2.replace({'purpose':mapping})
	df4 = df3.convert_objects(convert_numeric=True) 
	df5 = df4[df4.purpose < 2]     	
	df6 = df5.drop_duplicates(subset=['track'])
	df6['fractionebike'] = df6["purpose"].mean()
	df6.to_csv(file_)
	del df1,df2,df3,df4,df5,df6
 
for file_ in allfiles:
	columns = ['','track','purpose','person','fractionebike']
	df1 = pd.read_csv(file_)    	
	df2 = df1.drop_duplicates(subset=['person'])
	df2.to_csv('C:/Users/Aaron Korver/Desktop/GIMA/Module 2/joinedtracks/joinedtracks/joinedtracks/outputloop.csv',mode='a',header=columns)
	del df1,df2
	
df1 = pd.read_csv('C:/Users/Aaron Korver/Desktop/ebikeusage.csv')
df2 = pd.read_csv('C:/Users/Aaron Korver/Desktop/GIMA/Module 2/personal data/outputbestandcombiindividueelenneigborhood.csv')
df3 = df2.merge(df1, left_on='person', right_on='person', how='inner')

df4 = df3.drop_duplicates(subset=['person'])
print df4
df4.to_csv('C:/Users/Aaron Korver/Desktop/nuechtdelaatste.csv')



