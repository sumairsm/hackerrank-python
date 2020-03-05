#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s.split()
    c = []
    for i in s:
        c.append(i[0].upper())
        c.append(i[1:])

    return ' '.join(c)

if __name__ == '__main__':
  #  fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    print(result)

#    fptr.write(result + '\n')

 #   fptr.close()
