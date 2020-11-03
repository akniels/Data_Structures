#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 17:18:26 2020

@author: parallels
"""
import os 



def new_find_file(suffix, path):
    files = []  
    def new_file_sub(suffix, path, files):
        if suffix == "":
            return "The suffix is an empty string"
        for file in os.listdir(path):
            file = os.path.join(path, file)
            if os.path.isfile(file) and file.endswith(suffix):
                files.append(file)
            elif os.path.isdir(file):
                files = new_file_sub(suffix, file,files )
        return files 
    return new_file_sub(suffix, path, files)

#Test Case 1#
print(new_find_file(".c", os.getcwd()))
#Test Case 2#
print(new_find_file(".", os.getcwd()))
#Test Case 3#
print(new_find_file("", os.getcwd()))
#Test Case 4#
print(new_find_file(".h", os.getcwd()))
