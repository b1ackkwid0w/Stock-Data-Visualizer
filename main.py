# Stock Data Visualizer
# This program does 3 things:
# Get input from the user
# Call api with input from user
# Generates a graph and open in the user’s default browser
#
# 10/20/2021
# Amy Snell, Eric Stranquist, Joel Spencer, Luke Manary, Michael Shamsutdinov, Stephen White

from functions.user_input import get_user_input
from functions.call_api import call_api
from functions.filter_dates import filter_dates
from functions.render_graph import render_graph
from api_key import API_KEY

def main():
  print('Stock Data Visualizer\n-----------------------')

  #get user input
  inputs = get_user_input()
  # print('\ninputs = \n', inputs)

  #make api call
  api_data = call_api(inputs, API_KEY)
  # print('\napi_data = \n', api_data)

  #filter out unwanted dates
  filtered_api_data = filter_dates(api_data, inputs)
  # print('\nfiltered_api_data = \n', filtered_api_data)

  if not filtered_api_data:
    #render graph in browser
    render_graph(filtered_api_data)
  else:
    # render_default()
    pass

main()