# Stock Data Visualizer
# This program does 3 things:
# Get input from the user
# Call api with input from user
# Generates a graph and open in the user’s default browser
#
# 10/20/2021
# Amy Snell, Eric Stranquist, Joel Spencer, Luke Manary, Michael Shamsutdinov, Stephen White

from user_input import get_user_input
from call_api import call_api
from filter_dates import filter_dates
from render_graph import render_graph
from api_key import API_KEY

def main():

  do_again = True
  while do_again:
    #get user input
    inputs = get_user_input()
    # print('\ninputs = \n', inputs)

    #make api call
    api_data = call_api(inputs, API_KEY)
    # print('\napi_data = \n', api_data)

    #filter out unwanted dates
    filtered_api_data = filter_dates(api_data, inputs)
    # print('\nfiltered_api_data = \n', filtered_api_data)

    if filtered_api_data:
      #render graph in browser
      # print("FILTERED DATA FROM INSIDE IF", filtered_api_data)
      # print("test")
      render_graph(filtered_api_data, inputs)
    else:
      print("An unexpected error occurred...")
      # render_default()
      pass
    go_again = input('Would you like to see more stock data? (Y/N): ')
    go_again = go_again.upper()
    if (go_again == 'Y'):
      do_again = True
    else:
      do_again = False
      

main()
