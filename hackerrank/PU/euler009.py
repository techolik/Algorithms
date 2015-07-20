l = 1500
sq = {x * x: x for x in range(3, l)}
ca = {}
for i in range(3, l):
	for j in range(i, l):
		s = i * i + j * j
		if sq.get(s):
			k = sq[s]
			#print(i, j ,k)
			su = i + j + k
			pr = i * j * k
			c = ca.get(su)
			if c == None or c < pr:
				ca[su] = pr
#print(sq)
print(len(ca))