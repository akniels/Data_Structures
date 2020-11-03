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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A
list_bangalore = []
for item in calls:
    if "(080)" in str(item[0]):
        if ")" in str(item[1]):
            item[1] = item[1].split(")")[0]+")"
            if item[1] not in list_bangalore:
                list_bangalore.append(item[1])
        if "(" not in str(item[1]):
            item[1] = item[1].split(" ")[0][0:4]
            if item[1] not in list_bangalore:
                list_bangalore.append(item[1])

print("The numbers called by people in Bangalore have codes: " )

list_bangalore = sorted(list_bangalore, key=str) 
  


for number in list_bangalore:
    print(number)

# part B
numerator = 0 
denominator= 0 
for item in calls:
    if '(080)' in item[0]:
        denominator += 1 
        if '(080)' in item[1]:
            numerator += 1 

#print(len(list_bangalore))
#print(len(set(list_bangalore)))

print(f"{round(numerator/denominator*100, 2)} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

"""
Big O Notation Worst Case Scenario

PArt A Big 0 Notation

(1 + 2x + xlog(x))

1 is for the constant variable created 

2x is for the for loop iterating over calls 

xLog(x) is for the sort function 

Part B Big O Notation

(2 + 1n)

2 represents the two variables created which are constant

1n represents the for loop over the calls file

I couldnt think of a way to make this more efficient

"""

