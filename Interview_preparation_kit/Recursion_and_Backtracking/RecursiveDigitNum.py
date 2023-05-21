#!/bin/python3

import math
import os
import random
import re
import sys

# 1000000 * 100000 = 10^12

def superDigit(n, k):
    string = str(n) * k
    summedlist = list(map(int, string))    
    
    def recurring(array):
        total = sum(array)
        if total < 10:
            return total
        numlist = list(map(int, str(total)))
        return recurring(numlist)
    answer = recurring(summedlist)
    return answer
    
    
    # def recursion(n, answer):
        

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)
    
    print(result)