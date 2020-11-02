# Active Directory

The task at hand was to create an efficient algorithm to test whether a user was in a group. The way I went about doing this was to was a binary search. The users and groups were both in lists. Since these wouldn’t be in a particular order, and the lists were shorter, I split the group in two and did recursive functions on the halves until the item was found. 

## Help from Resources

In the Udacity lessons there was an example of a recursive binary search which I based the logic off of but built it to the task at hand. 

## Time COmplexity

is_user_in_group = O(2n)

2n represents the sort algorithm plus the recursive calls

Udacity: Binary Search Variation

https://classroom.udacity.com/nanodegrees/nd256/parts/da17de0f-f834-46f8-bb48-ee2705d95dc4/modules/b849517a-9ee0-4fa8-8e22-b49fd084a350/lessons/04407d33-d27a-4732-9e4a-df6fe788a569/concepts/c8beafab-f740-4ef6-875e-dfba919bfe6f