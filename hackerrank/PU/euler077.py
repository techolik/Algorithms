def find_prime5(n):
    n += 1
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
    
def solve(n):
    primes = find_prime5(n)
    lp = len(primes)
    cache = [[0] * (n - 1) for i in range(lp)]
    cache[0] = [1 - i % 2 for i in range(2, n + 1)]
    
    #for i, p in enumerate(primes[]):
    for i in range(1, lp):
        p = primes[i]
        for j in range(2, n + 1):
            r = 0
            remaining = j            
            while remaining > p + 1:
                remaining -= p
                r += cache[i - 1][remaining - 2]
            if remaining == p:
                r += 1
                
            cache[i][j - 2] = cache[i - 1][j - 2] + r
    
    #for c in cache:
    #    print(c)
        
    print(cache[lp - 1][n - 2])
    
solve(5)
solve(10)
solve(20)
solve(10 ** 3)
#solve(5 * 10 ** 3)