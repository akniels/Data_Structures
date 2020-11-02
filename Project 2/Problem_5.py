#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 14:05:51 2020

@author: akniels1
"""

import hashlib
from datetime import datetime
from pytz import timezone


class Block:

    def __init__(self,  data, timestamp, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(data, timestamp)

    def calc_hash(self, value , time ):
          sha = hashlib.sha256()
          
          string = str(value) + str(time)
    
          hash_str = string.encode('utf-8')
    
          sha.update(hash_str)
    
          return sha.hexdigest()

class block_linked_list:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append_block(self, value, time=datetime.now(tz=timezone('GMT')).strftime("%m/%d/%Y, %H:%M:%S"), previous_hash=0 ):
        if self.head is None:
            self.head = Block(value, time, previous_hash)
            self.tail = self.head
            
        else:
            previous = self.tail
            block = Block(value, time, previous)
            self.tail = block 
        return
    
    def __str__(self):
        cur_tail = self.tail
        out_string = ""
        while cur_tail:
            out_string += str(cur_tail.data)+ " - " + str(cur_tail.hash)+ " -> "
            cur_tail = cur_tail.previous_hash
        return out_string
    

# Test case 1 #


b = block_linked_list()

b.append_block("New Data" )
b.append_block("This is new Data")
b.append_block("To be or not to be")

b.append_block("full data")

b.append_block("data t")

print(b.__str__())


# Test case 2 #

new_list = block_linked_list()

new_list.append_block("")
new_list.append_block("")
new_list.append_block("")
new_list.append_block("")
new_list.append_block("")

print(new_list.__str__())



## Test Case 3##

new_list = block_linked_list()

new_list.append_block("a")
new_list.append_block("aaaaa")
new_list.append_block("aaaaaaaaa")
new_list.append_block("aaaa")
new_list.append_block("a")

print(new_list.__str__())