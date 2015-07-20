from time import clock
from collections import Counter
#from random import randint

def gcd(a, b):
    if b == 0:
        return a
    while b:
        a, b = b, a % b
    return a
    
def abundant_nums(n):
    t = [[1] for i in range(n)]
    for i in range(2, n // 2 + 1):
        j = 2
        while j <= n // i:
            t[i * j - 1].append(i)
            j += 1
    
    print(t)
    abn = []
    for i in range(n):
        if sum(t[i]) > i + 1:
            abn.append(i + 1)
    
    return abn
    
#print(len(abundant_nums(10 ** 5)))
#abundant_nums(100)

def sum_of_factors(n):
    res = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            res += i
            x = n // i
            if i != x:
                res += x
    return res

def sums(n):
    res = []
    for i in range(1, n + 1):
        res.append(sum_of_factors(i))
    return res
#print(sum_of_factors(18))

def sums0(n):
    t = [[1] for i in range(n)]
    for i in range(2, n // 2 + 1):
        j = 2
        while j <= n // i:
            t[i * j - 1].append(i)
            j += 1
    return [sum(x) for x in t]

def sums01(n):
    t = [[1] for i in range(n)]
    for i in range(2, n // 2 + 1):
        for j in range(2 * i - 1, n, i):
            t[j].append(i)
    return [sum(x) for x in t]
    
def sums02(n):
    t = [1 for i in range(n)]
    t[0] = 0
    for i in range(2, n // 2 + 1):
        for j in range(2 * i - 1, n, i):
            t[j] += i
    return t
    
def factors2(fts, n):
    res = set([1])
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            #print(n, i)
            res.add(i)
            res.add(n // i)
            res.update(fts[i - 1])
            res.update(fts[n // i - 1])
            break
    for x in list(res):
        if x != 1:
            res.add(n // x)
    return res
    
def sums2(n, pt=False):
    fts = []
    for i in range(1, n + 1):
        fts.append(factors2(fts, i))
    if pt:
        for i in range(0, len(fts)):
            print(i + 1 ,fts[i])
    return [sum(x) for x in fts]
    
def factors3(fts, n):
    res = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            #print(n, i)
            res.append(i)
            res.append(n // i)
            res.extend(fts[i - 1])
            res.extend(fts[n // i - 1])
            break
    for i in range(0, len(res)):
        if res[i] != 1:
            res.append(n // res[i])
    return list(set(res))
    
def factorization_to(n):    
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
        
    primes = find_prime5(n + 1)
    sp = set(primes)
        
    def factorize_small(n):
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
    cache = [factorize_small(x) for x in range(1, cache_size + 1)]
        
    def factorize_large():            
        factorizations = cache + [False] * (n - cache_size)
        
        small_primes = primes[5:10 ** 3] # the last prime in the list has to be >= sqrt of n
        #print(small_primes[-1])
        for i in range(cache_size + 1, n + 1):
            if i % 2 == 0:
                factorizations[i - 1] = factorizations[1] + factorizations[i // 2 - 1]
            elif i % 3 == 0:
                factorizations[i - 1] = factorizations[2] + factorizations[i // 3 - 1]
            elif i % 5 == 0:
                factorizations[i - 1] = factorizations[4] + factorizations[i // 5 - 1]
            elif i % 7 == 0:
                factorizations[i - 1] = factorizations[6] + factorizations[i // 7 - 1]
            elif i % 11 == 0:
                factorizations[i - 1] = factorizations[10] + factorizations[i // 11 - 1]
            elif i in sp:
                factorizations[i - 1] = [i]
            else:
                #ft = pollard_brent(i, small_primes)
                for ft in small_primes:
                    if i % ft == 0:
                        break            
                factorizations[i - 1] = factorizations[ft - 1] + factorizations[i // ft - 1]
                        
        return factorizations
        
    return factorize_large()
    
def sums3(n):
    factorizations = factorization_to(n)
    sums = [0] * n
    #pow_cache = {}
    for j, fact in enumerate(factorizations):
        s = 1
        d = Counter(fact)
        for x in d.keys():
            y = 1
            for i in range(d[x]):                
                y += x ** (i + 1)
            s *= y
        sums[j] = s - j - 1
        
    return sums
    
def find_prime3(x):
    d = [1 for i in range(x + 1)]
    d[0] = 0
    d[1] = 0
    for i in range(2, int(x ** 0.5) + 1):
        if d[i]:
            for j in range(i ** 2, x + 1, i):
                d[j] = 0

    return [i for i in range(x + 1) if d[i]]

primes = find_prime3(10 ** 5)

def factorize_d(n):
    d = {}
    for p in primes:
    #for i in range(0, len(primes)):
    #    p = primes[i]
        if p > n:
            break
        while n % p == 0:
            '''
            try:                
                d[p] += 1
            except KeyError:
                d[p] = 1
            '''
            if d.get(p):
                d[p] += 1
            else:
                d[p] = 1
            
            n /= p
    
    return d

def factorize_l(n):
    l = []
    for p in primes:
        if p > n:
            break
        while n % p == 0:
            l.append(p)            
            n /= p
    
    return l

factorization = []
def factorize_c(n):
    c = Counter()
    for p in primes:
        if p > n:
            break
        if n % p == 0:
            if n == p:
                c[n] = 1
            else:
                #print(len(factorization), p, n/p, n)
                c = factorization[p - 2] + factorization[n / p - 2]    
    
    factorization.append(c)
    return c
    
def sopd(n):
    s = 1
    d = factorize_d(n)
    for x in d.keys():
        y = 1
        for i in range(d[x]):
            y += x ** (i + 1)
        s *= y

    return s - n

def sums4(n):
    s = [1]
    ps = set(primes)
    for i in range(2, n + 1):
        '''
        if i in ps:
            x = 1
        else:
        '''
        x = sopd(i)
        s.append(x)
    return s

cache = {}
def LeastPower(a, x):
    #key = a * 10 ** 5 + x
    #if cache.get(key):
    #    return cache[key]
    b = a
    while x % b == 0:
        b *= a
    
    #cache[key] = b
    return b

def SumDivisors(x):
    t = x
    result = 1

    # Handle two specially.
    p = LeastPower(2, t)
    result *= p-1
    t /= p/2

    # Handle odd factors.
    for i in range(3, int(t ** 0.5) + 1, 2):
        p = LeastPower(i, t)
        result *= (p-1) / (i-1)
        t /= p/i

    # At this point, t must be one or prime.
    if 1 < t:
        result *= 1+t

    return result - x

def pollard_rho(n):
    #l = []
    i = 1
    k = 2
    y = x = randint(0, n - 1)
    while 1:
        i += 1
        x = (x ** 2 - 1) % n
        d = gcd(y - x, n)
        if d != 1 and d != n:
            return d
        if i == k:
            y = x
            k *= 2
    #return l
            
#print(pollard_rho(24))

def sums5(n):
    s = [1]
    for i in range(2, n + 1):
        s.append(SumDivisors(i))
    return s
        
def evaluate(funcs): 
    for func in funcs:
        c = clock()
        s1 = func(10 ** 4)
        print(clock() - c, func.__name__)
        #print(sum(s1))

#evaluate([sums0, sums02, sums3, sums2])
#evaluate([sums0, sums, sums2, sums4, sums5, sums6])
#print(sums3(15))
#sums3(10 ** 5)
#assert(sums0(15) == sums01(15))
#print(sums0(15))
#print(sums(15))
sums(10 ** 5)
'''
s = sums0(60)
for i in range(0, len(s)):
    print(i + 1, s[i], s[i] + i + 1, factorize_l(i + 1))
'''