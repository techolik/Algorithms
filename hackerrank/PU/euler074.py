import math
    
def find0(n):
    stats = {}
    pw = [math.factorial(i) for i in range(10)]
    for i in range(0, n + 1):
        #i = int(''.join(sorted(x for x in str(i))))
        #if stats.get(i, []):
        #    continue
        lifar = []
        nt = i
        base = None
        while 1:
            lifar.append(nt)
            
            x = nt
            nt = 0
            while x or nt == 0:
                nt += pw[x % 10]
                x //= 10
                
            if nt in lifar:
                break
                
            if stats.get(nt, []):
                base = stats[nt]
                break
                
        if base:
            for j, b in enumerate(base):
                if b in lifar:
                    j -= 1
                    break
            stats[i] = lifar + base[:j + 1]
            if 0 and j < len(base) - 1:
                print(lifar)
                print(base)
                print(base[:j + 1])
                print(stats[i])
                print 
        else:
            stats[i] = lifar
              
        #print(i, stats[i], len(stats[i]))
    
    res = [[] for i in range(60)]
    for k, v in stats.items():
        res[len(v) - 1].append(k)
    
    for r in res:
        r.sort()
    
    return (res)

def find(n):
    stats = {}
    next = {}
    pw = [math.factorial(i) for i in range(10)]
    for i in range(1, n + 1):
        sofar = set()
        nt = None
        while 1:
            if not nt:
                nt = i
            sofar.add(nt)
            if next.get(nt, 0):
                nt = next[nt]
            else:
                o = nt
                nt = sum(pw[int(x)] for x in str(nt))
                next[o] = nt
            #nt = next.setdefault(nt, sum(pw[int(x)] for x in str(nt)))
            if nt in sofar:
                break
        stats[i] = len(sofar)            
        print(i, stats[i], sofar)
find0(10 ** 3)   
for i, x in enumerate(find0(3 * 10 ** 2)):
    print(i + 1, x)
#find0(10 ** 6)