from itertools import *

n = 9#int(input())

def solve(n):
    digits = '0123456789'
    res = 0

    divs = [2, 3, 5, 7, 11, 13, 17]
    for p in permutations(digits[0:n+1]):
        s = ''.join(p)
        #print(p, s)
        for i in range(n - 2):
            ss = int(s[i + 1: i + 4])
            #print(i + 1, i + 3, ss)
            if ss % divs[i]:
                break
        else:            
            res += int(s)   
            
    print(res)         
    
solve(n)    