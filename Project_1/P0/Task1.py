#!/usr/bin/env python3
"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

text_counter = 0
list_check = []
for i in range(len(texts) - 1):
    if texts[i][0] not in list_check:
       list_check.append(texts[i][0]) 
       text_counter += 1
    if texts[i][1] not in list_check:
       list_check.append(texts[i][1]) 
       text_counter += 1
for p in range(len(calls) - 1):
    if calls[p][0] not in list_check:
       list_check.append(calls[p][0]) 
       text_counter += 1
    if calls[p][1] not in list_check:
       list_check.append(calls[p][1]) 
       text_counter += 1  



#print(len(calls))
#print(len(texts))
print(f"There are {text_counter} different telephone numbers in the records.")

"""
Big O Notation Worst Case Scenario

O(2 + 4n + 4x)

2 is for the variables created (text_counter, list_check)  

4n and 4x is for the for loops based on the length of calls and chats


I could make this more efficient by reading each 
row once instead of twice and then checking if it is in the list.


"""