#n, a, b = [int(x) for x in input().split()]
from math import *
 
def solve(n, a, b):
    s = {1}
    if a == 3:
        ia = ib = 2
        aa = ia * (ia + 1) // 2
        bb = ib * (3 * ib - 1) // 2
        while aa < n and bb < n:
            if aa < bb:
                ia += 1
                aa = ia * (ia + 1) // 2
            elif aa > bb:
                ib += 1
                bb = ib * (3 * ib - 1) // 2
            else:
                s.add(aa)
                ia += 1
                ib += 1
                aa = ia * (ia + 1) // 2
                bb = ib * (3 * ib - 1) // 2       
    else:
        ia = ib = 2
        aa = ia * (3 * ia - 1) // 2
        bb = ib * (2 * ib - 1)
        while aa < n and bb < n:
            if aa < bb:
                ia += 1
                aa = ia * (3 * ia - 1) // 2
            elif aa > bb:
                ib += 1
                bb = ib * (2 * ib - 1)
            else:
                s.add(aa)
                ia += 1
                ib += 1
                aa = ia * (3 * ia - 1) // 2
                bb = ib * (2 * ib - 1)                           
    for x in sorted(s):
        print(x)
        
#print(solve(2 * 10 ** 14, 5, 6))
solve(2 * 10 ** 14, 5, 6)
#solve(2 * 10 ** 14, 3, 5)