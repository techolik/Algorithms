#!python3
def polygonal(n, k):
    return n * ((k - 2) * n - k + 4) // 2

def poly_of_4(k):
    res = []
    for i in range(1, 10000):
        p = polygonal(i, k)
        if p > 9999:
            break
        if p < 1000:
            continue
        res.append(p)
    
    f2 = {x // 100 : x for x in res}
    
    return f2
        
polies = [poly_of_4(x) for x in range(3, 9)]

def search(s, depth=None, f2=None, l2=None):
    if depth == None:
        depth = len(s)
    res = []
    if depth > 0:
        if l2 == None:
            i = s.pop()
            for poly in polies[i - 3].values():
                r = search(s, depth - 1, poly // 100, poly % 100)
                res.extend(x + [poly] for x in r)                 
        elif l2 > 0:
            for i in s:            
                poly = polies[i - 3].get(l2) 
                if poly:
                    if depth == 1 and f2 == poly % 100:
                        res.append([poly])
                    else:
                        r = search(s.symmetric_difference({i}), depth - 1, f2, poly % 100)
                        res.extend(x + [poly] for x in r)
        
    return res


def solve(s):
    res = search(s)
        
    for x in res:
        print(*reversed(x))
        x.sort()
        
    rres = []
    #print(res)
    for x in res:
        if res.count(x) == 1:
        #if x not in rres:
            rres.append(x)
    #print(rres)        
    for i in sorted(sum(x) for x in rres):
        print(i)
        
        
#solve({6, 5, 4, 3, 7, 8})
#solve({3, 4, 5, 6, 7})
#solve({3, 4, 4})

from itertools import combinations
for i in range(3, 7):
    for combo in combinations([3, 4, 5, 6, 7, 8], i):
        print(combo)
        solve(set(combo))
        print()