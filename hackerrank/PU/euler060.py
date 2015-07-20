#!python3

from random import randrange

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
        a = randrange(2, n - 2)
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
    
'''   
def cool(a, b, sp):
    #if int(str(a) + str(b)) in sp and int(str(b) + str(a)) in sp:
    if isprime(int(str(a) + str(b)), sp) and isprime(int(str(b) + str(a)), sp):
        return True
    else:
        return False

def solve(n, k):
    primes = find_prime5(n)
    np = len(primes)
    sp = set(primes)
    
    selected = []
    num_selected = 0
    
    while num_selected < k:
        start = selected[-1] if selected else 0
        for i in range(start, np):            
            if num_selected > 0:
                for s in selected:
                    if cool(primes[s], primes[i]) == False:
                        break
                else:                
                    selected.append(i)
                    num_selected += 1
            else:
                selected.append(i)
                num_selected += 1
'''
def test(n, pr=False):
    pre_size = min(n ** 2, 2 * 10 ** 7)
    primes = find_prime5(pre_size)
    sp = set(primes)
    smp = set(primes[:30])
    
    def is_prime(pp):
        if pp < pre_size:
            return pp in sp         
        return isprime(pp, smp)

    #sub = set()
    graph = {}
    edges = 0
    for i, p in enumerate(primes):
        if p == 2 or p == 5:
            continue
        if p >= n:
            break
            
        j = i + 1
        while primes[j] < n:
            pj = primes[j]
            spi, spj = str(p), str(pj)
            if is_prime(int(spi + spj)) and is_prime(int(spj + spi)):
                pass
                graph.setdefault(p, set()).add(pj)
                #graph.setdefault(pj, []).append(p)
                edges += 1
                if pr:
                    print(p, pj)
            j += 1
    
    count = 0
    
    def search(solution, candidate, k):
        
        
    for k, v in graph.items():
        for 
        
    print(len(graph.keys()), count, edges)
 
#test(31, True) 
#test(2 * 10 ** 4)
test(2 * 10 ** 3)
#print(len(find_prime5(2 * 10 ** 4))) # 2262