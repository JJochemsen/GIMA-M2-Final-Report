#Import required libraries
from scipy import stats
import numpy as np
import pandas as pd
import pylab
#Load CSV main file
df1 = pd.read_csv('C:\Users\Aaron Korver\Desktop\GIMA\Module 2\joinedtracks\joinedtracks\eindbestandjeej.csv')
#Filters out variables that are going to be used (can be replaced by other by changing to column header name)
df2 = df1[['WOZ','Utilitarian']]
#Filters out rows with empty values (in order to ensure equal array size)
df3 = df2[df2>0].dropna()
#Option to conditionally filter out outliers (in this case all neighborhoods with unrealistic WOZ-average values)
dfFilter = df3[df3['WOZ'] <= 750]
#Declare which variable is the X-variable
x = dfFilter['Utilitarian']
#Declare which variable is the Y-variable
y = dfFilter['WOZ']

#Optional: calculate spearmans rho + p value
#spearman = stats.spearmanr(x,y)
#print spearman

#Calculate and print basic linear statistics
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x, y)
print "slope, intercept, r_value, p_value, slope_std_error"
print slope, intercept, r_value, p_value, slope_std_error
#Calculate linear graph
predict_y = intercept + slope * x
pred_error = y - predict_y
degrees_of_freedom = len(x) - 2
residual_std_error = np.sqrt(np.sum(pred_error**2) / degrees_of_freedom)
#Plot linear graph
#Plot linear graph
#X-label
pylab.xlabel('% Non-Western Foreigners (in neighborhood)')
#Y-label
pylab.ylabel('Mean trip length (in minutes per case)')
#Title
pylab.title('Mean trip length versus Non-Western Foreigners %')
pylab.plot(x, y, 'o')
pylab.plot(x, predict_y, 'k-')
pylab.show()

