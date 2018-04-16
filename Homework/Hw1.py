# CS299
# HW1
# @Author: James Domingo

import math
import statistics
import numpy as np
import random

ListA = [1, 2, 3, 4, 5]
ListB = [2, 4, 5, 6, 8, 9]
ListofNums = [4, 5, 6, 10]


# Number 1

def merge(ListA, ListB) :

    newList = ListA + ListB
    sortedList = sorted(newList)

    return sortedList


print(merge(ListA, ListB))


# Number 2

def summaryStatistics(ListofNums):

    maxValue = np.max(ListofNums)
    minValue = np.min(ListofNums)
    meanValue = np.mean(ListofNums)
    stdev = np.std(ListofNums)
    median = np.median(ListofNums)
    perc75 = np.percentile(ListofNums, 75)
    perc25 = np.percentile(ListofNums, 25)

    return {'max': maxValue,
            'min': minValue,
            'mean': meanValue,
            'stdev': stdev,
            'median': median,
            'perc75': perc75,
            'perc25': perc25}


print(summaryStatistics(ListofNums))


# Number 3

def scaleToDigits(ListOfNums):
    ListOfNums.sort()
    min = ListofNums[0]
    max = ListofNums[(len(ListofNums)) - 1]
    newList = []
    for x in (ListOfNums):
        newList.append((x - min) / (max - min))

    return newList


ListofNums = [random.randint(1, 10) for i in range(10)]
print(ListofNums)
print(scaleToDigits(ListofNums))