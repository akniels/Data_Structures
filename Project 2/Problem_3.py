#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 15:28:56 2020

@author: parallels
"""

import sys
from heapq import heappush, heappop, heapify
from collections import defaultdict
    

class Node(object):
        
    def __init__(self,value = None, letter = None):
        self.value = value
        self.left = None
        self.right = None
        self.letter = letter
        self.binary = None
        
    def set_value(self,value):
        self.value = value
        
    def get_value(self):
        return self.value
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def set_binary(self, binary):
        self.binary = binary
   
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.value),
        if self.right:
            self.right.PrintTree()     

class Tree():
    def __init__(self):
        self.root = None
        
    def set_root(self,Node):
        self.root = Node
        
    def get_root(self):
        return self.root




def get_binary(tree):
    
    binary = {}
    root = tree.get_root()
    

    def get_bin(binar, node):
        if node.letter is not None:
            
            # if 
            
            
            if not binar:
                binary[node.letter] = str(node.binary)
            else: 
                binary[node.letter] = binar
        else:
            get_bin(binar+str(node.left.binary), node.left) 
            get_bin(binar+str(node.right.binary), node.right)

    get_bin("",root)
    return binary

        
    


def huffman_encoding(data):
    if data == "" :
        return  '-1', None
    Huffman_tree = Tree()
    d = defaultdict(int)
    for ch in data:
        d[ch] += 1
    d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
    heap = [[wt,sym] for sym, wt in d.items()]
    if len(heap) == 1:
        left = heappop(heap)
        node = Node(left[0], left[1])
        node.binary = 0
        Huffman_tree.set_root(node) 
    else:
        left  = heappop(heap)
        right = heappop(heap)
        l_node = Node(left[0], left[1])
        r_node = Node(right[0], right[1])
        Parent_node = Node(left[0]+right[0])
        Parent_node.set_left_child(l_node)
        Parent_node.set_right_child(r_node)
        l_node.set_binary(0)
        r_node.set_binary(1)
        Huffman_tree.set_root(Parent_node) 
    while len(heap) > 1 :
        n = heappop(heap) 
        left_node = Node(n[0], n[1])
        left_node.binary = 0
        nn = heappop(heap)
        right_node = Node(nn[0], nn[1])
        right_node.binary = 1
        parent_value = n[0] + nn[0]
        pa_node = Node(parent_value)
        pa_node.left = left_node
        pa_node.right = right_node
        grandparent_value = Huffman_tree.get_root().value + pa_node.value
        grandparent_node = Node(grandparent_value)
        grandparent_node.left = Huffman_tree.get_root()
        grandparent_node.right = pa_node
        Huffman_tree.get_root().binary = 0
        pa_node.binary = 1 
        Huffman_tree.set_root(grandparent_node)
    dictionary = get_binary(Huffman_tree)    
        
    return "".join([dictionary[a] for a in data]), Huffman_tree
   
    
        

def huffman_decoding(data,tree):
    if data == "-1" :
        return  '-1'
    
    data = [char for char in data]
    decoded = list()
    index_tracker = 0
    current_node  = tree.get_root()
    if current_node.left is None and current_node.right is None:
        for char in data:
            decoded.append(current_node.letter)
    else:
        
        while index_tracker <= (len(data)-1):
            if current_node.letter is not None:
                decoded.append(current_node.letter)
                current_node = tree.get_root()
                # index_tracker+=1
                continue
            else:
                bin_value = data[index_tracker]
                if bin_value == '0':
                    current_node = current_node.get_left_child()
                    index_tracker+=1
    
                else:
                    current_node = current_node.get_right_child()
                    index_tracker+=1
        decoded.append(current_node.letter)
    return "".join([ d for d in decoded])
    




if __name__ == "__main__":
    codes = {}


    #Test Case 1 #

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    
    #Test Case 2 #

    empty_sentece = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(empty_sentece)))
    print ("The content of the data is: {}\n".format(empty_sentece))

    empty_encoded_data, empty_tree = huffman_encoding(empty_sentece)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(empty_encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(empty_encoded_data))

    empty_decoded_data = huffman_decoding(empty_encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(empty_decoded_data)))
    print ("The content of the encoded data is: {}\n".format(empty_decoded_data))
    
    a_sentence = "aaaaaaaaaaaa"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_sentence)))
    print ("The content of the data is: {}\n".format(a_sentence))

    a_encoded_data, a_tree = huffman_encoding(a_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(a_encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(a_encoded_data))

    a_decoded_data = huffman_decoding(a_encoded_data, a_tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(a_decoded_data)))
    print ("The content of the encoded data is: {}\n".format(a_decoded_data))