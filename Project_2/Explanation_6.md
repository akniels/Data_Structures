# Union and Intersection

In order to complete this problem, a few elements were needed. There needed to be a way to create a copy of a linked list. I first tried running my union and intersection functions without a copy function and the intersection would be based off the union that was created from the linked list. In order to do that, one needed to iterate over the linked list and copy each node. For the union after a copy was made, I joined the lists together by adding the beginning of the second to the end of the first. Then created a union list by using the dict.fromkeys function I then created a new link list and only added elements based on the union list created. For the intersection I copied the list, and created an intersection list to model the new link list off of. This was done by checking if a value was in both list. I then created a new linked list by looking at intersection linkedlist and only adding the elements in the intersection_list to the linked list. 

## Time COmplexity

Append  = O(2 + n)

the 2 represents the two linked list head assignment and the creation of the new node at the end. The n represents the while loop that finds the end of the list. 

duplicate =  O(2 + 3n)

2 represents the initial variables created and the 3n represents the copy function iterated over the whole linked list

#### Union =  O(8 + n + 2n  )

8 represents the eight individual steps in the algorithm and the n represents the iteration ove the first list to get to the end of the second. 2n represents the iteration over the union node to match the other steps

the 8 steps all call different functions that can be broken down into more more sub problems

duplicate and append have already been mentioned

to_list = O(2+2n)

union_link = O(n)

#### intersection = O( 3 + 2n + 4x^3)

thre represents the 3 variables that are inialized at first. 2n represents the to lists that are created, and the 4x represents the last While node that is iterated over and checked by the two lists. The last part is cubed because the iteration checks the two lists found above 

## Help from Resources

I based the duplicate function off of an online example but changed it to fit the example. This function is easy its just iterating over the link list and creating the linked list one at a time. 

## Sources

Duplicate Function

https://www.sanfoundry.com/python-program-find-intersection-union-2-linked-lists/