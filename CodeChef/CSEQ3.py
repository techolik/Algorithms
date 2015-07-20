    
cl = [1]
def factorial2(n, mod):
    if n > len(cl):
        for i in range(len(cl), n):
            cl.append((i + 1) * cl[i - 1] % mod)
    return cl[n - 1]
    
def select7(n, k, mod):
    if n > mod or k > mod:
        n1, k1 = n // mod, k // mod
        n0, k0 = n % mod, k % mod
        if n1 < k1 or n0 < k0:
            return 0
        return select7(n1, k1, mod) * select7(n0, k0, mod)
    
    if n == k or k == 0:
        return 1
    a = factorial2(n, mod)
    b = factorial2(k, mod)
    b = pow(b, mod - 2, mod)
    c = factorial2(n-k, mod)
    c = pow(c, mod - 2, mod)
    return a * b * c % mod
    
def solve2(n, m, p):
    return (select7(m + n, n, p) - 1) % p
        
for t in range(int(input())):
    n, l, r = [int(x) for x in input().split()]
    print (solve2(n, r - l + 1, 10 ** 6 + 3))