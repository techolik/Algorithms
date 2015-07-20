#!python3
from itertools import *
from random import *
import math

def test(m, k):
    return len([i for i in combinations_with_replacement('a' * m,k)])

'''    
for i in range(2, 10):
    for j in range(1, i + 1):
        print(i, j, test(i, j), select(i + j - 1, j))
    print
'''

def f(m, k):
    return select1(m + k - 1, k)
    
def g(m, n):
    s = 0
    for i in range(1, n + 1):
        s += f(m, i)
    return s

#print(g(2, 2))

'''
for i in range(1, 7):
    for j in range(1, 7):
        #print(g(i, j), end=' ')
        print ('{0:>4}'.format(g(i, j)), end='')
    print ('')
    
   1   2   3   4   5   6
   2   5   9  14  20  27
   3   9  19  34  55  83
   4  14  34  69 125 209
   5  20  55 125 251 461
   6  27  83 209 461 923
'''
cache = {}
def fact(n):
    if cache.get(n, 0) > 0:
        return cache[n]
    r = factorial(n)
    cache[n] = r
    return r
    
def select1(a, b):
    r = math.factorial(a) // math.factorial(b) // math.factorial(a - b)
    return r

cl = [1]
def fact2(n):
    if n > len(cl):
        for i in range(len(cl), n):
            cl.append((i + 1) * cl[i - 1])
    return cl[n - 1]

def select2(a, b):
    r = fact2(a) // (fact2(b) * fact2(a - b))
    return r
    
'''
from operator import mul    # or mul=lambda x,y:x*y
from fractions import Fraction
def select3(n,k): 
  return int( reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )
'''
def select3(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0
        
def select4(n, r):
    c = 1
    for (num,denom) in zip(range(n,n-r,-1), range(1,r+1,1)):
        c = (c * num) // denom
    return c

def select5(n, k):
    if k > n / 2:
        k = n - k
    r = 1
    p = 10 ** 6 + 3
    for t in range(1, k + 1):
        r *= (n - k + t)
        r //= t
        r %= p
    return r
'''
def factorial(n, mod):
    r = 1
    for i in range(2, n + 1):
      r = r * i % mod
    return r % mod;
'''    
cl = [1]
def factorial2(n, mod):
    if n > len(cl):
        for i in range(len(cl), n):
            cl.append((i + 1) * cl[i - 1] % mod)
    return cl[n - 1]
    
def select6(n, k, mod):
    k = min(k, n - k)
    r = 1
    for i in range(n - k + 1, n + 1):
        r = r * i % mod    
    d = factorial2(k, mod)
    d = pow(d, mod - 2, mod)
    r = r * d
    return r % mod
    
def select7(n, k, mod):
    if n > mod or k > mod:
        n1, k1 = n // mod, k // mod
        n0, k0 = n % mod, k % mod
        if n1 < k1 or n0 < k0:
            return 0
        return select7(n1, k1, mod) * select7(n0, k0, mod)
    
    if n == k or k == 0:
        return 1
    a = factorial2(n, mod)
    b = factorial2(k, mod)
    b = pow(b, mod - 2, mod)
    c = factorial2(n-k, mod)
    c = pow(c, mod - 2, mod)
    return a * b * c % mod
    
def solve(m, n, p):
    s = 0
    for i in range(1, n + 1):
        s += select2(m + i - 1, i)
    return s % p
    

def test2(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            #print(g(i, j), end=' ')
            #print ('{0:>7}'.format(solve(j, i) - i) , end='')
            pass
        print ('')
           

def test3(n, m, p, pr=False):
    a = (select7(n + m, m, p) - 1)%p
    b = (select3(n + m, m) - 1)% p
    #print(a)
    #print(g(n, m) % p)
    #print()
    if a != b:
        print(n, m, a,b)
    assert(a == b)
    
p = 10 ** 6 + 3

for i in range(1000):
    test3(randint(1, 1000), randint(1, 1000), 193)

#test3(779, 117, 193, True)

#print(select3(10000, 340) % (10 ** 6 + 3))
#print(select6(10000, 340))

def solve2(n, m, p):
    if n > p or m > p:
        return (solve2(n // p, m // p, p) * solve2(n % p, m % p, p)) % p
    else:
        return (select4(m + n, n, p) - 1) % p
        