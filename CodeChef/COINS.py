def ca(n):
    cache = [0] * (n + 1)
    cache[0] = 0
    for i in range(1, n + 1):
        c = cache[i // 2] + cache[i // 3] + cache[i // 4]
        cache[i] = c if c > i else i
    return cache

def solve():
    l = [10 ** 10,10 ** 9,10 ** 9,10 ** 9,10 ** 9,10 ** 9,10 ** 8,10 ** 9,10 ** 7]
    #l = [1000032]
    '''
    try:
        while 1:
            l.append(int(input()))
    except:
        pass
    '''
    
    cache_size = 10 ** 2
    cache = ca(min(max(l), cache_size))
    cache2 = {}
    
    def calc(n):
        #global cache
        if n > cache_size:
            if cache2.get(n, 0) == 0:
                c = calc(n // 2) + calc(n // 3) + calc(n // 4)
                r = c if c > n else n
                cache2[n] = r
            return cache2[n]
        else:
            return cache[n]
    
    for ll in l:
        print(calc(ll))
        
solve()        

#print(ca(10))

'''
4243218150
2566393

'''