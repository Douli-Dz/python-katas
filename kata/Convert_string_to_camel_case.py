
"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

Examples
to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns  "TheStealthWarrior"
 
"""

import re
def to_camel_case(text):
    text = re.split('[- _]',text)
    return text[0]+''.join(x.title() for x in text[1:])

"""
-- best solution:

def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s

def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')


from re import findall
def to_camel_case(text):
    text = findall(r"[^-_]+", text)
    return text[0] + "".join(w.capitalize() for w in text[1:]) if text else ""

"""