#from collections import Counter

def find_prime5(N):
    correction = N % 6 > 1
    N = {0:N, 1:N-1, 2:N+4, 3:N+3, 4:N+2, 5:N+1}[N%6]
    #sieve = [True] * (N // 3)
    sieve = [True for i in range(N // 3)]
    sieve[0] = False
    for i in range(int(N ** .5) // 3 + 1):
        if sieve[i]:
            k = (3 * i + 1) | 1
            sieve[k*k // 3::2*k] = [False] * ((N//6 - (k*k)//6 - 1)//k + 1)
            sieve[(k*k + 4*k - 2*k*(i%2)) // 3::2*k] = [False] * ((N // 6 - (k*k + 4*k - 2*k*(i%2))//6 - 1) // k + 1)
    return [2, 3] + [(3 * i + 1) | 1 for i in range(1, N//3 - correction) if sieve[i]]

def find_progression(n, l, k):
    res = []
    # Fix a middle element, and 'shrink' from both sides
    for i in range(1, len(l)):
        lo = 0
        hi = len(l) - 1
        while lo < i and i < hi:
            if l[lo] >= n:
                break
            cmp = l[lo] + l[hi] - 2 * l[i]
            if cmp > 0:
                hi -= 1
            elif cmp < 0:
                lo += 1
            else:
                if k == 3:
                    res.append([l[lo], l[i], l[hi]])
                    #return res
                else:
                    # k == 4
                    # If we got a triple, then just try to find another one...
                    for hh in range(hi + 1, len(l)):
                        if l[hh] + l[i] == 2 * l[hi]:
                            res.append([l[lo], l[i], l[hi], l[hh]])
                
                # Shrink on both sides to look for the next triple
                lo += 1
                hi -= 1
    return res
    
#n, k = [int(x) for x in input().split()]
n, k = 10 ** 5, 3

primes = find_prime5(10 ** 6)

d = {}
for p in primes:
    #if p > 10 ** 3:
    d.setdefault(''.join(sorted(i for i in str(p))), []).append(p)

regs = []        
for pa in d.items():
    if len(pa[1]) >= k:
        l = sorted(pa[1])
        if l[0] >= n:
            continue
        
        for reg in find_progression(n, l, k):
            if reg and reg[0] < n:
                regs.append(int(''.join(str(x) for x in reg)))
#print(len(regs))            
for reg in sorted(regs):
    print(reg)