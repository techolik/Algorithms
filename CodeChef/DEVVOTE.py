def omg(n):
    return n * (n - 1) ** (n - 1), n ** n
    
for i in range(2, 11):
    print(i, omg(i))
    
from itertools import *
from collections import *
from math import *

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a
    
def gen(n):
    presidents = 0.0
    votes = 0
    for p in product([i for i in range(1, n + 1)], repeat=n):
        for i in range(1, len(p)):
            if p[i] == p[i-1]:
                break
        else:
            #print (p)
            c = None
            pre = 0
            for common in Counter(p).most_common():
                if c == None or common[1] == c:
                    pre += 1
                    c = common[1]
                else:
                    break
            votes += 1
            #if pre == 3:
            #    print(p, pre)
            presidents += pre
            
    return presidents, votes

def solve():
    for i in range(1, 7):
        p, v = gen(i)
        g = gcd(p, v)
        print(i, p/i, v/i, p/v)

print(gen(6))
#solve()

'''
(1, 1.0, 1, 1.0)
(2, 4.0, 2, 2.0)
(3, 24.0, 12, 2.0)
(4, 192.0, 108, 1.7777777777777777)
(5, 2120.0, 1280, 1.65625)
(6, 31140.0, 18750, 1.6608)
(7, 566202.0, 326592, 1.733667695473251)
'''