from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact




    ## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.isword = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
                self.children[char] = TrieNode()
                
    def suffixes(self, suffix = '',list_words=[]):
            ## Recursive function that collects the suffix for 
            ## all complete words below this point
        for key , value  in self.children.items():
            suffix += str(key)
            if value.isword == True:
                list_words.append(suffix)
            self.children[key].suffixes(suffix)
        return list_words
                #new_suff  = value.suffixes(suffix) +str(key)
                #return new_suff
        
                   
        # return  suffix  
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        node = self.root 
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isword = True
 
            
    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root
        
        for item in prefix:
            if item   in node.children:
                node = node.children[item]
            else:
                return False
        return node
    
    
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


print(MyTrie.find('ant').suffixes())
print(MyTrie.find('t').suffixes())

#print(MyTrie.root.children)




               
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='')  

