#!/usr/bin/env python3
"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

#call_addition =0 
List_check = {}
for call in calls:
    List_check[call[0]] = List_check.get(call[0],0)+int(call[3])
    List_check[call[1]] = List_check.get(call[1],0)+int(call[3])
    
telephone_number = 0
total_time  = 0    
for key, value in List_check.items():
    if  value > total_time:
        total_time = value 
        telephone_number = key

#df = pd.DataFrame(List_check)
#df.to_csv('test.csv', index=False, header=False)
#
#print(calls[0])
#print(List_check)
#print(len(List_check)) 
#print(len(set(List_check[1])))

print(f"{telephone_number} spent the longest time, {total_time} seconds, on the phone during September 2016.")


"""
Big O Notation Worst Case Scenario

O(3 + 2n + 2x)

3 is for the constant variables created (list check, telephone_number, and total_time)

2n is for the for loop based on the call data

2x on the for loop created in the list check

I couldnt think of a way to make this more efficient. 
"""