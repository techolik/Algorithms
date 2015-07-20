def long_div(a, b, prec=40):
    #dprec = 1
    num, den = a, b
    res = str(num // den) + '.'
    num %= den
    dprec = len(str(res)) - 1
    #print(res, dprec)
    while num and dprec < prec:
        num *= 10
        res += str(num // den)
        num %= den
        dprec += 1
    return res
    
def long_div_calc(a, b, prec=40):
    num, den = a, b
    res = sum(int(x) for x in str(num // den))
    dprec = len(str(num // den))
    num %= den
    print(res, dprec)
    while num and dprec < prec:
        num *= 10
        d = num // den
        print(d)
        res += d
        num %= den
        dprec += 1
    return res   
    
def solve_all(n, p, vb=False):    
    def long_div_calc(a, b, prec=40):
        num, den = a, b
        res = sum(int(x) for x in str(num // den))
        dprec = len(str(num // den))
        num %= den
        if vb:
            s = str(res)
        # Performance optimization
        while num and dprec < prec - 100:
            num *= 10 ** 100
            d = num // den
            if vb:
                s += str(d)
            res += sum(int(x) for x in str(d))
            num %= den
            dprec += 100
        while num and dprec < prec:
            num *= 10
            d = num // den
            if vb:
                s += str(d)
            res += d
            num %= den
            dprec += 1
        if vb:
            print(s, a, b)
        return res
        
    tenp = 10 ** (p + 1)
    def solve(n, p):
        #a, b = 2 * n - 1, n
        a, b = n, int(n ** 0.5)
        while 1:
            ap, bp = a * a + n * b * b, 2 * a * b
            if abs(a * bp - ap * b) * tenp < b * bp:
                # a / b - ap / bp < 10 ** (-p), meaning we've got enough precision
                break
            a, b = ap, bp
            
        return long_div_calc(a, b, p)
        
    res = 0
    sqs = set(i ** 2 for i in range(int(n ** 0.5) + 1))
    for i in range(1, n + 1):
        if i not in sqs:
            r = solve(i, p)
            if vb:
                rt = 0
                for x in str(i ** 0.5)[0: p + 1]:
                    if x != '.':
                        #print(x)
                        rt += int(x)
                print(i, r, rt)
                assert(r == rt)
            res += r
    print(res)
#solve_all(int(input()), int(input()))    

solve_all(1000, 13, True)
#solve_all(97, 10000)
#solve_all(93, 10000)

print(long_div(1441629220732621056, 142742563079178240))
print(long_div_calc(1441629220732621056, 142742563079178240, 13))
#print(long_div_calc(1358779425194943601,135203606136112080, 13))

        