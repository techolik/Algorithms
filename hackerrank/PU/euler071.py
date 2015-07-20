
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
    
def gcd(a, b):
	while b:
		a, b = b, a % b
	return a
    
def fraction_reduction(num, denom):
	_gcd = gcd(num, denom)
	return num // _gcd, denom // _gcd
    
def fractions(n):
    c = 0
    #s = set()
    
    sp = set(find_prime5(n + 1))
    
    for den in range(2, n + 1):
        for num in range(1, den):
            if den in sp:
                c += 1
            elif den % 2 == 0 and num % 2 == 0:
                print(num, den, 'no')
                continue
            #if num > 1 and den % num == 0:
            #    continue
            #if den in sp or gcd(num, den) == 1:
            elif gcd(num, den) == 1:
                c += 1
            else:
                print(num, den, 'no')
                #s.add((num, den))
    return c
    #return sorted(s, key=lambda x:float(x[0]) / x[1])
            
#print(fractions(2 * 10 ** 3))
fractions(20)
#for f in fractions(20):
    #print(f)