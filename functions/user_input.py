#imports
from datetime import datetime
from enum import Enum

GRAPH = {
    '1': 'bar',
    '2': 'line'
}
FUNCTION = {
    '1': 'TIME_SERIES_INTRADAY',
    '2': 'TIME_SERIES_DAILY',
    '3': 'TIME_SERIES_WEEKLY',
    '4': 'TIME_SERIES_MONTHLY'
}
INTERVAL = {
    '1': '1min',
    '2': '5min',
    '3': '15min',
    '4': '30min',
    '5': '60min'
}

#this function collects and tests user data for the queries - stock symbol, chart type, time series, start date and end date
def get_user_input():
    #initializing values
    stock_symbol = "" #initializing stock symbol
    chart_type = "1" #initializing chart type
    time_series = "1" #initializing time series
    start_day = "1900-01-01" #initiazing start date at Jan 1 1900
    end_date_obj = datetime.today() #initiazing end date obj as today
    end_date = end_date_obj.date() #removing time from end date object
    end_day = datetime.strftime(end_date, "%Y-%m-%d") #converting end date to string

    while True:
        try: #testing user input
            stock_symbol = input('Enter the Stock Symbol you are looking for: ')
            stock_symbol = stock_symbol.upper()
            if stock_symbol == "": #testing if user input is null
                print('Stock Symbol Example: GOOGL')    #input example due to null input
                raise Exception
        except Exception: #catching errors
            print('\nInvalid Entry. Please try again...')
            continue
        else:
            while True:
                try: #testing user input
                    print('\nGraph Types\n------------\n1. Bar\n2. Line\n')
                    graph_type = int(input('Enter the Graph Type you want (1, 2): '))
                    if graph_type < 1 or graph_type > 2:
                        raise Exception
                except Exception: #catching invalid input
                    print('\nInvalid entry: Please try again...')
                    continue
                else:
                    while True:
                        try: #testing user input
                            print('\nTime Series\n-----------\n1. Intraday\n2. Daily\n3. Weekly\n4. Monthly\n')
                            time_series = int(input("Enter time series option (1, 2, 3, 4): "))
                            if time_series < 1 or time_series > 4:
                                raise Exception
                        except Exception: #catching invalid input
                            print('\nInvalid entry: Please try again...')
                            continue
                        else:
                            while True:
                                try: #testing user input
                                    print('\nTime Interval\n-------------------\n1. 1min\n2. 5min\n3. 15min\n4. 30min\n5. 60min\n')
                                    time_interval = int(input("Enter time interval option (1, 2, 3, 4, 5): "))
                                    if time_interval < 1 or time_interval > 5:
                                        raise Exception
                                except Exception: #catching invalid input
                                    print('\nInvalid entry: Please try again...')
                                    continue
                                else:
                                    while True:
                                        try: #testing user input on start date
                                            start_day = input('\nEnter the start date (YYYY-MM-DD): ') 
                                            start_date_obj = datetime.strptime(start_day, "%Y-%m-%d") #converting string input to date object and formmating
                                            start_date = start_date_obj.date() #removing time from date object
                                        except Exception: #raising exception for date format error
                                            print('\nInvalid entry. Please try again...')
                                            continue
                                        else:
                                            while True: #starting another loop for end date
                                                try: #testing user input on end date
                                                    end_day = input('Enter the end date (YYYY-MM-DD): ')
                                                    end_date_obj = datetime.strptime(end_day, "%Y-%m-%d") #converting string input to date object and formatting
                                                    if end_date_obj <= start_date_obj: # rasining exception if end date is before start date
                                                        print('\nEnd Date must be after Start Date. Current Start Date is',start_date) #informs user of error
                                                        raise Exception
                                                except Exception: #catching other error like date formats
                                                    print('Invalid entry. Please try again...')
                                                    continue
                                                else:
                                                    end_date = end_date_obj.date() #removing time from date object
                                                    start_date_str = datetime.strftime(start_date, "%Y-%m-%d") #converting date objects to strings for queries
                                                    end_date_str = datetime.strftime(end_date, "%Y-%m-%d") #converting date objects to strings for queries
                                                    graph_type_str = GRAPH[str(graph_type)] #converting ints to strings for queries
                                                    time_series_str = FUNCTION[str(time_series)] #converting ints to strings for queries
                                                    time_interval_str = INTERVAL[str(time_interval)] # Convert ints to strings for queries

                                                    return_dict = {
                                                        "stock_symbol": stock_symbol,
                                                        "graph_type": graph_type_str,
                                                        "time_series": time_series_str,
                                                        "time_interval": time_interval_str,
                                                        "start_date": start_date_str,
                                                        "end_date": end_date_str
                                                    }

                                                    #returning string values to send for queries
                                                    return return_dict