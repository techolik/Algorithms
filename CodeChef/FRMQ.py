#!python3

def test(n, x, y, m):
    mm = m
    n1 = n - 1
    res = set()
    while mm:
        #res.add((x, y) if x < y else (y, x))
        #res.add((x, y))
        if (x,y) not in res:
            res.add((x,y))
            print(x, y)
        x = (x + 7) % n1
        y = (y + 11) % n
        '''
        y = y + 11
        if y > n:
            y %= n
        '''
        mm -= 1
    print(n, n ** 2, m, len(res))
    #for r in res:
    #    print(r)
    
test(15, 1, 2, 10 ** 3)    