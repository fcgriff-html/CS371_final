# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 15:19:26 2021

@author: charl
"""
def dfa_model():
    print("please enter your string: ")
    input_string = input()
    dfa_states= {0:{'0':0, '1':3},
                 1:{'0':1, '1':1},
                 2:{'0':2, '1':1},
                 3:{'0':1, '1':0}}
    state = 0
    for i in input_string:
        state = dfa_states[state][i]
    if state == 1:
        print("accepted!   " + input_string)
    else:
        print("declined :( ")
        
    
        