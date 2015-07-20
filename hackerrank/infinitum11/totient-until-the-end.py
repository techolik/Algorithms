def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def totients_n(x):
    d = [i for i in range(x + 1)]
    for i in range(2, x + 1):
        if d[i] == i:
            for j in range(i * 2, x + 1, i):
                d[j] = d[j] * (i - 1) // i
            d[i] -= 1

    return d

def solve():
    data = [[2, 2, 3, 1, 3, 1, 6, 1], [1, 1, 1, 1, 1, 1, 1, 1]]
    m = 6
    '''
    for t in range(int(input())):
        l = [int(x) for x in input().split()]
        data.append(l)
        for i, x in enumerate(l):
            if i % 2 == 0:
                m = max(m, x)
    '''
    tot = totients_n(m)
    
    for l in data:
        a, b = l[0], l[1]
        for i in range(2, 8, 2):
            c, d = l[i], l[i + 1]
            ggcd = gcd(a ** b, c ** d)
            
        
