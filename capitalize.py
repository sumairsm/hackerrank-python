#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    t = []
    for i in s.split():
        t = s.replace(s[0], s[0].upper())

    return ''.join(t)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    print(result)
    # fptr.write(result + '\n')

    # fptr.close()
