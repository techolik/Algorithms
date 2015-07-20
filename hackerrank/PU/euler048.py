from time import clock
def pp(i, stp, mstp):
    p = 1
    for j in range(i // stp):
        for k in range(mstp):
            p *= (i ** (stp // mstp))
            p %= 10 ** 10
    for j in range(i % stp):
        p *= i
        p %= 10 ** 10
    return p
                
def solve(n):
    r = 0
    for i in range(1, n):
        if 0:
            p = pp(i, 800, 5)
        else:
            p = pow(i, i, 10 ** 10)
        r += p
        r %= 10 ** 10

    print(r)
    
c = clock()
# 6936530900
solve(10 ** 6)
print(clock() - c)