#!python3
from random import randint

def sums(a, b):
    return sum([abs(a[i] - b[i]) for i in range(0, len(a))])
def cost(s, t, pt=False):  
    lb = []
    lg = []
    rb = []
    rg = []
    nb = ng = 0
    for i in range(0, len(s)):
        if s[i] == 'B':
            nb += 1
            if i % 2:
                # Should be 'G'
                lb.append(i)
            else:
                rb.append(i)
        else:
            ng += 1
            if i % 2 == 0:
                # Should be 'B'
                lg.append(i)
            else:
                rg.append(i)
    
    if pt:
        print(s, t, nb, ng, lb, lg, rb, rg)
    
    if nb - ng > 1 or nb - ng < -1:
        return -1
    if nb - ng == -1 or len(rb) == 0:
        lb = rb
        lg = rg
    
    if pt:
        print(s, t, nb, ng, lb, lg, rb, rg)
    
    assert(len(lb) == len(lg))
    #print(lb, lg, rb, rg)
    if t == 0:
        if nb == ng:
            return min(len(lb), len(rb))
        else:
            return len(lb)
    else:
        #return min(sums(lb, lg), sums(rb, rg))
        
        if len(rb) == len(rg):
            return min(sums(lb, lg), sums(rb, rg))
        else:
            return sums(lb, lg)
        
'''
assert(cost('BBBGG', 0) == 1)    
assert(cost('BBBGG', 1) == 3)   
assert(cost('BGBGB', 1) == 0)   
assert(cost('GBGBG', 2) == 0) 
 
assert(cost('BBGGG', 0) == 1)
assert(cost('BBGGG', 1) == 3)

assert(cost('GGGGG', 0) == -1)
assert(cost('BBGBB', 1) == -1)
   
assert(cost('BGBGG', 0) == 2)
assert(cost('BGBGG', 1) == 2)
   
assert(cost('BBGGBBGG', 0) == 2)
assert(cost('BBGGGGBB', 1) == 4)
assert(cost('BBBBGGGG', 1) == 6)

assert(cost('BGBGBGBG', 1) == 0)

assert(cost('GBGBGBGB', 1) == 0)

assert(cost('BB', 1) == -1)
'''

def test_all(s):
    print(s)
    print(0, cost(s, 0))
    print(1, cost(s, 1))
    #print(2, cost(s, 2))
        
#print(cost('GBGGBB', 1, True))
#print(cost('GBGGBB', 0, False))
test_all('GGBB')
test_all('GBBBG')
test_all('GGBBB')
test_all('GGGBBB')
test_all('GGBGBB')
test_all('GBGGBB')
test_all('GBBBGBG')

test_all(''.join (['B', 'G'][randint(0, 1)] for i in range(7)))
#print(cost(''.join (['B', 'G'][randint(0, 1)] for i in range(4)), 0))