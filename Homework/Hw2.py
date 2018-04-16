import pandas as pd
from pandas import DataFrame, Series
import random as randomint
import matplotlib.pyplot as plt
import numpy as np
import collections

"""CS299
HW2
author: James Domingo"""

#Question 1
#See word doc or code below
"""
a. print(df)
       a  b  c 
One    0  7  3 
Two    6  2  8 
Three  5  9  4 
 
b. df[‘a']
One      0 
Two      6 
Three    5 
Name: a, dtype: int32 
 
c. df.loc[‘Two’]
a    6 
b    2 
c    8 
Name: Two, dtype: int32 
 
d. df[:2]
     a  b  c 
One  0  7  3 
Two  6  2  8 
 
e. df.iloc[:,:]
       a  b  c 
One    0  7  3 
Two    6  2  8 
Three  5  9  4 
 
f. df.iloc[:,:2]
       a  b 
One    0  7 
Two    6  2 
Three  5  9 
 
g. list(df.columns)
['a', 'b', 'c'] 
 
h. list(df.index)
['One', 'Two', 'Three'] 
 
i.df[‘b’][‘Two]
2 
 
j. list(df.iloc[2,:])
[5, 9, 4] 
 
k. df.drop(‘a’, axis=1)
       b  c 
One    7  3 
Two    2  8 
Three  9  4 
 
l. df[df.a !=5]
     a  b  c 
One  0  7  3 
Two  6  2  8 
 
m. list(df.sum(axis=0))
[11, 18, 15] 
 
n. df.iloc[:, list(df.sum(axis=0) <17)]
       a  c 
One    0  3 
Two    6  8 
Three  5  4 
 
o. df.sort_values(by=’c’)
       a  b  c 
One    0  7  3 
Three  5  9  4 
Two    6  2  8 
 
p. df.sort_values(by=’Two', axis=1)
       b  a  c 
One    7  0  3 
Two    2  6  8 
Three  9  5  4 
 
q. df.t
   One  Two  Three 
a    0    6      5 
b    7    2      9 
c    3    8      4 
 
r. (df<=2).any(axis=0)
a     True 
b     True 
c    False 
dtype: bool 
 
s. df.applymap(lambda x: x*2-1)
        a   b   c 
One    -1  13   5 
Two    11   3  15 
Three   9  17   7 
 
t. df.apply(lambda x: max(x),axis=1)
One      7 
Two      8 
Three    9 
dtype: int64
"""

#Question 2

#Used from Hw1, part b
def summaryStatistics(x):

    maxValue = np.max(x)
    minValue = np.min(x)
    meanValue = np.mean(x)
    stdev = np.std(x)
    median = np.median(x)
    perc75 = np.percentile(x, 75)
    perc25 = np.percentile(x, 25)

    return {'max': maxValue,
            'min': minValue,
            'mean': meanValue,
            'stdev': stdev,
            'median': median,
            'perc75': perc75,
            'perc25': perc25}


#Creates the 3 list of 100 random integers from 1-100
List1 = [randomint.randint(1,100) for x in range(100)]
List2 = [randomint.randint(1,100) for x in range(100)]
List3 = [randomint.randint(1,100) for x in range(100)]

#Uses summaryStatistics method to get max/min/mean/std dev/etc.
List1Data = summaryStatistics(List1)
List2Data = summaryStatistics(List2)
List3Data = summaryStatistics(List3)

#Reorganizing to list of random numbers to make it easier to plot
data = {"Data 1":List1Data, "Data 2":List2Data, "Data 3":List3Data}
dataF = DataFrame(data, index = ['max', 'min', 'mean', 'stdev', 'median', 'perc25', 'perc75'])

#Transposes data frame
dataT = (dataF.T)
print(dataT)

#Plotting
#How to label data 1, 2, and 3?
ax = dataT.plot(legend=True, xticks = range(3), style=['r+','rx','bx', 'y^', 'gv', 'b>', 'b<'], title='Summary Statistics')
ax.set_xlabel('Values')
ax.set_ylabel('Data Set')
ax.legend(loc='center left', bbox_to_anchor=(1,0.73))
plt.interactive(False)
plt.show()


#Question 3

#Source: Hw1, c. Modified to make it 0-9 nondecimal numbers
def scaleToDigits(a):

    minNumb = np.min(a)
    maxNumb = np.max(a)
    scaledList = [round((9 - 0) * (x - minNumb) / (maxNumb - minNumb)) for x in a]
    return scaledList

#Scale the list of random numbers
List1Scale = scaleToDigits(List1)
List2Scale = scaleToDigits(List2)
List3Scale = scaleToDigits(List3)


#Counter for count of numbers 0 to 9
countedList1 = collections.Counter(List1Scale)
countedList2 = collections.Counter(List2Scale)
countedList3 = collections.Counter(List3Scale)

#All three list into one dataset and made into a DataFrame
data1 = {"List 1":countedList1, "List 2":countedList2, "List ":countedList3}
data1F = DataFrame(data1)
print(data1F)

#Plotting
#Same questions with plotting as Number 2
ax=data1F.plot(legend=True, xticks = range(10), style=['r+-', 'gx-', 'b*-'], title='Frequency of Dataset')
ax.set_xlabel('Values')
ax.set_ylabel('Data Set')
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.show()