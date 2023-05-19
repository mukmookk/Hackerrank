#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#
from collections import defaultdict

def checkMagazine(magazine, note):
    strings = defaultdict(int)
    answer = "Yes"
    for m in magazine:
        strings[m] += 1
    
    for n in note:
        if strings[n] == 0:
            answer = "No"
            break
        elif strings[n] > 0:
            strings[n] -= 1
    
    print(answer)
        

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
