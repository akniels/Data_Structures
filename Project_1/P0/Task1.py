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

tele_number = set()
for item in calls:
     tele_number.add(item[0])
     tele_number.add(item[1])
for item in texts:
    tele_number.add(item[0])
    tele_number.add(item[1])




#print(len(calls))
#print(len(texts))
print(f"There are {len(tele_number)} different telephone numbers in the records.")

"""
Big O Notation Worst Case Scenario

O(1 + 2n + 2x)

2 is for the set created tele_number 

2n and 2x is for the for loops based on the length of calls and texts


I could make this more efficient by reading each 
row once instead of twice and then checking if it is in the list.


"""