
def find_prime5(n):
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
    
primes = find_prime5(31623)
sp = set(primes)

def factorize(n):
    if n in sp:
        return [n]
    f = []
    for p in primes:
        if p > n:
            break
        if n % p == 0:
            f.append(p)
            n //= p
            while n % p == 0:
                n //= p
    return f
  
import random
l = [random.randint(1, 10 ** 9) for i in range(10 ** 5)]

for x in l:
    factorize(x)