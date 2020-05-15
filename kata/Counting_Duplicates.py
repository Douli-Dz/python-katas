
"""
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice

"""

from collections import Counter

def duplicate_count(text):
    counter = Counter(text.lower())
    #filter the dict  by keeping only letter repeated more than once
    newDict = dict(filter(lambda elem: elem[1] > 1, counter.items()))
    #return the length of the filtred dict
    return len(newDict.keys())

"""
-- best solution:

from collections import Counter
def duplicate_count(text):
    return sum(1 for c, n in Counter(text.lower()).iteritems() if n > 1)
    

from collections import Counter
def duplicate_count(text):
    return sum(v > 1 for v in Counter(text.lower()).itervalues())
     
"""
    

