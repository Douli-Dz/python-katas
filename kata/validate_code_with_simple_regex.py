"""
Basic regex tasks. Write a function that takes in a numeric code of any length. 
The function should check if the code begins with 1, 2, or 3 and return true if so. Return false otherwise.
You can assume the input will always be a number.
"""

import re
def validate_code(code):
    #using regex
    return re.findall(r'^\d{1}',str(code))[0] in ['1','2','3']
    #without regex
    return str(code)[0] in ['1','2','3']


"""
--- best solution:

def validate_code(code):
    return str(code).startswith(('1', '2', '3'))

def validate_code(code):
    import re
    return bool(re.match(r"^[123]\d*$",str(code)))

validate_code = lambda c: str(c)[0] in "123"


import re
def validate_code(code):
    return bool(re.match("^[1-3]",str(code)))

"""