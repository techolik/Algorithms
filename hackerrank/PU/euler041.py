from itertools import *
import random

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
    
def isprime(n, precision=7):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for repeat in range(precision):
        a = random.randrange(2, n - 2)
        x = pow(a, d, n)
        #x = a ** d % n

        if x == 1 or x == n - 1:
            continue

        for r in range(s - 1):
            #x = pow(x, 2, n)
            x = x ** 2 % n
            if x == 1:
                return False
            if x == n - 1:
                break
        else:
            return False

    return True

def panprime(n):
    pre_size = 10 ** 5
    ps = find_prime5(pre_size)
    sps = set(ps)
    l = []
    for i in range(1, n + 1):
        for per in permutations([str(x) for x in range(1, i + 1)]):
            d = int(per[-1])
            if d % 2 == 0 or d == 5:
                continue
            pan = int(''.join(per))
            if pan < pre_size:
                if pan in sps:
                    l.append(pan)
            else:
                if isprime(pan):
                    l.append(pan)
    return l
print(len(panprime(9)))