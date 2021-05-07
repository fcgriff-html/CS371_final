# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 15:19:26 2021

@author: charl
"""

"""
ok so basically all we need to do is repurpose this state machine to start scanning once the proper state has been reached, we can have it start a quiz or something, it shouldnt be too crazy
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
        print("/n" + "ready to unlock the scanner? y/n: ")
        answer = input()
        if answer == "y":
            scanner()
        else:
            print("Thanks for hanging out gamers")
    else:
        print("declined :( /n")
        print("would you like to try again? y/n: ")
        answer = input()
        if answer == "y":
            dfa_model()
        else:
            print("thanks for playing!")
    
  def scanner():
    print("format note: please use '-' to denote math, and '--' to denote a dash", "/n")
    scan = input("please enter the string to be scanned: ")
    output = switcher(scan) #pseudo switch case to determine the token
    #output is a dictionary organized by index in the string
    token_idx = output.keys()
    for i in range(len(token_idx)):
        if i == 0:
            print(scan[0:i], "  " , output[token_idx[i]])
        elif i < len(token_idx)-1:
            print(scan[i:i+1], "  ", output[token_idx[i]])
        else:
            print(scan[i::], "  ", output[token_idx[i]])

            
 def switcher(scan):
    #takes string in, returns array w/ token types and indexs for each token
    ret = {}
    for i in range(len(scan)):
        if scan[i] == "+":
            ret[i] = "plus"
        if scan[i] == "-":
            ret[i] = "minus"
        if scan[i] == "/":
            ret[i] = "divide"
        if scan[i] == "*":
            ret[i] = "multiply"
        if scan[i] == "--":
            ret[i] = "dash"
        if scan[i] == "**":
            ret[i] = "exponet"
    return ret
            
    
    
    
    
        
