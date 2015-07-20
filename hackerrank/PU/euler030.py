m2 = [i ** 2 for i in range(10)]

print(m2)

def cool(l, s):
	ll = [int(x) for x in str(s)]
	return sorted(ll) == sorted(l)
	
def sr(l, s, d):
	ls = []
	if s <= 10 ** d and (s >= 10 ** (d - 2) or (s == 0 and d == 1)):
		#for i in range(1 if d == 1 else 0, 10):
		for i in range(1, 10):
			ss = s + m2[i]
			ll = l + [i]
			if cool(ll, ss):
				ls.append(ll)
			
			lll = sr(ll, ss, d + 1)
			if lll:
				ls.append(lll)
	return ls
	
print(sr([], 0, 1))