#imports
from datetime import datetime, timedelta
from constants import GRAPH, FUNCTION

#this function collects and tests user data for the queries - stock symbol, chart type, time series, start date and end date
def get_user_input():
    #initializing values
    stock_symbol = "" #initializing stock symbol
    chart_type = "1" #initializing chart type
    time_series = "1" #initializing time series
    start_day = "1900-01-01" #initiazing start date at Jan 1 1900
    today = datetime.now().date() #initiazing end date obj as today
    end_date_obj = today
    end_day = datetime.strftime(today, "%Y-%m-%d") #converting end date to string
    return_dict = {}    # default return value

    print('Stock Data Visualizer\n-----------------------')
    
        
    #stock symbol input
    while True:
        try: 
            stock_symbol = input('Enter the Stock Symbol you are looking for: ')
            stock_symbol = stock_symbol.upper()
            if stock_symbol == "": #testing if user input is null
                print('Stock Symbol Example: GOOGL')    #input example due to null input
                raise Exception
            break
        except Exception: #catching errors
            print('\nInvalid Entry. Please try again...')
            continue

    #graph type input
    while True:
        try: 
            print('\nGraph Types\n------------\n1. Bar\n2. Line\n')
            graph_type = int(input('Enter the Graph Type you want (1, 2): '))
            if graph_type < 1 or graph_type > 2:
                raise Exception
            break
        except Exception: #catching invalid input
            print('\nInvalid entry: Please try again...')
            continue

    #time series input
    while True:
        try: 
            print('\nTime Series\n-----------\n1. Intraday (past 60 days)\n2. Daily\n3. Weekly\n4. Monthly')
            time_series = int(input("Enter time series option (1, 2, 3, 4): "))
            if time_series < 1 or time_series > 4:
                raise Exception
            break
        except Exception: #catching invalid input
            print('\nInvalid entry: Please try again...')
            continue

    
        
    #start date input
    while True:
        try: 
            start_day = input('\nEnter the start date (YYYY-MM-DD): ') 
            start_date_obj = datetime.strptime(start_day, "%Y-%m-%d") #converting string input to date object and formmating
            start_date = start_date_obj.date() #removing time from date object
            if time_series == 1:    # if intraday
                earliest_date = today-timedelta(days=60) # 60 days prior to today
                if start_date < earliest_date:
                    raise IOError
            break
        except IOError: # specific error for date out of bounds
            print('\nEarliest date for intraday is: ' + datetime.strftime(earliest_date,'%Y-%m-%d'))
            continue
        except Exception: #raising exception for date format error
            print('\nInvalid entry. Please try again...')
            continue
        
    #end date input
    while True:
        try:
            end_day = input('Enter the end date (YYYY-MM-DD): ')
            end_date_obj = datetime.strptime(end_day, "%Y-%m-%d")   # input string to date object
            if end_date_obj <= start_date_obj:  # raise exception if end date is before start date
                raise IOError
            break
        except IOError:
            print('\nEnd Date must be after Start Date. Current Start Date is ' + datetime.strftime(start_date,'%Y-%m-%d'))
            continue
        except Exception:   # catching other error like date formats
            continue

    end_date = end_date_obj.date() #removing time from date objectls

    graph_type_str = GRAPH[str(graph_type)]             # converting ints to proper strings for queries
    time_series_str = FUNCTION[str(time_series)]        # converting ints to proper strings for queries
    

    return_dict = {
        "stock_symbol": stock_symbol,       # string
        "graph_type": graph_type_str,       # string
        "time_series": time_series_str,     # string
        "start_date": start_date,           # datetime object
        "end_date": end_date                # datetime object
    }
        
    #returning string values to send for queries
    return return_dict

    
