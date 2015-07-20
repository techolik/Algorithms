#a = int(input())
#b = int(input())

def f(a, b, i):
    return a ^ (b << i)

def solve(a, b):
    n = 314160
    s = a ^ b
    for i in range(1, n):
        s += a ^ (b << i)
        #if i % 10 ** 4 == 0:
        #    s %= (10 ** 9 + 7)       
    print(s % (10 ** 9 + 7))        
    
solve(2, 10)