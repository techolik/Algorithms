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
        
def isprime(n, smp, precision=1):
    for p in smp:
        if n % p == 0 and n != p:
            return False
        
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
    
def solve(n):
    pre_size = int(n ** 0.5 * 6)
    primes = find_prime5(pre_size)
    small_primes = primes[:10]
    sp = set(primes)
    sums = [0]
    
    slen = 1
    mlen = 0
    res = []
    for p in primes:
        last = sums[-1] + p
        start = slen - mlen - 1
        i = start
        while i >= 0:   
            rng = last - sums[i]
            if rng > n:
                break
            leng = len(sums) - i
            if rng < pre_size:                
                if rng in sp:
                    if leng > mlen:
                        mlen = leng
                        res.append((rng, mlen))
            elif isprime(rng, small_primes):
                if leng > mlen:
                    mlen = leng
                    res.append((rng, mlen))
                
            i -= 1
        
        # Already too much...
        if i == start:
            break
            
        sums.append(sums[-1] + p)
        slen += 1
    return res
 
#print(len(solve(10 ** 12)))
for r in solve(10 ** 4):
    #pass
    print(r)
    
'''
(5, 2)
(17, 4)
(41, 6)
(127, 9)
(197, 12)
(281, 14)
(379, 15)
(499, 17)
(857, 19)
(953, 21)
'''