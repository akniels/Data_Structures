#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 15:07:42 2020

@author: akniels1
"""
import copy 
from time import time

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    
    def to_list(self):
        node = self.head
        node_list = []
        while node:
            node_list.append(node.value)
            node = node.next
        return node_list
    
    def duplicate(self):
        copy = LinkedList()
        node1 = self.head
        while node1:
            node = node1.value
            copy.append(node)
            node1 = node1.next
        return copy    
    
def union( llist_1, llist_2):
        # Your Solution Here
    if llist_1.head is None and  llist_2.head is None:
        return []
        
    else: 
        first_list = llist_1.duplicate()
        
        node1 = first_list.head
        while node1.next is not None:
            node1 = node1.next
        second_list = llist_2.duplicate()
        node1.next = second_list.head
        new_list = first_list.to_list()   
        union_list = list(dict.fromkeys(new_list))
        union_link = LinkedList()
        iterator = 0
        union_node = first_list.head 
        while union_node:
            value = union_node.value
            if value == union_list[iterator] and iterator < (len(union_list)-1):
                union_link.append(value)
                iterator +=1
            union_node = union_node.next
            
       
        
    return union_link.to_list()
        
       
    
def intersection(llist_1, llist_2):
        # Your Solution Here
        
    if not llist_1 and not llist_2:
        return []
         
    first_list = llist_1.duplicate()
    node1 = first_list.head

    intersection_link = LinkedList()
    intersection_list = [value for value in llist_1.to_list() if value in llist_2.to_list()] 
    intersection_list = list(dict.fromkeys(intersection_list)) 
    if len(intersection_list) == 0:
        return []
    else: 
        iterator = 0
        while node1:
            value = node1.value
            if int(value) == int(intersection_list[iterator]) and iterator < (len(intersection_list)) :
                intersection_link.append(value)
                iterator +=1
            node1 = node1.next
          
            
            
    return intersection_link.to_list()



# Test case 1
t0 = time()

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

t1 = time()

print('function vers1 takes {} seconds.'.format(t1-t0))

# Test case 2
t2 = time()
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
t3 = time()

print('function vers1 takes {} seconds.'.format(t3-t2))



# Test case 3 #
t2 = time()
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [1,7,8,9,11,21,1]
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))
t3 = time()

print('function vers1 takes {} seconds.'.format(t3-t2))

# Test case 4 #
t2 = time()
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print (union(linked_list_7,linked_list_8))
print (intersection(linked_list_7,linked_list_8))
t3 = time()

print('function vers1 takes {} seconds.'.format(t3-t2))