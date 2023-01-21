#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    unsorted_num = arr[len(arr) - 1]
    for i in range((len(arr) - 2), -1, -1):
        if unsorted_num < arr[i]:
            arr[i + 1] = arr[i]
            for item in arr:
                print(item, end=" ")
            print()
        else:
            arr[i + 1] = unsorted_num
            for item in arr:
                print(item, end=" ")
            print()
            break
    if arr[0] > unsorted_num:
        arr[0] = unsorted_num
        for item in arr:
            print(item, end=" ")
        print()
         
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
