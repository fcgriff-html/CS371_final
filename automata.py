# -*- coding: utf-8 -*-
"""
Created on Fri May  7 19:15:10 2021

@author: charl
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 15:19:26 2021
@author: charl
"""

"""
ok so basically all we need to do is repurpose this state machine to start scanning once the proper state has been reached, we can have it start a quiz or something, it shouldnt be too crazy
"""
def calc_math(dicty, key_idx, mathstr):
    numli = []
    for i in range(len(mathstr)):
        if i not in key_idx:
            numli.append(int(mathstr[i]))
    total = 0
    count = 0
    #this loop checks the number values against the tokens to compute the equation based on a PMDM order of operations
    for j in numli:
        if count == 0:
            total += j #starts with this as a base case
            #the following if statements account for the operation
        elif dicty[key_idx[count-1]] == "plus":
            total = total + j
        elif dicty[key_idx[count-1]] == "minus":
            total = total-j
        elif dicty[key_idx[count-1]] == "divide":
            total = total/j
        elif dicty[key_idx[count-1]] == "multiply":
            total = total*j
        count+=1
        print("step total: ", total) #sanity check to make sure the steps described in the first part
    print("your total is: ", total) #final total
            

def scanner():
    print("format note: please use '-' to denote math, and '--' to denote a dash", "\n")
    print("if you decide to use numbers in your string, we can also compute those values")
    scan = input("please enter the string to be scanned: ")
    calc = input("would you like to see the result(numbers only, no spaces or letters)? y/n: ")
    output = switcher(scan) #pseudo switch case to determine the token
    #output is a dictionary organized by index in the string
    token_idx = []
    keys = output.keys()
    for key in keys:
        token_idx.append(key)
    for i in range(len(token_idx)):
        if i == 0:
            print(scan[0:token_idx[i+1]], "  " , output[token_idx[i]])
        elif i < len(token_idx)-1:
            print(scan[token_idx[i]:token_idx[i+1]], "  ", output[token_idx[i]])
        else:
            print(scan[token_idx[i]::], "  ", output[token_idx[i]])
    if calc == "y":
        calc_math(output, token_idx, scan)

            
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
            if scan[i] == "(":
                ret[i] = "open parens"
            if scan[i] == ")":
                ret[i] = "closed parens"
                
        return ret
def dfa_model():
    print("even zeros, odd ones :)")
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
        print("\n" + "ready to unlock the scanner? y/n: ")
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
