#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
from collections import defaultdict
def freqQuery(queries):
    array = defaultdict(int)
    frequency = defaultdict(int)
    result = []
    
    for query in queries:
        operation = query[0]
        element = query[1]
        if operation == 1:
            if array[element] > 0:
                frequency[array[element]] -= 1
            array[element] += 1
            frequency[array[element]] += 1
        elif operation == 2:
            if array[element] > 0:
                frequency[array[element]] -= 1
                array[element] -= 1
                frequency[array[element]] += 1
        elif operation == 3:
            if frequency[element] > 0:
                result.append(1)
            else:
                result.append(0)

    return result  
     

if __name__ == '__main__':

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)