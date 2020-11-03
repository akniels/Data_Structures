## HTTP Router Using Trie

This assignment focused on the creation of a routing trie for for a website. This was to test the understanding on a node tree typetype item that found the websites with a handler. This was similar to the tree items we learned about in the various lessons. We started with a Router class that referenced a tree with nodes. We needed a way to add handlers and lookup handlers and get rid of the random slashes that were found in the paths. I used a split path method that took out the commas and added the peices in between to a list. the list was then passed. to a tree insert function that added the nodes to the tree with the path list. The lookup function utilized the same split path function and then passed that path to the find function in the tree which then searched the nodes. 

## Time Complexity

Add Handler  = O(2 + 6n )

The 1 shows the initiation of the list. The 4n is complicated because the items go through alot of various steps. The first step to split the list and append the items to the list initiated. This is dependant on the items in the list (n). There are two steps in this which leads to the first 2 of the 6n. The insert statement for the tree class and the node class also contain two steps based off the length of the list (n) Therefore 2n + 2n + 2n = 6n. also the root initiation in the tree insert function adds another step to the process adding one more for standard initiation.

lookup  = O(2 + 3n)

The lookup function is similar to the add handler function with the exception of the find function for the node. The find function was only necessary in the tree function which only had noe step for the items in the list. 

## Space Complexity

lookup = O(1 + n)

The space complexity has n which is dependant on the length of the path in the split_path function. It also has a the 1 for the path the node created in the find function.

add_handler = O(1 + n)

The space complexity of the add_handler item is also based on the split path functin with the initiation of the node in the insert function.

## Sources

I referenced the udacity section with the explanation of Tries. I utilized the same structure but changed the sections to better fit the problem.

https://classroom.udacity.com/nanodegrees/nd256/parts/da17de0f-f834-46f8-bb48-ee2705d95dc4/modules/b849517a-9ee0-4fa8-8e22-b49fd084a350/lessons/04407d33-d27a-4732-9e4a-df6fe788a569/concepts/e79df31f-6b25-416b-b62d-a410f12a512d