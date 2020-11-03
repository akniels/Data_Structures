#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 15:02:38 2020

@author: akniels1
"""

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler, not_found_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)
        self.handler = handler
        self.not_found_handler = not_found_handler

    def insert(self, list_of_paths, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node  = self.root
        for  i ,item in enumerate(list_of_paths):
            if  item not in node.children and i == len(list_of_paths)-1 :
                new_node = node.insert(item, handler)
                node = new_node
            if item not in node.children:
                new_node = node.insert(item, self.not_found_handler)
                node = new_node
            if item in node.children:
                node = node.children[item] 
            
    def find(self, path_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        
        node = self.root
        if path_list == ['']:
            return self.root.handler
        for item in path_list:
            if item in node.children:
               node = node.children[str(item)]
            elif item not in node.children:
                return self.not_found_handler
        return node.handler
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler
    def insert(self, string, handler):
        # Insert the node as before
        self.children[string] = RouteTrieNode(handler)
        nn = self.children[string]
        return nn

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler= 'not found handler'):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route = RouteTrie(root_handler, not_found_handler)
        self.handler = root_handler
        self.handler = not_found_handler
    def add_handler(self, path , handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        # self.path = path 
        # self. handler
        path_list = self.split_path(path)
        self.route.insert(path_list, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if not path:
            new_lookup = self.route.not_found_handler
        else:
            path_list = self.split_path(path)
            new_lookup = self.route.find(path_list)
        return new_lookup

    def split_path(self, stringed_path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        P_list = []
        for items in stringed_path.split("/"):
            P_list.append(items)
        P_list = P_list[1:]
        if P_list[-1] == '':
            P_list.pop()
        return P_list
# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/resume", "resume handler")  # add a route

#print(router.route.root.children['home'].handler)
# # some lookups with the expected output
# Two Edge Cases
print(router.lookup("")) # should print 'not found'
print(router.lookup("/")) # should print 'root handler'
# rest of the cases
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one        
 


##print(router.route.root.children)       
print(router.lookup("/home/resume")) # should print 'resume' or None if you did not implement one        
print(router.lookup("/home/resume/")) # should print 'resume handler' or None if you did not implement one        
print(router.lookup("/home/resume/me")) # should print 'not found handler' or None if you did not implement one        

        
        
        
        
        
        
        
        