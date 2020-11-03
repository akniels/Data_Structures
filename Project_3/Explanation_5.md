## Autocomplete with Tries

This assignment was created to help understand the structure of Tries. In order to create the trie one must have two sections, thereneeds to be a nod section along with a tree section. The tree section is built of nodes with the first tree node as the root. The insert tree function traverses the tree until the end by iterating over the children. The insert then add the newest to the end of the traversal. The find function does the same thing but traverses the trees of children to see if the letters in the word have been added to the tree.

## Time Complexity
insert O(3 + 2n)

This algorithm has  a time complexity of 1 + 2n because it first calls the root variable and then traversies the length of trie N and then adds the variable and isword to the end.

find O(1 + n)

this function is 1 + n because it first calls the root and then traverses the dictionary n until the word is found.

## Space Complexity

Find =  O(1)

The space complexity of the item is 1 because a node based of self.root is created.

insert = O(1)

The space complexity of the item is 1 because a node based of self.root is created.

TrieNode Initializer = O(1 + 1n)

The space complexity of the initializer is a boolean and children dependant on the number of characters in the dictionary.

Trie initializer = O(1)

A root is created with the initializer .

## Sources

I referenced the udacity section with the explanation of Tries. I utilized the same structure but changed the sections to better fit the problem

https://classroom.udacity.com/nanodegrees/nd256/parts/da17de0f-f834-46f8-bb48-ee2705d95dc4/modules/b849517a-9ee0-4fa8-8e22-b49fd084a350/lessons/04407d33-d27a-4732-9e4a-df6fe788a569/concepts/e79df31f-6b25-416b-b62d-a410f12a512d