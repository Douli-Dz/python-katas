"""
The prime numbers are not regularly spaced. For example from 2 to 3 the gap is 1. From 3 to 5 the gap is 2. 
From 7 to 11 it is 4. Between 2 and 50 we have the following pairs of 2-gaps primes: 3-5, 5-7, 11-13, 17-19, 29-31, 41-43

A prime gap of length n is a run of n-1 consecutive composite numbers between two successive primes (see: http://mathworld.wolfram.com/PrimeGaps.html).

We will write a function gap with parameters:

g (integer >= 2) which indicates the gap we are looking for

m (integer > 2) which gives the start of the search (m inclusive)

n (integer >= m) which gives the end of the search (n inclusive)

In the example above gap(2, 3, 50) will return [3, 5] or (3, 5) or {3, 5} which is the first pair between 3 and 50 with a 2-gap.
"""
import math

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def gap(g, m, n):
    if g&1:
        if m > 2 or n < g+2: return None
        return [2,2+g] if is_prime(2+g) else None
    j = 0
    for i in range(m|1,n+1,2):
        if is_prime(i):
            if j>0 and i-j==g:
                return [j,i]
            j = i  
    return None



"""
-- best solutions

from gmpy2 import next_prime


def gap(g, m, n):
    prev = next_prime(m - 1)

    while prev < n:
        p = next_prime(prev)

        if p - prev == g:
            return [prev, p]

        prev = p

def gap(g, m, n):
    prime = 0
    for i in range(m,n+1):
        for j in range(2,int(i**0.5)+1):
            if i%j == 0:
                break
        else: 
            if i - prime == g: return [prime,i]
            else: prime = i

"""