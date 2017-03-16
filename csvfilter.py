import pandas as pd
df1=pd.read_csv("C:/Users/Aaron Korver/Desktop/GIMA/Module 2/joinedtracks/legetable.csv")
df2=df1[df1.purpose == "home"]
df3=df2[df2.accuracy < 11]
df4=df3.drop_duplicates(subset=['person'])
df4.to_csv("C:/Users/Aaron Korver/Desktop/GIMA/Module 2/joinedtracks/OutputPandas3.csv")
