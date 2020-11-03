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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
incoming_text = []
outgoing_text = []
incoming_call = []
for text in texts:
    if text[0] not in incoming_text:
        incoming_text.append(text[0])
    if text[1] not in outgoing_text:
        outgoing_text.append(text[1])
        
        
for call in calls:
    if call[1] not in incoming_call:
        incoming_call.append(call[1])
        
master_list = set(incoming_text + outgoing_text + incoming_call)
spammers = set()
for call in calls:
    if (call[0] not in master_list):
        spammers.add(call[0])
    
print(f"These numbers could be telemarketers:",*sorted(spammers),sep='\n')    

"""
Big O Notation Worst Case Scenario

O(5 + 1n + 1x + 1x+ x(log(x)))



5 represents the 5 valiables created in the algorithm (3 lists, two sets)

1n represents the first for loop iterating over texts

the  two 1x variables represent the two for loops iteration over calls

xlog(x) is for the sotring function in the print statement

"""