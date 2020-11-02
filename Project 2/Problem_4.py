#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 11:15:19 2020

@author: akniels1
"""

from time import time

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name



def is_user_in_group(user, group):
    """
        Return True if user is in the group, False otherwise.
    
        Args:
          user(str): user name/id
          group(class:Group): group to check user membership against
        """
    # if group is not Group:
    #     return False
        
    people = sorted(group.get_users())
    
    if len(people) == 0:
        return False
    center = (len(people)-1)//2
    if people[center] == user:
        return True
    elif people[center] < user:
        return is_user_in_group(user, group[center+1:])
    else:
        return is_user_in_group(user, group[:center])
                
    
   #Test Case 1 # 

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


print(is_user_in_group("sub_child_user", sub_child))


# Test Case 2 #


computer = Group("subchild")
computer_1_user = "computer1_user"
print(is_user_in_group("computer1_user", computer))

# Test Case 3 #



print(is_user_in_group("", computer))
