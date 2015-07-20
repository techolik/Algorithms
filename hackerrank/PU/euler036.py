def int_to_base(n, base):
    r = ''
    r += str(n % base)
    while n:
        n //= base
        r += str(n % base)
    
    return str(int(r[::-1]))
    
#for i in range(2, 10):    
#    print(int_to_base(20, i))

def solve(n, k):
    r = 0
    for i in range(1, n + 1):
        s = str(i)
        if s == s[::-1]:
            tb = int_to_base(i, k)
            if tb == tb[::-1]:
                r += i
    return r                    
            