from bisect import *

def test(n):
    s = ''
    for i in range(1, n + 1):
        s += str(i)
          
    #for i, c in enumerate(s):
    #    print(i + 1, c)
    #print(len(s))
    #print(s)
    return s

l = [9, 189, 2889, 38889, 488889, 5888889]   
#for i in range(1, 7):  
#    l.append(test(10 ** i - 1))

'''
[9, 189, 2889, 38889, 488889, 5888889]
(180, 20)
(2700, 300)
(36000, 4000)
(450000, 50000)
(5400000, 600000)
'''
#print(l)
#for i in range(1, len(l)):
#    print(l[i] - l[i - 1], (l[i] - l[i - 1]) / 9)

'''
print(test(1000)[249])
print(test(1000)[250])
print(test(1000)[251])
print(test(1000)[252])
print(test(1000)[253])
'''
#print(test(10000)[2889])

pwr = 18
step = [9 * i * 10 ** (i - 1) for i in range(1, pwr)]
base = []
for i in range(pwr - 1):
    if i == 0:
        base.append(step[i])
    else:
        base.append(base[i - 1] + step[i])
#print(base)

def nth(n):
    if n < 10:
        return n
    n -= 1    
    idx = bisect(base, n)
    b = base[idx - 1]
    
    remaining = n - b
    position = remaining // (idx + 1)
    num = 10 ** idx + position
    return int(str(num)[remaining % (idx + 1)])
    
def verify(n):
    a = int(test(n)[n - 1])
    b = nth(n)
    assert(a == b)
    print(n, a, b)

verify(12)    
    
from random import randint
for i in range(10):
    verify(randint(1, 10 ** 4))