# Blockchain

For this assignment, the goal was to create a hashed linked list with reference to the previous hash. This was different from the practice problems because it was essentially a double linked list with no reference to the next function. I created a class called blocked linked list that would append items to the linked list. I did this in the traditional linked list fashion by having head and tail node. The only difference was the I created a function that would only add the previous hash as a variable in the Block initialization done in the append block method. 



# Help from Resources

I used a print function found in the lessons to print the blockchain that was created with tweaks to take into consideration the hash and the string. 


## Time Complexity

Block_linked_list initializer = O(4)

four variables are initated with the creation of the object

append_block = = O(11)

there are 11 steps in the append block process when you include the initialization the steps below, and the calc_has function. 

append_block = = O(2+ 2n)

Two variables are created and then a while loop 

iItterating over the number of append blocks gives us the 2n variable. 

## Sources

Udacity: Show Me the Data Structures Problem 6 

https://classroom.udacity.com/nanodegrees/nd256/parts/b835ca8d-4269-4ca3-b911-c8ceb9cc0aa0/modules/47d96396-21f6-4c33-91f8-41fb9cc6a88c/lessons/a640374a-90af-40ad-85ff-1c6ce3948219/concepts/1b29b6fd-d79e-4079-ab84-341555b7f520
