
def fibs(n):
    res = []
    f1, f2 = 1, 2
    count = 1
    index = 2
    while 1:
        f1, f2 = f2, f1 + f2
        index += 1
        #print(f1, f2)
        if f1 > 10 ** count:
            res.append(index)
            count += 1
            if count > n:
                break
    return res
    
print(len(fibs(10000)))