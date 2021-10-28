from datetime import datetime
from functions.constants import FUNCTION

def filter_dates(api_data, inputs):
  start = inputs['start_date']
  end = inputs['end_date']

  #FUNCTION:
  # 1. intraday     } --> must also match time of day
  # 2. daily          |
  # 3. weekly         |--> same format
  # 4. monthly        |
  pattern = '%Y-%m-%d'
  if inputs['time_series'] == FUNCTION['1']: # if it's intraday
    pattern = pattern + ' %H:%M:%S' # adjust pattern to match time of day

  # variables for simplicity
  dates_key = list(api_data.keys())[1]  # key corresponding to the value for the list of data entries
  dates_dict = api_data[dates_key]  # make new dict to hold the dates

  # remove dates from dates_dict as specified by start and end
  for key in list(dates_dict.keys()): # list(<>.keys()) for iterating over keys. Note that dates_dict is still the entire dict of objects
    try:
      current_key = datetime.strptime(key, pattern)
      if current_key.date() < start or current_key.date() > end:
        dates_dict.pop(key)
    except Exception:
      print('exception occured on data entry: ', key)
      continue

  return dates_dict