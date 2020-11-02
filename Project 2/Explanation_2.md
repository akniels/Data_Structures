# File Recursion

In order to achieve the specified solution to this problem, recursion allowed the function to be most efficient. Recursion stores items in memory while calling a function on itself allowing big N notation to be linear instead of being multiplied by the number of steps. I knew I wanted to first determine if the file ended with the specified suffice, if so, the file would be appended to a list of files. If not, the file would be called on itself recursively with the added file name in order to drill down to the lower levels. At first I had trouble appending to the list without causing the result of the recursion to overwrite itself. I was able to solve the issue by building a function within a function.


## Time Complexity

#### new_find_file = O(1 + 1n^x)

The 1 represents the initiaiton of the empy files list that will contain our answer.

THe 1n represents the append function that will add to the list when a file is found. N represents the iteration over the fils in the path

^2 represents the depths of the path of the recursion. 

## Help from Resources

I found a resource that showed how to append a list from a recursive function. It had the function listed in the function with only one function. I wanted to see if I could do it differently by having a function within a function and got it to work. 

## Source 
Stack Overflow
https://stackoverflow.com/questions/41677237/traverse-directory-structure-in-python-recursively-without-os-walk