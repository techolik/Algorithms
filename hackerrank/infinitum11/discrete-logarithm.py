#!python3
import math

def solve(a, b, g):
    sqf = g ** 0.5
    sq = math.floor(sqf)
    preset = {pow(a, math.floor((i + 1) * sqf), g): i for i in range(sq)}
    #preset = {a ** int((i + 1) * sqf) % g: i for i in range(sq)}
    r = None
    for j in range(sq):
        right = (b * (a ** j)) % g
        f = preset.get(right, -1)
        if f != -1:
            rr = (f + 1) * sq - j
            #print(f, j, right, rr)
            if r == None or rr < r:
                r = rr
    print(r)
    
#solve(2, 5, 17)    
solve(2, 70, 131)
'''
(101, 77, 86209L, 57897)
(243, 231, 45331L, 139251)
(385, 385, 233555L, 220605)
(527, 539, 305371L, 301959)
57897
'''
#solve(233529, 184091, 329746)
#solve(26161, 23893, 62356)
#solve(126995,142647,270599)