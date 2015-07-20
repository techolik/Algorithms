#!python3
import math
p2 = [2 ** x for x in range(50)]

def sck(s, c, k):
    m = max(s, c)
    base = 2 ** (m + 1)
    pts = [0 for i in range(base + 1)]
    for i in range(m):
        st = base // (2 ** (i + 1))
        dt = base // (2 ** (i + 2))
        #print(st, dt)
        if i < s:
            for j in range(0, base + 1, st):
                #print(j)
                pts[j] += 1
        if i < c:
            for j in range(dt, base + 1, st):
                #print(j)
                pts[j] += 1
    
    res = 0
    for i in range(0, base + 1):
        if pts[i] >= k:
            res += 1
    
    print(pts)
    return res

def brutal():
	for i in range(1):
		S, C, K = [5, 5, 25]
		for s in range(0, S + 1):
			for c in range(0, C + 1):                    
				for k in range(1, s + 1):
					res = sck(s, c, k)
					rr = -1
					 
					if s == 0 and k == 1:
						rr = 2 ** (c + 1) - 2
					elif k > s:
						rr = 0
					elif k == 1:
						if s > c:
							x = s
						else:
							x = c + 1
					else:
						if (s >= c + k):
							x = max(s, c) + 1 - k
						elif s < c:
							x = s + 2 - k
						else:
							x = max(s, c) + 2 - k
					if rr == -1:
						rr = 2 ** x + 1
						
					#if rr != res:
					print (s, c, k, res, rr)
                                
print(sck(4, 2, 0))
