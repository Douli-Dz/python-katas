"""
Write a function called that takes a string of parentheses, 
and determines if the order of the parentheses is valid. 
The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, 
input may contain any valid ASCII characters. Furthermore, 
the input string may be empty and/or not contain any parentheses at all. 
Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
"""
open_list = ["("] 
close_list = [")"]
  
def valid_parentheses(string):
    stack = [] 
    for i in string: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return False
    if len(stack) == 0: 
        return True
    else: 
        return False
  
"""
-- best solutions

import re
def valid_parentheses(s):
    try:
        re.compile(s)
    except:
        return False
    return True


def valid_parentheses(string):
    count = 0
    for i in string:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0


def valid_parentheses(string):
    count = 0
    for i in string:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0
"""
