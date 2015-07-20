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

def solve(n):
    primes = find_prime5(10 ** 6)
    sp = set(primes)
    ma = mb = m = 0
    for a in range(-n, n + 1):
        for b in range(-n, n + 1):
            i = 0
            while True:
                if i * i + a * i + b in sp:
                    i += 1
                else:
                    break
            if i > m:
                m = i
                ma, mb = a, b
    print(ma, mb)

solve(43)
    