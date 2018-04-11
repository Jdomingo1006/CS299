from pandas import Series, DataFrame
import pandas as pd
import random

"""obj = Series([4, 7, -5, 3])
print(obj)
print(obj.index)
print(obj.values)"""

"""obj2 = Series([4, 3, 2, 1], index = ['d', 'b', 'c', 'a'])
print(obj2)
print(obj2.index)
print(obj2.values)
print(obj2['c'])
print(obj2[:3])
print(obj2.d)"""

"""obj3 = Series({'a': 10, 'b': 5, 'c': 30 })
print(obj3)
print(obj3 **2)
print('a' in obj3)"""

"""sdata = {'Texas': 10, 'Ohio': 20, 'Oregon': 15, 'Utah': 18}
states = ['Texas', 'Ohio', 'Oregon', 'Iowa', 'Utah']
obj4 = Series(sdata, index=states)
print(obj4)
print(pd.isnull(obj4))
print(pd.notnull(obj4))
print(obj4[obj4.notnull()])"""

"""sdata1 = {'Texas': 10, 'Ohio': 20, 'Oregon': 15, 'Utah': 18}
states1 = ['Texas', 'Ohio', 'Oregon', ]
sdata = {'Texas': 10, 'Ohio': 20, 'Oregon': 15, 'Utah': 18}
states = ['Texas', 'Ohio', 'Oregon', 'Utah']
obj5 = Series(sdata1, index = states1)
obj4 = Series(sdata, index=states)
print(obj4)
print(obj5)
print(obj4 + obj5)"""

"""sdata = {'Texas': 10, 'Ohio': 20, 'Oregon': 15, 'Utah': 18}
states = ['Texas', 'Ohio', 'Oregon', 'Iowa']
obj4 = Series(sdata, index=states)
obj4.name = 'population'
obj4.index.name = 'state'
print(obj4)
obj4.index = ['California', 'New York', 'Pennsylvania', 'Georgia']
print(obj4)
print(obj4.index)"""

#Actvity 3
"""RandomList = [random.randint(1,100) for i in range(10)]
values = Series(RandomList, index = range(1, 11))
print(values[-4:])
values**2
print(values[-4:])
rands = [random.randint(1,100) for _ in range(10)]
obj3 = Series(rands, index=range(1, 11))
print(obj3[-4:])
obj4 = obj3**2
print(obj4[-4:])"""

#DataFrame
"""data = {
'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
'year': [2000, 2001, 2002, 2001, 2002],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9]
}
#Reordered alphabetical order
#Pop --> state --> year
frame = DataFrame(data)
frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['A', 'B', 'C', 'D', 'E'])
print(frame)
print(frame2)"""

#Test
list = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]
print(list[2:]) #3, 4, 5
print(list[:2]) #1, 2
print(list[:-2])#1, 2, 3
print(list[-2:])#4, 5
y = (list + list + list2)
x = sorted(y)
print(x[4:])