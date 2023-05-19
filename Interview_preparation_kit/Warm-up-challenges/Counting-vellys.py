#!/bin/python3

import math
import os
import random
import re
import sys

def draw_map(path):
    temp = []
    
    level = 0
    for v in path:
        if v == 'D':
            level -= 1
        else:
            level += 1    
        temp.append(level)
        
    return temp
            

def countingValleys(steps, path):
    N = len(path)
    answer = 0
    
    maps = draw_map(path)
    idx = 0
    while idx < N:
        if maps[idx] < 0:
            while maps[idx] <= 0:
                if maps[idx] >= 0:
                    answer += 1
                idx = idx + 1
                if idx >= N:
                    break         
        else:
            idx += 1
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
