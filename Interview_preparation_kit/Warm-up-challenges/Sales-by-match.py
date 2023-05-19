#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar

from collections import defaultdict
def sockMerchant(n, array):
    pair = 0
    dic = defaultdict(int)
    
    for elem in array:
        dic[elem] += 1
    for i, v in dic.items():
        if v >= 2:
            pair += v // 2
    
    return pair
            

if __name__ == '__main__':

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
