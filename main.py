# Stock Data Visualizer
# This program does 3 things:
# Get input from the user
# Call api with input from user
# Generates a graph and open in the user’s default browser
#
# 10/20/2021
# Amy Snell, Eric Stranquist, Joel Spencer, Luke Manary, Michael Shamsutdinov, Stephen White

from functions import *

def main():
    print('Stock Data Visualizer\n-----------------------')
    #call the functions
    user_data = get_user_input()
    print('userData = ', user_data)

    api_data = call_api()
    print('apiData (currently just api_key)= ', api_data)



main()