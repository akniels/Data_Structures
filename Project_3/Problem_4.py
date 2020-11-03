#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 14:46:34 2020

@author: akniels1
"""

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    index_traverser = 0 
    front = 0
    back = len(input_list) - 1
    
    while index_traverser <= back:
        if input_list[index_traverser] == 0:
            input_list[index_traverser] = input_list[front]
            input_list[front] = 0
            index_traverser+=1
            front +=1
        elif input_list[index_traverser] == 2 :
            input_list[index_traverser] == input_list[back]
            input_list[back] = 2
            back -= 1
        else:
            index_traverser +=1
    return input_list
            

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([0])
test_function([])
test_function([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
test_function([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])