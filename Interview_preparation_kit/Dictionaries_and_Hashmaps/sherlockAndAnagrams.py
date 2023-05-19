#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
from collections import defaultdict
def sherlockAndAnagrams(s):
    answer = 0
    subsets = defaultdict(int)
    for i in range(len(s)):
        for j in range(1, len(s) - i + 1):
            sub = ''.join(sorted(s[i:i+j]))
            if subsets[sub] > 0:
                answer += subsets[sub]
            subsets[sub] += 1
    print(subsets)
    return answer
            
            
if __name__ == '__main__':

    q = int(input().strip())

    for _ in range(q):
        s = input()

        result = sherlockAndAnagrams(s)


