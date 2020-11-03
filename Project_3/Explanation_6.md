# Max and Min of an Unsorted Array

In order to meet the requirement of this assignment, the Min and max needed to be found within one traversal of an array. In order to do so a maximum and minimum had to be found one traversal of an array. In order to do so, I first initiated the data within the definition (min and max both at 0 ). After that, I did one iteration over the list comparing the data to the min and minimum and maximum and replacing if the number was less than the minimum or greater than the maximum.

## Time Complexity

get_min_max = O(1 + n)

The 1 represents the initiation of the minimum. We could put it up in the definition with a really high nunber, however, one could alawys put it up in the funtiopn definition and eliminate that step.

## Space Complexity

get_min_max = O(8)

There are two numbers that are createed both with the space of 4 bytes. Therefore the space complexity is 8.

