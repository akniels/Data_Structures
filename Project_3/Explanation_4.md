# Dutch National Flag Problem

In order to solve this problem, one must traverse the list and sort one at a time. Since there are only three numbers in the list, the sorting is easier. One must have three variables. The rist variable will be the traversal item. The traversal item will do most of the movement throught the list checking items one at a time. The other two variables keep track of the movement at the sides of the list. Begin with the traverser at the beginning of the list and check the 0's and 2's that you come across. If a 0 appears push it to the front tracker and then have the front move up. if a 2 appears in the traverser push it to the end of the list and have the end variable catch and then iterate one step. Do this until the traverser reaches the back variable. 

## Time Complexity 

sort_012 = O(3 + 4n)

3 represents the initial variable created at the beginning of the algorithm.

4n represents the steps taken in the while loop that iterate over the list.

## Spece Complexity


sort_012 = O(3n)

The space complexity of the sort function is 3n because there are 3 variable created with this algorithm.

## Resources used

Udacity was referenced with 0,1,2 sorting algorithm. 

### Sources

https://classroom.udacity.com/nanodegrees/nd256/parts/da17de0f-f834-46f8-bb48-ee2705d95dc4/modules/b849517a-9ee0-4fa8-8e22-b49fd084a350/lessons/902b8515-a2ef-485b-9543-f9a9aad9843f/concepts/a72b7596-67d6-462c-8917-8c5e98c43bed

