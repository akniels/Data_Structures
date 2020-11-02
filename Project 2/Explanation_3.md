# Huffman Encoding

Huffman encoding was the most challenging problem for me. I did not focus on optimization or speed and instead tried to code it in a way that the algorithm completed the task. I first knew that we needed a priority queue. This priority queue was created from a dictionary and then turned into a heap format. Once it was in the heap format and in order, I was able to pop from the beginning where the numbers were smaller and create the tree based off the smallest number. After the tree was created, the task was encode the tree by traversing and adding a 0 for left movements and 1 for right movements. The decode function traversed the tree based on 0’s and 1’s until a tree with a letter was found. Once it was found, the tree was restarted. 

## Time Complexity

Encoded_data  = O(2 + 19n)

2 represents the static creation of variables that are constant

n represents the number of items in the string that is passed into the function

19 represents the 19 steps taken to creates the nodes for the tree in the while loop. 

get_binary = O(2 + 2n)

2 represents the dictionary greation and the get root function 

2n represents the recursion function done for each step of the tree

## Help from Resources

The udacity projects displayed various ways to build nodes and trees. I used that code for this assignment with the addition of more variables needed. I also had a difficult time with traversing the tree after its creation so I based the get_binary function off of an example I found but made it in a way that worked with my logic. I undestand how both the nodes and trees work along with the recursive get binary function

## Sources

https://www.techrepublic.com/article/huffman-coding-in-python/

Udacity Code DFS

https://classroom.udacity.com/nanodegrees/nd256/parts/b835ca8d-4269-4ca3-b911-c8ceb9cc0aa0/modules/47d96396-21f6-4c33-91f8-41fb9cc6a88c/lessons/34adf09a-888b-409b-988f-0506b0e7501e/concepts/d1b28254-3536-4831-9567-6d66d669ab13