# Square Root Function

The goal of this project was to make a sqrt function with time complexity of 0(logn). The best approach for log(n) was to do a binary search with no added variables before the If and reurn statements. I had to functions, the out function that called the inner function with the creation of the list of 0 up to the number for the square, and then in the inner function I created the Binary search. The binary search split the list based on the number squared. 

## Time Complexity

sqrt = O(n) 

The 1 represents the floored square variable that begins the check through all variables up to the sqrt variable. N represents the items in the string of numbers. It is log n because at most you will only traverse half of the dataset (with the exeption of 0 and 1). 
## Space Complexity

sqrt = O(1)

This algorithm = O(1) space complexity because there is only one variable that is created in the algorithm.

## Use of Resources

I able to create a binary search with a similar format as the binary search practice with adjustments to take into consideration the square root comparison to the number. 

### Sources

https://classroom.udacity.com/nanodegrees/nd256/parts/da17de0f-f834-46f8-bb48-ee2705d95dc4/modules/b849517a-9ee0-4fa8-8e22-b49fd084a350/lessons/04407d33-d27a-4732-9e4a-df6fe788a569/concepts/97eb5b12-2dba-4c17-b9dc-2e30b43d88de

