#!python3

class Intervals:
    def __init__(self):
        self.l = []
    
    def get(self):
        if len(self.l) >= 1:
            ll = 10 ** 9
            y = self.l[0]
            for x in self.l:
                if x[1] - x[0] < ll:
                    ll = x[1] - x[0]
                    y = x
            return y
        else:
            raise KeyError
            
    def add(self, intv):
        self.l.append(intv)
        
    def remove(self, intv):
        try:
            self.l.remove(intv)
        except:
            pass
    
    def shortest(self):
        mm = None
        for x in self.l:
            if not mm or mm > x[1] - x[0]:
                mm = x[1] - x[0]
        return mm
        
    def __repr__(self):
        return str(self.l)
    
    
    def __bool__(self):
        return len(self.l) > 0
    
        
class Teams:    
    def __init__(self, debug=False):
        self.debug = debug
        self.start = {}
        self.end = {}
            
    def add(self, n):
        '''
        if self.debug:
            print('Before ' + str(n) + ':')
            print('\t' + str(self))
        '''    
        sivts = self.start.get(n + 1)
        eivts = self.end.get(n - 1)
        if not sivts and not eivts:
            intv = [n, n]
            self.start.setdefault(n, Intervals()).add(intv)
            self.end.setdefault(n, Intervals()).add(intv)
        elif sivts and not eivts:
            rg = sivts.get()
            rg[0] = n
            sivts.remove(rg)
            self.start.setdefault(n, Intervals()).add(rg)
        elif not sivts and eivts:
            rg = eivts.get()
            rg[1] = n
            eivts.remove(rg)
            self.end.setdefault(n, Intervals()).add(rg)
        else:
            range_start = sivts.get()
            range_end = eivts.get()
            range_start[0] = range_end[0]
            sivts.remove(range_start)
            eivts.remove(range_end)
            self.start[range_start[0]].remove(range_end)
            self.start.setdefault(range_start[0], Intervals()).add(range_start)
            
        if self.debug:
            print('After ' + str(n) + ':')
            print('\t' + str(self))
            print('')
            
    def __repr__(self):
        return 'start: ' + str(self.start) + '\n\tend: ' + str(self.end)
    
def solve(l):
    ints = Teams()
    for x in l:
        ints.add(x)
    res = len(l)
    for x in ints.start.values():
        t = x.shortest()
        #print(t)
        if t != None and t < res:
            res = t
    print(res + 1)
        
#solve([4, 5, 2, 3, -4, -3, -5])
#solve([1, -2, -3, -4, 2, 0, -1])
#solve([3, 2, 3, 1, 4])   
#solve([0, 1, 2, 1, 2, 3, 4, 0, 2, 0, 0, 2, 1, 1, 6, 7, 5])
solve([1, 2, 3, 4, 5, 6, 3, 4])
'''
if __name__ == '__main__':
    with open('in.txt') as file:
        for t in range(int(file.readline())):
            rd = [int(x) for x in file.readline().split()]
            n = rd[0]
            if n == 0:
                print(0)
                continue
            data = rd[1:]
            solve(data)
'''