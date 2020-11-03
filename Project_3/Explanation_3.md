## Rearrange Array Elements

For this problem there were two problems were were trying to solve, first to sort the list, and second to split the data into two halves. To first sort the data a merge sort appeared to be the best option because it gives us the efficiency of O(logn) this is done by splitting the data into two using recursive functions and then sorting the data one by one. THe second part involved sp;litting the data into two by using a while loop to pop the smallest items first and appending it to the two numbers.

## Time Complexity

Rearrange_digit O(1)

There is only one step in the problem, hover the function called is more complex.

split_in_two = O(n)

this is O(n) complexity because the pop function will have to traverse the whole list.

msort  = O(logn)

msort is O(Nlogn) because it performs a mergesort.

## Space Complexity 

split in Two = O(2n)

The space complexity is 2n because there are two string items created which length will be based on N number of characters dependant on the length.

msort  = O(8n)


The space complexity is 8n because two lists are created with 4 bytes for integers. the n is dependant on the number of items found in the list. 

Merge = O(4n)

Merge creates a list in the function built of integers and is based on the Len n of the list.


## Recources used

I refernce the Mergesort walkthrough found in the Udacity course but created the sort based off the needs of this problem.

## Sources

https://classroom.udacity.com/nanodegrees/nd256/parts/da17de0f-f834-46f8-bb48-ee2705d95dc4/modules/b849517a-9ee0-4fa8-8e22-b49fd084a350/lessons/902b8515-a2ef-485b-9543-f9a9aad9843f/concepts/50d8c2cc-7ac3-41c3-a9dd-4e407bb6e8e0

