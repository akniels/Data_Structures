
# LRU Cache

There were plenty of examples for the LRU Cache mentioned in the lessons. The idea behind the LRU cache was to begin by creating a queue allowing to add to the front of the stack and take away from the end of the stack. The enqueue would increase the size of the stack while the front stood at the beginning. The dequeue would decrease the size by one.  In order to do that, I created two lists, one for the key and one for the value. On top of the enqueue dequeue there needs to be a way to get the most recent data with a get function. I was able to fit this into the get function by removing the value and bringing it to the front of the stack. Finally the cache will set values up to the capacity and this is done by a full cache handler function. 

## Time Complexity

#### Initializer = O(1 + 2n)
1 it the creation of the limit whil 2n represents the two lists that are created with size n.

#### Enqueue = O(2n) 
The insert functions have time complexity of 0(n)

#### Dequeue = O(2n)

Pop has a time complexity of 0(n) and we are completing it twice in this function

#### Get O(6n)

All the functions in this equation (insert, remove, index) all have time complexity 0(n) which is six 0(n) functions

#### Set = Enqueue


#### Full Cache Handler = Dequeue


## Help from Resources

I was able create a new form of enqueue/dequeue from the lessons found in Udacity but adjusted the functions to meet my needs. 

## Source 

Udacity: Building a Queue Using an Array

https://classroom.udacity.com/nanodegrees/nd256/parts/b835ca8d-4269-4ca3-b911-c8ceb9cc0aa0/modules/47d96396-21f6-4c33-91f8-41fb9cc6a88c/lessons/99bd7ee4-31b7-4801-a211-dbc35fbe1945/concepts/35c8b4db-ff07-4264-b48e-ed523c3e51b1


