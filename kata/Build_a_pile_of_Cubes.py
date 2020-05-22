"""
Your task is to construct a building which will be a pile of n cubes. 
The cube at the bottom will have a volume of n^3, 
the cube above will have volume of (n-1)^3 and so on until the top which will have a volume of 1^3.
You are given the total volume m of the building. 
Being given m can you find the number n of cubes you will have to build?

The parameter of the function findNb (find_nb, find-nb, findNb) 
will be an integer m and you have to return the integer n such as 
n^3 + (n-1)^3 + ... + 1^3 = m if such a n exists or -1 if there is no such n.

Examples:
findNb(1071225) --> 45
findNb(91716553919377) --> -1
"""
def find_nb(m):
    # your code
    if 1 ** 3 == m:
        return 1
    else:
        n = 2
        volume = 1
        while volume < m:
            volume = volume + n ** 3
            if volume == m:
                return n
            else:
                n = n + 1
                continue
        return -1
"""
-- best solution:

def find_nb(m):
    i,sum = 1,1
    while sum < m:
        i+=1
        sum+=i**3
    return i if m==sum else -1

def find_nb(m):
    n,k=0,0
    while k < m:
        k = (n*(n+1)/2)**2
        n+=1
    if k == m: return n-1
    else: return -1

def find_nb(m):
    '''
    n cube sum m = (n*(n+1)//2)**2
    then n**2 < 2*m**0.5 < (n+1)**2
    and we can proof that for any n, 0.5 > (2*m**0.5)**0.5 - n**2 > 2**0.5 - 1 > 0.4
    '''
    n = int((2*m**0.5)**0.5)
    if (n*(n+1)//2)**2 != m: return -1
    return n
"""