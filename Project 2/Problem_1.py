#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 17:54:48 2020

@author: parallels
"""

class LRU_Cache(object):

    def __init__(self, limit):
        self.limit = limit
        self.cache_key = [0 for _ in range(limit)]
        self.cache_value = [0 for _ in range(limit)]

    def enqueue(self,key,  value):
        if self.limit == len(self.cache_key):
            self.full_cache_handler()
        self.cache_key.insert(0, key)
        self.cache_value.insert(0, value)


    def dequeue(self):
        key = self.cache_key.pop()
        value = self.cache_value.pop()
        return key, value 
    
    def get(self, key):
        if key in self.cache_key:
            value  = self.cache_value[self.cache_key.index(key)]
            key =  self.cache_key[self.cache_key.index(key)]
            self.cache_key.remove(key)
            self.cache_value.remove(value)
            self.cache_key.insert(0, key)
            self.cache_value.insert(0, value)
            return self.cache_value[self.cache_key.index(key)]
            return key, value
        else: 
            return -1

    def set(self, key, value):
        if self.cache_key == []:
            print("This cache is empty. Nothing can be added.")
            return
        elif key not in self.cache_key:
           self.enqueue(key, value)

        else:
            print("Key already present")
            return 
    
    def full_cache_handler(self):
        key, value = self.dequeue()
        return
        



## Test Case 1 ##
our_cache = LRU_Cache(5)
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print("Test Case 1")
print(our_cache.get(1) )      # returns 1
print(our_cache.get(2) )      # returns 2
print(our_cache.get(9) )     # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3)  )    # returns -1 because the cache reached it's capacity and 3 was the least recently used entry


# Test Case 2 #
new_cache = LRU_Cache(3) 

new_cache.set(1, 1);
new_cache.set(3, 3);
new_cache.set(5, 5);


print("Test Case 2")
print(new_cache.get(1) )      # returns 1
print(new_cache.get(2) )      # returns -1
print(new_cache.get(4) )        # returns - 1 

new_cache.set(4, 4) 
new_cache.set(2, 2)

print(new_cache.get(3) )      # returns -1
print(new_cache.get(4) )      # returns 4




# Test Case 3 #
new_cache = LRU_Cache(2) 

new_cache.set(11, 11);
new_cache.set(52, 52);
new_cache.set(1, 1);


print("Test Case 3")
print(new_cache.get(11) )      # returns -1
print(new_cache.get(1) )      # returns 1
print(new_cache.get(52) )        # returns  52

new_cache.set(16, 16) 
new_cache.set(56, 56)

print(new_cache.get(16) )      # returns 16
print(new_cache.get(52) )      # returns -1


# Edge Test Case #
new_cache = LRU_Cache(0) 
new_cache.set(11,11)
print(new_cache.get(16) ) 