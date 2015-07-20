#!python3
import math
cl = 10 ** 4
sq = [x ** 2 for x in range(1, cl + 1)]

def solve(d, k):
    r = math.floor(d ** 0.5)
    
    global cl
    global sq
    
    if r > cl:
        sq.extend([x ** 2 for x in range(cl + 1, r + 1)])
        cl = r
    
    c = 1 if r == d ** 0.5 else 0
    
    yl = 1
    for x in range(r, 0, -1):
        y = yl
        if x < y:
            break
        while sq[x - 1] + sq[y - 1] < d:
            #print(x,y, yl)
            y += 1
            yl += 1
        if sq[x - 1] + sq[y - 1] == d:
            print('got', x, y, yl)
            if x < y:
                break
            elif x == y:
                c += 1
            else:
                c += 2
        else:
            #print('miss', x,y, yl)
            if yl > 1:
                yl -= 1
    print(d, c * 4)
    
    #print('possible' if c * 4 <= k else 'impossible')
    
'''
solve(25, 11)
solve(25, 12)

solve(3, 0)
solve(2, 3)
solve(2, 4)
'''

solve(4225, 0)
#for i in range(1, 101):
#    solve(i, 0)