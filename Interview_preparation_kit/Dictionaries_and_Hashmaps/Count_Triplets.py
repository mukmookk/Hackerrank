#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
from collections import defaultdict

def countTriplets(arr, r):
    nums = defaultdict(int)
    count = 0
    for a in arr:
        nums[a] = 1
    
    for key in list(nums):
        bucket = []
        temp = nums
        for i in range(2, 4):
            pow_num = pow(key, i)
            print(pow_num, temp[pow_num])
            if temp[pow_num] != 0:
                bucket.append(temp[pow_num])
                temp[pow_num] = 0
            
                if i == 3:
                    print(bucket)
                    count += sum(bucket)
            else:
                break
        
            
                
    
    return count
        
        

if __name__ == '__main__':

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    print(countTriplets(arr, r))
