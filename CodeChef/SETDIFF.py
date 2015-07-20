
S = set(i for i in range(1, 6))

def subsets(my_set):
    result = [[]]
    for x in my_set:
        result = result + [y + [x] for y in result]
    return result

def test():
    print(subsets(S))    

    for s in subsets(S):
        if s:
            print(min(s), max(s))
            
def solve(l, m):
    n = len(l)
    s = 0
    for i in range(n):
        t = (pow(2, n - i - 1, m) - 1) % m
        if t > 0:
            s += l[n - 1 - i] * t
            s -= l[i] * t
        else:
            break
        #s %= (10 ** 9 + 7)
    print(s % m)
    
from random import *
l = [randint(1, 10 ** 9) for x in range(10 ** 5)]
l.sort()
#solve(sorted([1, 2, 3, 4]))    
solve(l, 10 ** 9 + 7)

#test()
    