def f(m, n):
    if m > n:
        return f(n, m)
    if m == 1:
        return n + 1
    
    return f(m - 1, n) + f(m, n - 1)

for i in range(1):
    a, b = [500, 500]
    if a > b:
        a, b = b, a
    cache = [[] for i in range(a)] 
    for i in range(a):
        if i == 0:
            cache[i] = [x + 2 for x in range(b)]
        else:
            for j in range(0, b - i):
                #print(i, j)
                if j == 0:
                    cache[i].append(2 * cache[i - 1][j + 1])
                else:
                    cache[i].append(cache[i - 1][j + 1] + cache[i][j - 1])
    #print (cache)
    print(cache[a - 1][b - a])
    print(cache[a - 1][b - a] % (10 ** 9 + 7))
    #print(f(a, b) % (10 ** 9 + 7))
    