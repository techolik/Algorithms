from collections import Counter

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

def table(n):    
    primes = find_prime5(n + 1)
    sp = set(primes)
    
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
    
    cache_size = min(n + 1, 10 ** 5)
    cache = [factorize_l(i) for i in range(1, cache_size + 1)]
        
    r = []    
    for i in range(1, n + 1):
        if i % 2 == 0:
            a, b = i // 2, i + 1
        else:
            a, b = i, (i + 1) // 2
        
        c = Counter(cache[a - 1] + cache[b - 1])
        s = 1
        for x in c.values():
            s *= (x + 1)
        if not r or s > r[-1]:
            r.append((s, a * b))
            
    return r
                   
#print(factorization_to(100))
t = table(41041)
        
'''
(1, 1, 1)
(2, 3, 2)
(3, 6, 4)
(7, 28, 6)
(8, 36, 9)
(15, 120, 16)
(24, 300, 18)
(32, 528, 20)
(35, 630, 24)
(63, 2016, 36)
(80, 3240, 40)
(104, 5460, 48)
(224, 25200, 90)
(384, 73920, 112)
(560, 157080, 128)
(935, 437580, 144)
(1224, 749700, 162)
(1664, 1385280, 168)
(1728, 1493856, 192)
(2015, 2031120, 240)
(2079, 2162160, 320)
(5984, 17907120, 480)
(10295, 52998660, 512)
(11099, 61599450, 576)
(11703, 68485956, 720)
(16379, 134144010, 768)
(23412, 274072578, 1008)
(27302, 372713253, 1152)
'''
