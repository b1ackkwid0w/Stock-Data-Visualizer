# Stock Data Visualizer
# This program asks the user to enter the stock symbol for the company they want data for
# Asks the user for the chart type they would like
# Asks the user for the time series function they want the api to use
# Asks the user for the beginning date in YYYY-MM-DD format
# Asks the user for the end date in YYYY-MM-DD format (The end date should not be before the begin date) 
# Generates a graph and open in the user’s default browser
#
# 10/20/2021
# Amy Snell, Eric Stranquist, Joel Spencer, Luke Manary, Michael Shamsutdinov, Stephen White

from datetime import datetime


#this function collects and tests user data for the queries - stock symbol, chart type, time series, start date and end date
def GetUserData():

#initializing values
    stockSymbol = "" #initializing stock symbol
    chartType = 1 #initializing chart type
    timeSeries = 1 #initializing time series
    startDay = "1900-01-01" #initiazing start date at Jan 1 1900
    endDateObj = datetime.today() #initiazing end date obj as today
    endDate = endDateObj.date() #removing time from end date object
    endDay = datetime.strftime(endDate, "%Y-%m-%d") #converting end date to string

    while True:
        try: #testing user input
            stockSymbol = input('Enter the Stock Symbol you are looking for: ').upper()
        except stockSymbol == "": #testing if user input is null
            print('Stock Symbol Example: GOOGL')
            continue
        except Exception: # catching errors
            print('\nInvalid Entry. Please try again...')
            continue
        else:
            while True:
                try: #testing user input
                    print('\nChart Types\n------------\n1. Bar\n2. Line\n')
                    chartType = int(input('Enter the Chart Type you want (1, 2): '))
                    if chartType <= 0:
                        raise Exception
                    if chartType >= 3:
                        raise Exception
                except Exception: #catching invalid input
                    print('\nInvalid entry: Please try again...')
                    continue
                else:
                    while True:
                        try: #testing user input
                            print('\nSelect the Time Series of the chart you want to Generate\n------------------------------------------------------------\n1. Intraday\n2. Daily\n3. Weekly\n4. Monthly\n')
                            timeSeries = int(input("Enter time series option (1, 2, 3, 4): "))
                            if timeSeries < 1:
                                raise Exception
                            if timeSeries > 4:
                                raise Exception
                        except Exception: #catching invalid input
                            print('\nInvalid entry: Please try again...')
                            continue
                        else:
                            while True:
                                try: #testing user input on start date
                                    startDay = input('\nEnter the start date (YYYY-MM-DD): ') 
                                    startDateObj = datetime.strptime(startDay, "%Y-%m-%d") #converting string input to date object and formmating
                                    startDate = startDateObj.date() #removing time from date object
                                except Exception as e1: #raising exception for date format error
                                    print('\nInvalid entry. Please try again...')
                                    continue
                                else:
                                    while True: #starting another loop for end date
                                        try: #testing user input on end date
                                            endDay = input('Enter the end date (YYYY-MM-DD): ')
                                            endDateObj = datetime.strptime(endDay, "%Y-%m-%d") #converting string input to date object and formatting
                                            if endDateObj <= startDateObj: # rasining exception if end date is before start date
                                                print('\nEnd Date must be after Start Date. Current Start Date is',startDate) #informs user of error
                                                raise Exception
                                        except Exception: #catching other error like date formats
                                            print('Invalid entry. Please try again...')
                                            continue
                                        else:
                                            endDate = endDateObj.date() #removing time from date object
                                            startDateStr = datetime.strftime(startDate, "%Y-%m-%d") #converting date objects to strings for queries
                                            endDateStr = datetime.strftime(endDate, "%Y-%m-%d") #converting date objects to strings for queries
                                            chartTypeStr = str(chartType) #converting ints to strings for queries
                                            timeSeriesStr = str(timeSeries) #converting ints to strings for queries

                                            #printing values and types for debugging purposes - will take out later
                                            print ('Stock Symbol: ', stockSymbol, 'Chart Type: ',chartTypeStr,'Time Series: ',timeSeriesStr,'Start Date: ',startDateStr,'End Date: ',endDateStr)

                                            symbol_type = type(stockSymbol)
                                            chart_type = type(chartTypeStr)
                                            timeSeries_type = type(timeSeriesStr)
                                            startDate_type = type(startDateStr)
                                            endDate_type = type(endDateStr)

                                            print(symbol_type,chart_type,timeSeries_type,startDate_type,endDate_type)

                                            #returning string values to send for queries
                                            return stockSymbol, chartTypeStr, timeSeriesStr, startDateStr, endDateStr


def main():
    print('Stock Data Visualizer\n-----------------------')
    GetUserData()


main()
