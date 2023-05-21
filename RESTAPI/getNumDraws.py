#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getNumDraws' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER year as parameter.
#
import requests
import json

# def getNumDraws(year):
#     url1 = "https://jsonmock.hackerrank.com/api/football_matches?year=" + str(year)
#     response = requests.get(url1)
#     result1 = json.loads(response.content)
#     curr_1 = 1
#     total_page_url_1 = result1['total_pages']
    # total = 0
    # for i in range(0, 12):
    #     url1 = "https://jsonmock.hackerrank.com/api/football_matches?year={0}&team1goals={1}&team2goals={1}".format(year, i, i)
    #     response1 = requests.get(url1)
    #     result1 = json.loads(response1.content)
    #     total += result1['total']
    
    # return total


def getNumDraws(year):
    total = 0
    for i in range(0, 12):
        url1 = "https://jsonmock.hackerrank.com/api/football_matches?year={0}&team1goals={1}&team2goals={1}".format(year, i, i)
        response1 = requests.get(url1)
        result1 = json.loads(response1.content)
        total += result1['total']

    return total
    
def getNumDraws(year):
    answer = 0
    for goal in range(0, 1):
        url_goals = "https://jsonmock.hackerrank.com/api/football_matches?\
            year="+str(year) +\
            "&team1goals="+str(goal) +\
            "&team2goals="+str(goal)
        response_goal = requests.get(url_goals)
        result_goal = json.loads(response_goal.content)
        pages = result_goal['total_pages']
        
        
    return answer