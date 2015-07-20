#!python3
# -m cProfile

from itertools import *
from bisect import *

#n, k, l = [int(x) for x in input().split()]
n, k, l = 7, 1, 6
#n, k, l = 6, 6, 1
#n, k, l = 2, 1, 3
#n, k, l = 5, 2, 7
#n, k, l = 3, 2, 4
#n, k, l = 4, 3, 3

def find_prime5(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    correction = n % 6 > 1
    n = {0:n, 1:n-1, 2:n+4, 3:n+3, 4:n+2, 5:n+1}[n % 6]
    sieve = [True] * (n // 3)
    sieve[0] = False
    for i in range(int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = (3 * i + 1) | 1
            sieve[k*k // 3::2*k] = [False] * ((n//6 - (k*k)//6 - 1)//k + 1)
            sieve[(k*k + 4*k - 2*k*(i%2)) // 3::2*k] = [False] * ((n // 6 - (k*k + 4*k - 2*k*(i%2))//6 - 1) // k + 1)
    return [2, 3] + [(3 * i + 1) | 1 for i in range(1, n//3 - correction) if sieve[i]]

def combos(ls, k):
    return combinations(ls, k)
    
def solve():
    primes = find_prime5(10 ** n)
    primes = primes[bisect(primes, 10 ** (n - 1)):]
    set_of_primes = set(primes)
    pow_of_10 = [10 ** i for i in range(n)]
    #mul_of_pow_of_10 = [[pow_of_10[i] * x for i in range(n)] for x in range(10)]
    ls = [x for x in range(n - 1, -1, -1)]

    def swap(n, combo, i):
        pass
        
    families = []
    processed = set()
    
    for p in primes:
        ttsp = []
        for i in range(n):
            ttsp.append(p % 10 * pow_of_10[i])
            p //= 10
        ttsp.reverse()
        
        cool = False
        for combo in combinations(ls, k):
            tsp = ttsp[:]
            mask = 0
            for x in combo:
                mask += pow_of_10[n - x - 1]
                tsp[x] = 0
            masked = sum(tsp)
            if (masked, mask) in processed:
                continue
            else:
                processed.add((masked, mask))
            family = []
            for i in range(10):
                pp = masked + mask * i
                if pp in set_of_primes:
                    family.append(pp)
                    if len(family) == l:
                        families.append(family)
                        cool = True
                        break
            if cool:
                break
                
    if families:
        smallest = []
        for family in families:
            print(family)
            if not smallest or family[0] < smallest[0]:
                smallest = family
        
        #if len(family) == l:                
        for prime in smallest:
            #print(prime, end=' ')
            print(prime)

solve()