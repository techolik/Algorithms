    
def gcd(a, b):
	while b:
		a, b = b, a % b
	return a
    
def fraction_reduction(num, denom):
	_gcd = gcd(num, denom)
	return num // _gcd, denom // _gcd
    
def int_to_list(n):
    l = []
    while n:
        l.append(n % 10)
        n //= 10
    return l

def reduced_digit(i, ri):
    li, lri = sorted(int_to_list(i)), sorted(int_to_list(ri))
    a = b = 0
    lr = []
    while a < len(li) and b < len(lri):
        if li[a] != lri[b]:
            lr.append(li[a])
            a += 1
        else:
            a += 1
            b += 1
    if a == len(li) and b == len(lri):
        return lr
    else:
        return []

def reduced_digit2(i, j):
    li, lj = int_to_list(i), int_to_list(j)
    lr = []
    for x in li:
        if x in lj:
            lr.append(x)
            li.remove(x)
            lj.remove(x)
    return lr, li, lj
    
def solve(n, k):
    resi = resj = 0
    start = 10 ** (n - 1)
    end = 10 ** n
    for i in range(start, end):
        for j in range(start, i):
            g = gcd(i, j)
            if g > 1:
                ri, rj = i // g, j // g
                st, ed = start // (10 ** k), end // (10 ** k)
                if ri * j == rj * i and st <= ri <= ed and st <= rj <= ed:
                    #print(i, j, ri, rj)
                    rd, rdi, rdj = reduced_digit2(i, j)
                    if rd and rd[-1] != 0 and rdi == rdj:
                        print(i, j, ri, rj, rd, rdi, rdj)
                        resi += i
                        resj += j
                        #if rdi == rdj:
                        #    print(i, j, ri, rj)
                    
    return resi, resj
    
print(solve(2, 1))    