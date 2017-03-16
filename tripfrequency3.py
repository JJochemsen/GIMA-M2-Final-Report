import pandas as pd
df1 = pd.read_csv('C:/Users/Aaron Korver/Desktop/GIMA/Module 2/joinedtracks/joinedtracks/utilitarianeindbestand.csv')
df2 = pd.read_csv('C:/Users/Aaron Korver/Desktop/GIMA/Module 2/joinedtracks/joinedtracks/outputtotaal.csv')
df3 = df2.merge(df1, left_on='person', right_on='person', how='inner')
print df3
df3.to_csv('C:/Users/Aaron Korver/Desktop/GIMA/Module 2/joinedtracks/joinedtracks/eindbestandjeej.csv')
