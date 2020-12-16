"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""

def solution(string,markers):
    # split string into lines to process them one after another
    content = string.split("\n")
    
    #process every line by its own and append the clean line to clean_content
    clean_content = []
    for full_line in content:
        
        #appending each char until marker
        clean_line = ""
        for char in full_line:
            
            #check for marker, if no marker add char to clean_line 
            #if char in marker break loop
            
            if not char in markers:
                clean_line += char
            else:
                break
        
        #strip whitespaces
        clean_line = clean_line.strip()

        #add clean line to content
        clean_content.append(clean_line)
        
    return "\n".join(clean_content)