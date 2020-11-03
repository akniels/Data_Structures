#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 16:35:30 2020

@author: akniels1
"""

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    rear_dig = split_in_two(input_list)
    
    return rear_dig
    
    
def split_in_two(sorted_list, left="", right = ""):
    
    if len(sorted_list ) <= 1 :
        return sorted_list
    
    else: 
        slist = msort(sorted_list)
            
        while len(slist) > 0:
            if len(left) ==len(right):
                left = left + str(slist.pop())
            else:
                right = right + str(slist.pop())
        return [int(left),int(right)]
    
   

   
def msort(input_list):
    
    if len(input_list) <= 1:
        return input_list
    
    
    left = msort(input_list[:len(input_list)//2])
    right = msort(input_list[len(input_list)//2:])
    
    return merge(left, right)

def merge(left, right, r_index = 0, l_index = 0):
    merge = []
    while len(right) > r_index and len(left) >l_index:
        if left[l_index] > right[r_index]:
            merge.append(right[r_index])
            r_index += 1
            
        else:
            merge.append(left[l_index])
            l_index+= 1
    
    merge+= left[l_index:]
    merge+= right[r_index:]
    
    return merge

    
    
            
    
    

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")




test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[1,9,2,8,3,7,4,6,5], [97531, 8642]])
test_function([[0], [0]])
test_function([[], []])



#print(rearrange_digits([4, 6, 2, 5, 9, 8]))




