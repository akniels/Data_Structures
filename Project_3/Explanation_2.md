## Search in a Rotated Array

This problem was similar to the first problem due to the target time complexity. The time complexity of log(n) would most likely be acheived by using a binary search. I was able to create a binary search for the specified array with added elements to first check where the rotation was and split accordingly. I needed to create a variable called first_iteration to keep track of the first iteration which made the time complexity 1(1log(n)) == log(n).

## Time Complexity

roated_array_search = O(n) 

This has a time complexity of 0(logn) because of the recursive format and the binary functionality. N represents the debth of the recursion which is dependant on the length of the range created.

## Space Complexity 

rotated_array_search = O(1)
 The only variable that is created is the floor variable therefore  space complexity = 1.

## Use of Resources

I able to create a binary search with a similar format as the binary search practice with adjustments to take into consideration the square root comparison to the number. 

### Sources

https://classroom.udacity.com/nanodegrees/nd256/parts/da17de0f-f834-46f8-bb48-ee2705d95dc4/modules/b849517a-9ee0-4fa8-8e22-b49fd084a350/lessons/04407d33-d27a-4732-9e4a-df6fe788a569/concepts/97eb5b12-2dba-4c17-b9dc-2e30b43d88de