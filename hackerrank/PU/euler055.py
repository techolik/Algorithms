#!python3
from collections import Counter
from time import clock

mapping = {}
def converge(n):
    s = str(n)
    r = s[::-1]
    depth = 0
    while s != r:
        if depth == 60:
            return 0
        
        x = mapping.get(n)
        if x != None:
            return x
         
        n = int(s) + int(r)
        s = str(n)
        r = s[::-1]
        depth += 1
    return n
    
def solve(n):
    for i in range(1, n + 1):
        c = converge(i)
        if c > 0:
            mapping[i] = c
    
    c = Counter(mapping.values())
    for a, b in c.most_common(1):
        print(a, b)
    
c = clock()
solve(10 ** 2)
print(clock() - c)
 

'''
for x in range(26):
    for i in range(0, n, 3):
        s = data[i] ^ (97 + x)
        deq[i] = chr(s)
        if s not in table:
            break
    else:
        res += chr(97 + x)
        break
'''