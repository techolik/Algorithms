from math import *

fac = [factorial(x) for x in range(1, 3)]
#fac = [1]
#for i in range(1, len(facts)):
#    fac.append(fac[i - 1] + facts[i])
#print(s)
#for t in range(int(input())):

s = [chr(ord('k') + i) for i in range(3)]
n = 1
r = ''
i = 2
n -= 1
while n and s and i >= 0:
    if n >= fac[i - 1]:
        idx = n // fac[i - 1]
        n %= fac[i - 1]
    else:
        idx = 0
    #print(n, idx, r)
    r += s[idx]
    s.remove(s[idx])
    i -= 1
if s:
    #r += s[0]
    r += ''.join(s)
print(r)