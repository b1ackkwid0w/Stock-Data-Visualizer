# Stock Data Visualizer
# This program does 3 things:
# Get input from the user
# Call api with input from user
# Generates a graph and open in the user’s default browser
#
# 10/20/2021
# Amy Snell, Eric Stranquist, Joel Spencer, Luke Manary, Michael Shamsutdinov, Stephen White

from functions.user_input import *
from functions.call_api import *
from functions.render_graph import *

API_KEY = "NDN2S8ZUZVMFC79X"

def main():
  print('Stock Data Visualizer\n-----------------------')

  #get user input
  inputs = get_user_input()
  print('inputs = ', inputs)

  #make api call
  api_data = call_api(inputs, API_KEY)
  print('api_data = ', api_data)

  #render graph in browser

main()