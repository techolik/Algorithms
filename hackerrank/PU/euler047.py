def gcd(a, b):
	while b:
		a, b = b, a % b
	return a
#''' 

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

def pollard_brent(n, small_primes):
    for p in small_primes:
        if n % p == 0:
            return p
    
    y, c, m = randrange(1, n), randrange(1, n), randrange(1, n)
    #m = (y + c) // 2
    g, r, q = 1, 1, 1
    
    while g == 1 or g == n:
        x = y
        for i in range(r):
            #y = (pow(y, 2, n) + c) % n
            #y = ((y ** 2) % n + c) % n
            #y = ((y + y) % n + c) % n
            #y = (y + y + c) % n
            y = (y ** 2 + c) % n

        k = 0
        while k < r and g == 1:
            ys = y
            for i in range(min(m, r - k)):
                y = (y ** 2 + c) % n
                q = q * (x - y if x > y else y - x) % n
                
            g = gcd(q, n)            
            k += m
        r *= 2                
    
    return g
    
def factorization_to(n):    
    primes = find_prime5(n + 1)
    small_primes = primes[:int(n ** 0.5)]
    #sp = {x:1 for x in primes}
    sp = set(primes)
    #print(primes)
        
    def factorize_l(n):
        if n in sp:
            return [n]
        f = []
        for p in primes:
            if p > n:
                break
            while n % p == 0:
                f.append(p)
                n //= p
        return f
    
    cache_size = min(n, 10 ** 3)
    cache = [factorize_l(x) for x in range(1, cache_size + 1)]
        
    factorizations = [0] * n        
    for i in range(1, n + 1):
        if i <= cache_size:
            f = cache[i - 1] 
        elif i in sp:
            f = [i]
        else:
            ft = pollard_brent(i, small_primes)
            f = factorizations[ft - 1] + factorizations[i // ft - 1]
        
        factorizations[i - 1] = f
        
    return factorizations
    
def solve(n, k):
    res = []
    tcount = 0
    for i, fz in enumerate(factorization_to(n + k - 1)):
        fz = list(set(fz))
        #print(i + 1, fz)
        if len(fz) == k:
            tcount += 1
            if tcount == k:
                res.append(i + 2 - tcount)
                tcount -= 1
        else:
            tcount = 0
    
    for r in res:
        print(r)

solve(100, 2)
#solve(2 * 10 ** 6, 5)
        