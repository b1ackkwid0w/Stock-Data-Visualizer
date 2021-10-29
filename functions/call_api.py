import requests

# calls the api given inputs
def call_api(inputs, API_KEY):
  # inputs = {
  #   "stock_symbol": string,
  #   "chart_type": string,
  #   "time_series": string,
  #   "time_interval": string,
  #   "start_date": string,
  #   "end_date": string
  # }
  # Required fields based on 'function': (//optional: only including relevant fields)
  #   TIME_SERIES_INTRADAY --> function, symbol, interval, apikey   //optional: outputsize
  #   TIME_SERIES_DAILY --> function, symbol, apikey                //optional: outputsize
  #   TIME_SERIES_WEEKLY --> function, symbol, apikey               //optional: n/a
  #   TIME_SERIES_MONTHLY --> function, symbol, apikey              //optional: n/a

  # create url string
  url = 'https://www.alphavantage.co/query?function=' + inputs['time_series'] + '&symbol=' + inputs['stock_symbol']

  # if time_series is 'TIME_SERIES_INTRADAY' then add the required 'interval' field to the url string
  if inputs['time_series'] == 'TIME_SERIES_INTRADAY':
    url = url + '&interval=' + inputs['time_interval']
    url = url + '&outputsize=full'  # request more than the last 100 data points
  elif inputs['time_series'] == 'TIME_SERIES_DAILY':
    url = url + '&outputsize=full'  # request more than the last 100 data points

  # add API_KEY to url string
  url = url + '&apikey=' + API_KEY

  # make request using url string
  r = requests.get(url)

  # parse response from json to dictionary
  data = r.json()

  # check json status
  # print(r.status_code)
  if r.status_code == 200:
    print('api call success! ', r.status_code)
    return data
  else:
    print('Error: ', r.status_code)
    return {}