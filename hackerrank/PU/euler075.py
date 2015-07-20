def gcd(a, b):
	while b:
		a, b = b, a % b
	return a
    
def solve(n, pr=False):
    max_odd = int(n ** 0.5) + 1    
    r = [0] * n
    for p in range(3, max_odd, 2):
        for q in range(1, p, 2):
            if gcd(p, q) == 1:
                nsu = su = p * (p + q)
                while nsu <= n:
                    r[nsu - 1] += 1
                    nsu += su
            
    ca = [0] * (n + 1)
    for i in range(n):
        if r[i] == 1:
            ca[i + 1] = ca[i] + 1
            if pr:
                print(i + 1)
        else:
            ca[i + 1] = ca[i]
        
    return ca

l = [11, 12, 13, 50, 10 ** 3, 39, 40, 48, 216, 5 * 10 ** 6]
    
res = solve(max(l))

for ll in l:
    print(res[ll])

#for i, c in enumerate(solve(10 ** 3)):
#    print(i, c)

#solve(10 ** 2, True)