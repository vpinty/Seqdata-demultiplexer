#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 08 12:57:06 2016

@author: Panna Vass
"""

import os
path=raw_input("Please enter working directory path: ")
os.chdir(path)

# Opening sequencing data file:
sample_file=raw_input("Please enter sequencing data file name: ")
with open(sample_file) as f:
    seq_file=f.read().splitlines()
    
# Opening configuration file:
config_file=raw_input("Please enter configuration file name: ")    
with open(config_file) as h:
    config=h.read().splitlines()    

#Creating list of lists from the config file    
config_list=[]
for config_line in config:
    config_list.append(config_line.split())   

#Demultiplexing       
for i in seq_file:
    condition_is_met = False
    for group_list in config_list:
        len1=len(group_list[1])
        len2=len(group_list[2])
        if group_list[1] == i[:len1] and group_list[2] == i[-len2:]:
            with open(group_list[0]+".seq", "a+") as a:
                a.write(i+"\n") 
            condition_is_met = True            
    if condition_is_met == False:
        with open("unmatched.seq", "a+") as u:
            u.write(i+"\n") 
                
print "Finished demultiplexing."
