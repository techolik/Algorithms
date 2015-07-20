
def gcd(a, b):
	while b:
		a, b = b, a % b
	return a
    
def solve(n):
    max_odd = int(n ** 0.5) + 1    
    r = [0] * n
    for p in range(3, max_odd, 2):
        for q in range(1, p, 2):
            if gcd(q, p) == 1:
                nsu = su = p * (p + q)
                print(su, p, q, p * q, (p * p - q * q) / 2, (p * p + q * q) / 2)
                while nsu <= n:
                    r[nsu - 1] += 1
                    nsu += su 
    ca = {}    
    for i in range(n):
        if r[i] > 0:
            ca[i + 1] = r[i]
    return ca
    
ca = solve(360)
print(ca)
print(len(ca))
print(ca[120])

'''
5108
3
         49997476 function calls in 13.044 seconds

new:
10 ** 4 [12, 60, 120, 240, 360, 720, 840, 1260, 1680, 2160, 2520, 5040, 7560]
        [12, 60, 120, 240, 420, 720, 840, 1680, 2520, 4620]

old:
10 ** 4 [12, 60, 120, 240, 420, 720, 840, 1680, 2520, 4620, 5040, 9240]         
         

'''