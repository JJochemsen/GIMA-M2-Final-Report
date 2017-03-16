import pandas as pd
import glob
import os
path = "C:/Users/joach/Documents/GIMA/Module 2/joinedtracks/"
allfiles = glob.glob(os.path.join(path,"*.csv"))
for file_ in allfiles:
	df1 = pd.read_csv(file_)
	df2 = df1[['person', 'meantriplength']]
	df3 = df2.drop_duplicates(subset=['person'])
	columns = ["person", "meantriplength"]
	df3.to_csv("C:/Users/joach/Documents/GIMA/Module 2/joinedtracks/loopoutput.csv", mode='a', header=columns)
	print df3
