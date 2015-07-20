#!python3
from array import array

# Cache the input to find the max
l = []
for t in range(int(input())):
    l.append(int(input()))

m = max(l)

a_size = max(m, 10 ** 5)
cache_a = array('I', [1] * a_size) # Space efficient cache
cache_f = [0] * m # Result cache

def solve(n):
    m = 0
    rr = 0
    for i in range(1, n + 1):
        ii = i
        l = []
        fi = 1
        while ii > 1:
            if ii <= a_size:
                fi = cache_a[ii - 1]
            if fi > 1:
                break
                        
            l.append(ii)
                    
            if ii % 2:
                ii = 3 * ii + 1
            else:
                ii //= 2
         
        for t in reversed(l):
            fi += 1
            if t <= a_size:
                cache_a[t - 1] = fi
                
        if fi >= m:
            m = fi
            rr = i
        cache_f[i - 1] = rr

solve(m)
for x in l:
    print(cache_f[x - 1])