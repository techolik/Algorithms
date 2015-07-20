#!python3

from math import *

def solve(x, y):
	b = int(log2(y))
	xp = x
	for i in range(b):
		xp = xp * x % y
		if xp == 0:
			return True
	else:
		return False
		
print(solve(120, 75))
print(solve(120, 16))
print(solve(7, 49))

'''
from random import *
for i in range(10 ** 4):
	solve(randint(1, 10 ** 18), randint(1, 10 ** 18))
'''