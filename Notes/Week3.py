"""James Domingo
CS299
April 11, 2018"""


import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import math
#import matplotlib.pyplot as plt



#First Example
"""data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
'year': [2000, 2001, 2002, 2001, 2002],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['A', 'B', 'C', 'D', 'E'])
print(frame2.loc['A']) #".loc" is used to get data of row A
print(frame2.loc[:, :]) #Prints out rows and colums
frame2['DEBT']=range(5) #This is how you modify a column
print(frame2)
del frame2['DEBT'] #Deletes debt column
print(frame2)"""

#Second Example
"""data = np.arange(9).reshape(3,3)
print(data)
frame = DataFrame(data, index=['r1', 'r2', 'r3'], columns=['c1', 'c2', 'c3'])
print(frame['c1']) #prints out the column c1
frame[frame<3] = 'loser'
print(frame)"""

#Activty 4 - slide 27
"""array = np.random.random_integers(1, 100, (3, 5))
print(array)
frame = DataFrame(array, index=['a', 'b', 'c'], columns=range(1, 6)) #My option: columns=[1, 2, 3, 4, 5]
print(frame.T) #<---This is how you transpose/switch columns/index
frame = frame.T
frame[frame<40] = 0
print(frame)"""

#Activtiy 5 - Slide 33
"""array = np.random.random_integers(1, 100, (3, 5))
print(array)
frame = DataFrame(array, index=['a', 'b', 'c'], columns=range(1, 6)) #My option: columns=[1, 2, 3, 4, 5]
print(frame.T) #<---This is how you transpose/switch columns/index
frame = frame.T
frame[frame<40] = 0
print(frame)
print(frame.applymap(lambda x: math.sqrt(x)))"""

#Example 2 - Continues
"""data = np.arange(9).reshape(3,3)
print(data)
frame= DataFrame(np.arange(9).reshape(3,3), index=['a', 'a', 'b'], columns=['c1','c2','c3'])
print(frame)
def max_minus_min(x):
    return max(x)-min(x)
print(frame.apply(max_minus_min)) #Subtracts lowest value by max value (6-0, 8-2, 7-1)"""

#Continued Notes
"""from numpy import nan as NaN
data = Series([1, NaN, 2.5, NaN, 6])
print(data)
print(data.notnull())
print(data[data.notnull()])
print(data.dropna())"""

#Activity 6

"""list1 = np.random.randint(100, size=1000)
list2 = np.random.randint(100, size=1000)
list3 = np.random.randint(100, size=1000)

dictionary = {'Data 1' : np.random.randint(100, size=1000),'Data 2' : np.random.randint(100, size=1000),'Data 3' : np.random.randint(100, size=1000)}

frame = DataFrame(dictionary) ax = frame.plot(legend=True)ax.set_xlabel('Data Set') ax.set_ylabel('Random Numbers') ax.legend(loc='center left', bbox_to_anchor=(1,0.9))"""