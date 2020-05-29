"""
There is a secret string which is unknown to you. Given a collection of random triplets from the string, 
recover the original string.

A triplet here is defined as a sequence of three letters 
such that each letter occurs somewhere before the next in the given string. "whi" is a triplet for the string "whatisup".

As a simplification, you may assume that no letter occurs more than once in the secret string.

You can assume nothing about the triplets given to you other 
than that they are valid triplets and that they contain sufficient information to deduce the original string. 
In particular, this means that the secret string will never contain letters that do not occur in one of the triplets given to you.
EXAMPLE 
secret = "whatisup"
triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]
"""

def recoverSecret(triplets):
  secret=[]
  for a in triplets:
      x = a[0]
      y = a[1]
      z = a[2]
      if x not in secret:
          secret.insert(0,x)
      if y not in secret:
          secret.insert(secret.index(x)+1,y)
      if y in secret and secret.index(y) < secret.index(x):
          secret.pop(secret.index(y))
          secret.insert(secret.index(x) + 1, y)
      if z not in secret:
          secret.insert(secret.index(y)+1,z)
      if z in secret and secret.index(z) < secret.index(y):
          secret.pop(secret.index(z))
          secret.insert(secret.index(y) + 1, z)
  return ''.join(secret)

"""
--- best solutions:
from collections import defaultdict

def recoverSecret(triplets):
    letters = defaultdict(set)
    for a, b, c in triplets:
        letters[a].add(b)
        letters[a].add(c)
        letters[b].add(c)

    for key, value in letters.items():
        for after_key in value:
            letters[key] = letters[key].union(letters[after_key])

    return ''.join(k for k, _ in sorted(
        letters.iteritems(), key=lambda (_, v): len(v), reverse=True))


def recoverSecret(triplets):
  s = list(set([c for t in triplets for c in t]))
  for t in triplets:
    if s.index(t[1]) > s.index(t[2]):
      s.remove(t[1])
      s.insert(s.index(t[2]), t[1])
    if s.index(t[0]) > s.index(t[1]):
      s.remove(t[0])
      s.insert(s.index(t[1]), t[0])
  return ''.join(s)
"""
