#!python3
from time import clock
from itertools import permutations
def hash(n):
    return ''.join(sorted(x for x in str(n)))

p10 = [10 ** i for i in range(10)]
hsh = {}

def hash2(n):
    s = 0
    while n:
        s += p10[n % 10]
        n //= 10

    return s

def viable(n):
    return n
#hsh = [hash(i) for i in range(1, 10 ** 7)]

n, k = 2 * 10 ** 6, 6

c = clock()

l = len(str(n))
for p in range(1, l + 1):
    for s in permutations('0123456789', p):
        i = int(''.join(s))
        if i <= n and i > 0 and s[0] != '0':
            h = hash2(i)
            
            t = []
            for j in range(1, k + 1):
                m = i * j
                t.append(m)
                if h != hash2(m):
                    break
            else:
                for m in t:
                    print (m, end=' ')
                print('')

print(clock() - c)