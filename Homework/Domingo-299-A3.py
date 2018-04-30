"""CS299
    HW3
    @author: James Domingo
    4/30/18
    Program Used: PyCharm"""

from pandas import DataFrame, Series
from xml.etree  import ElementTree
import pandas as pd


#csv_data holds SP500_ind.csv file
csvTemp = pd.read_csv('SP500_ind.csv')

#Printing the XML file
xmlTemp = ElementTree.parse('SP500_symbols.xml')
root = xmlTemp.getroot()

#Creates a list for values from xml file
xmlList = []
for child in root:
    xmlList.append(child.attrib)

#xml & csv files into a dataframe
csv_data = DataFrame(csvTemp)
xml_dict = DataFrame(xmlList)

#Creating a check needed for the assignment
tickerList = xml_dict['ticker']
checkTicker = csv_data['Symbol']
ticker = 'A'

#Function that finds the ticker
def ticker_find(xml_dict, ticker):
    #Check is the boolean for the function.
    check = 0
    for child in root:
        if ticker == child.attrib["ticker"]:
            name = child.attrib["name"]
    #If it finds the ticker, it'll return the name of the ticker
    for i in range(len(checkTicker)):
        if ticker == checkTicker[i]:
            check = True
    #If it can't find the ticker, it'll return the statement 'No data in SP500'
    if check != True:
        name = 'No data in SP500'
    return name

#Prints out the name of the ticker.
print(ticker_find(xml_dict, ticker))

#Function that finds the average opening price
def calc_avg_open(csv_data, ticker):
    totalCount = 0
    averageCount = 0
    for i in range(len(csv_data)):
        if csv_data['Symbol'][i] == ticker:
            totalCount += csv_data['Open'][i]
            averageCount += 1
    if averageCount >0:
        average = totalCount / averageCount
        return average
    else:
        average = 'Error: Average can not be calculated'
    return average

#Prints out the average opening price
print(calc_avg_open(csv_data, ticker))

#VWAP = Volume Weighted Average Price
def vwap(stock_dict, ticker):
    averageDay = 0
    averageVolume = 0
    for i in range(len(csv_data)):
        if csv_data['Symbol'][i] == ticker:
            average = ((csv_data['High'][i] + csv_data['Low'][i] + csv_data['Close'][i]) / 3)
            averageDay += (average * csv_data['Volume'][i])
            averageVolume += csv_data['Volume'][i]

    vwap = averageDay / averageVolume
    return vwap

print(vwap(csv_data, ticker))

#For loop to show each ticker
for i in range(len(tickerList)):

    #Limits the numbers after decimals.
    tickerFinder = ticker_find(xml_dict, tickerList[i])
    if tickerFinder!= 'No data in SP500':
        tickerAvg = calc_avg_open(csv_data, tickerList[i])
        tickerVWAP = vwap(csv_data, tickerList[i])
        print('{0} {1:.4g} {2:.4g}'.format(tickerFinder, tickerAvg, tickerVWAP))
    else:
        print(tickerFinder)
