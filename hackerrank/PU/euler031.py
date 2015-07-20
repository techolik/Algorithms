#!python3

coins = [1, 2, 5, 10, 20, 50, 100, 200]

cache = {}
# aci available coin index
def solve(n):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    lc = 8
    cache = [[0] * n for i in range(lc)]
    cache[0] = [1 for i in range(n)]
    
    #for i, p in enumerate(primes[]):
    for i in range(1, lc):
        c = coins[i]
        for j in range(1, n + 1):
            r = 0
            remaining = j            
            while remaining > c:
                remaining -= c
                r += cache[i - 1][remaining - 1]
            if remaining == c:
                r += 1
                
            cache[i][j - 1] = (cache[i - 1][j - 1] + r) % (10 ** 9 + 7)
    
    #for c in cache:
    #    print(c)
        
    return cache

def solve2(n):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    def count(m, n):
        if n == 0:
            return 1
     
        if n < 0:
            return 0
     
        if m <= 0 and n >= 1:
            return 0
     
        return count(m - 1, n) + count(m, n - coins[m - 1])
    return count(8, n)
    
#print(solve2(10 ** 2))

def solve3(n):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    lc = 8
    cache = [[0] * n for i in range(lc)]
    cache[0] = [1 for i in range(n)]
    
    for i in range(1, lc):
        c = coins[i]
        for j in range(1, n + 1):
            if j > c:
                r = cache[i][j - c - 1]
            elif j == c:
                r = 1
            else:
                r = 0
            cache[i][j - 1] = (cache[i - 1][j - 1] + r) % (10 ** 9 + 7)
    
    #for c in cache:
    #    print(c)
        
    return cache
    #return cache[-1][-1]
    
def coins_dumb(n):
    if n == 0:
        return [[]]
    if n == 1:
        return [[1]]
        
    r = []
    for x in reversed(coins):
        if n >= x:
            rr = coins_dumb(n - x)
            r.extend(rrr + [x] for rrr in rr)
    res = []
    for ll in r:
        lls = sorted(ll)
        if lls not in res:
            res.append(lls)
    return res

def verify(n):
    r = solve3(n)
    rd = coins_dumb(n)
    print(r, len(rd))
    
#verify(10)
#solve(5 * 10 ** 3)
solve3(10 ** 5)

#for c in solve3(10):
#    print(c)

'''
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 2, 2, 3, 3, 4, 4, 5, 5, 6]
[1, 2, 2, 3, 4, 5, 6, 7, 8, 10]
[1, 2, 2, 3, 4, 5, 6, 7, 8, 11]
[1, 2, 2, 3, 4, 5, 6, 7, 8, 11]
[1, 2, 2, 3, 4, 5, 6, 7, 8, 11]
[1, 2, 2, 3, 4, 5, 6, 7, 8, 11]
[1, 2, 2, 3, 4, 5, 6, 7, 8, 11]
'''
#cns = coins_dumb(20)
#print(len(cns))
#for i in range(1, 201):
#    print(i, num_of_ways(i, 8), i * i)
#for p in cns:
#    print(p)