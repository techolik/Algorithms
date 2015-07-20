import bisect

def solve():
    d = [1, 18, 2, 36, 37, 40, 41, 59, 60]
    #for t in range(int(input())):
    #    d.append(int(input()))

    m = max(d)    
    mm = int((m * 2) ** 0.5) + 1
    
    pan = [0] * mm
    pan[0] = 1
    for i in range(1, mm):
        pan[i] = pan[i - 1] + i + 1
    
    print(pan)    
    
    cache = [0] * m
    for i in range(mm):
        for j in range(mm):
            s = pan[i] * pan[j]
            if s <= m:
                cache[s - 1] = max(cache[s - 1], (i + 1) * (j + 1))
    for i in range(m):
        print(i + 1, cache[i])
    
    cc = []
    for i in range(m):
        if cache[i] > 0:
            cc.append(i + 1)
    
    print(cc)
    
    for dd in d:
        idx = bisect.bisect(cc, dd)
        if cc[idx - 1] != dd:
            if idx < len(cc) and abs(cc[idx] - dd) <= abs(cc[idx - 1] - dd):
                idx += 1
        print(cache[cc[idx - 1] - 1])

solve()