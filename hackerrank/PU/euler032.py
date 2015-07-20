from itertools import *

def p_to_int(p):
    r = 0
    for pp in p:
        r *= 10
        r += pp
    return r

def int_to_set(n):
    s = set()
    while n:
        d = n % 10
        if d in s:
            return 0
        s.add(d)
        n //= 10
    return s
    
def solve_s(s, na, nb):
    res = 0
    added = set()
    for i in range(1, na + 1):
        for pa in permutations(s, i):
            soffa = s - set(pa)
            #print(pa, soffa)
            for j in range(1, nb + 1):
                for pb in permutations(soffa, j):
                    sres = soffa - set(pb)
                    ra, rb = p_to_int(pa), p_to_int(pb)
                    prod = ra * rb
                    #print(pa, pb, sres, prod)
                    if int_to_set(prod) == sres:
                        if prod not in added:
                            print(pa, pb, sres, prod)
                            res += prod
                            added.add(prod)
    return res
    
def solve(n):
    l = [i for i in range(1, 10)]
    if n == 4:
        return solve_s(set(l[:n]), 1, 1)
    elif n == 5 or n == 6:
        return solve_s(set(l[:n]), 1, 2)
    elif n == 7 or n == 8:
        return solve_s(set(l[:n]), 1, 3) + solve_s(set(l[:n]), 2, 2)
    elif n == 9:
        return solve_s(set(l[:n]), 1, 4) + solve_s(set(l[:n]), 2, 3)
    
for i in range(4, 10):
    print(solve(i))    

#print(solve(7))

'''
(3,) (4,) {1, 2} 12
12
(4,) (1, 3) {2, 5} 52
52
(3,) (5, 4) {1, 2, 6} 162
162
0
(3,) (5, 8, 2) {1, 4, 6, 7} 1746
(6,) (4, 5, 3) {8, 1, 2, 7} 2718
(2, 4) (5, 7) {8, 1, 3, 6} 1368
(3, 4) (5, 2) {8, 1, 6, 7} 1768
(3, 7) (5, 8) {1, 2, 4, 6} 2146
(5, 8) (6, 4) {1, 2, 3, 7} 3712
13458
(4,) (1, 7, 3, 8) {9, 2, 5, 6} 6952
(4,) (1, 9, 6, 3) {8, 2, 5, 7} 7852
(1, 2) (4, 8, 3) {9, 5, 6, 7} 5796
(1, 8) (2, 9, 7) {3, 4, 5, 6} 5346
(2, 7) (1, 9, 8) {3, 4, 5, 6} 5346
(2, 8) (1, 5, 7) {9, 3, 4, 6} 4396
(3, 9) (1, 8, 6) {2, 4, 5, 7} 7254
(4, 2) (1, 3, 8) {9, 5, 6, 7} 5796
(4, 8) (1, 5, 9) {2, 3, 6, 7} 7632
56370
'''