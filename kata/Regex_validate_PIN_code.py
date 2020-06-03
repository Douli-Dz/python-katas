"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot 
contain anything but exactly 4 digits or exactly 6 digits.
If the function is passed a valid PIN string, return true, else return false.

eg:

validate_pin("1234") == True
validate_pin("12345") == False
validate_pin("a234") == False
"""

import re
def validate_pin(pin):
    return bool(re.match('^(\d{4}|\d{6})$',pin))

    
"""
-- best solution:
import re
def validate_pin(pin):
    return bool(re.match(r'^(\d{4}|\d{6})$',pin))

validate_pin = lambda pin: len(pin) in (4, 6) and pin.isdigit()

def validate_pin(pin):
    import re
    if len(pin) == 4 or len(pin) == 6: #not 4 or 6 digits
        if re.search('[^0-9]', pin) == None : #contains non-digit chars
            return True
            
    return False
"""