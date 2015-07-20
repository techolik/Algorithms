# https://www.hackerrank.com/challenges/unbounded-knapsack
import bisect

for i in range(int(input())):
    n, k = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
	
	# Remove duplicate, they're of no use
    A = list(set(A))
	
    A.sort()
    #print(data)
    
	# The cache
	t = []
	
    for i in range(1, k + 1):
        s = 0
		
        if i >= A[0]:                   
            idx = bisect.bisect_left(A, i)
            if idx < len(A) and A[idx] == i:
				# If i is found in A, then just select i
                s = i
            else:
				# t[k] = max(A[j] + t(k - A[j]) for j in (0, idx - 1)
                for j in range(idx):
                    s = max(s, A[j], t[i - A[j] - 1])
                    if s == i:
                        break
						
                    c = A[j] + t[i - A[j] - 1]
                    if c > s and c <= i:
                        s = c
        t.append(s)
		
    print (t[k - 1])
