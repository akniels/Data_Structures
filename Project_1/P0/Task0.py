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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

incoming_number, answering_number, time = texts[0][0], texts[0][1], texts[0][2]
incoming_numberp, answering_numberp, timep, secondsp = calls[-1][0], calls[-1][1], calls[-1][2], calls[-1][3]
print(f"First record of texts, {incoming_number} texts {answering_number} at time {time}")
print(f"Last record of calls, {incoming_numberp} calls {answering_numberp} at time {timep}, lasting {secondsp} seconds")

"""
 Big  Notation Worst Case Secenario
 

 
 
 O(2)
 there are 2 steps of reading the variables and this is constant

This is most effeicent when you read the first and last row with one line 
and directly refer to the first and last line 
"""