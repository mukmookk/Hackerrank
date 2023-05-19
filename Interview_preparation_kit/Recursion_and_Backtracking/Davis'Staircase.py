import math
import os
import random
import re
import sys

#
# Complete the 'stepPerms' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
def recursion(depth, n, memo):
    if depth == n:
        return 1
    elif depth > n:
        return 0
    
    if memo[depth] != -1:
        return memo[depth]
    count = 0
    for i in range(1, 4):
        count += recursion(depth + i, n, memo)
        
    memo[depth] = count
    
    return count
    
def stepPerms(n):
    memo = [-1] * (n + 1)
    return recursion(0, n, memo)
    
if __name__ == '__main__':

    s = int(input().strip())

    for s_itr in range(s):
        n = int(input().strip())

        res = stepPerms(n)
        print(res)