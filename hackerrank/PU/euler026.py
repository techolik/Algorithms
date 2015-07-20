
def div(n):
    for i in range(2, n + 1):
        #print('%.30f' %(1.0 / i))
        print(i, "{:.16f}".format(1.0 / i), 10 ** 40 // i)
        
#div(10 ** 2)        

def long_div(a, b, prec=40):
    dprec = 1
    num, den = a, b
    res = str(num // den) + '.'
    num %= den
    while num and dprec < prec:
        num *= 10
        res += str(num // den)
        num %= den
        dprec += 1
    return res
    
def recurring_len(a, b):
    num, den = a % b, b
    s = set()
    length = 0
    while 1:
        num *= 10
        num %= den
        if num == 0:
            return 0
            
        if num in s:
            return length
        else:
            s.add(num)
        length += 1
    
def test(n):
    for i in range(2, n + 1):
        l = recurring_len(1, i)
        print(i, l, long_div(1, i, l * 2 + 1 if l else 20))
        
test(30)        

# euler follows
from bisect import *
        
l = []
for t in range(int(input())):
    l.append(int(input()))
    
m = max(l)
ls = []
for i in range(2, m):
    ls.append(recurring_len(1, i))

r = []
mls = 0
for j in range(0, len(ls)):
    if mls == 0 or ls[j] > mls:
        mls = ls[j]
        r.append(j + 2)
        
for n in l:
    idx = bisect(r, n - 1)
    print(r[idx - 1])