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
    
def sums02(n):
    t = [1] * n
    t[0] = 0
    for i in range(2, n // 2 + 1):
        for j in range(2 * i - 1, n, i):
            t[j] += i
    return t
    
def sum_of_factors(n):
    res = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            res += i
            x = n // i
            if i != x:
                res += x
    return res
    
#sums02(10 ** 6)    

def solve(n):
    pre_size = n * 5
    sums = sums02(pre_size)
    
    res = 0
    for i in range(n):
        if sums[sums[i] - 1] == i + 1:
            print(i + 1, sums[i])
            res += (i + 1)
    print (res)
    
solve(300)            