#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(clouds):
    N = len(clouds)
    idx = 0
    jumps = 0
    while idx < N - 1:
        if idx + 2 < N and clouds[idx + 2] == 0:
            jumps += 1
            idx = idx + 2
        elif clouds[idx +1] == 0:
            jumps += 1
            idx = idx + 1
        else:
            return -1
        # print(idx)
    return jumps
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
