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

O(5 + 1n^3 + 1x^2 + 1y^2+ x(log(x)))



5 represents the 5 valiables created in the algorithm (3 lists, two sets)

1n^3 represents the first for loop iterating over texts. This item is cubed because
one must check if the item is not in incoming text or outgoing text and the worse case is the item 
as long as the CSV

the  1x^2 variables represent the loop iteration over calls. This item is squared because
the worst case scenario is the incoming call is just as long as the call csv

the  1y^2 variables represent the  second loop iteration over calls. This item is squared because
the worst case scenario is the master list is just as long as the call csv



xlog(x) is for the sorting function in the print statement

"""