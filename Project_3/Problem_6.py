#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 14:30:31 2020

@author: akniels1
"""


import math 
def get_min_max(ints, maximum = 0, minimum = None):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    minimum = len(ints)
    for integer in ints:
       if maximum < integer and integer < minimum:
          maximum, minimum  =  integer, integer
       elif maximum < integer:
           maximum = integer
       elif integer < minimum:
           minimum = integer
       else:
           continue
    return ( minimum , maximum)

##Test Case 1
import random

l = [i for i in range(0, 10)]  
random.shuffle(l)

get_min_max(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

## Test Case 2
m = [0]  
random.shuffle(m)

get_min_max(m)



print ("Pass" if ((0, 0) == get_min_max(m)) else "Fail")


## Test Case 3
n = [i for i in range(0, 100001)]   
random.shuffle(n)




print ("Pass" if ((0, 100000) == get_min_max(n)) else "Fail")

## Test Case 4
p = []  
random.shuffle(p)




print ("Pass" if ((0, 0) == get_min_max(p)) else "Fail")



