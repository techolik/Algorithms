from math import factorial

#n, k = [int(x) for x in input().split()]
n, k = 1000, 10 ** 10

fact = [factorial(x) for x in range(1, n + 1)]
def sel(n, r):
    return fact[n - 1] // fact[r - 1] // fact[n - r - 1]
    
res = 0
for nn in range(1, n + 1):
    for r in range(0, nn + 1):
        if sel(nn, r) > k:
            res += 1

print(res)     