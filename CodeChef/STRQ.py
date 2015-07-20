# http://www.codechef.com/FEB15/problems/STRQ
from random import randint
from time import clock
from subprocess import call

def chef_count():
	limit = 10000
	q = ['c', 'h', 'e', 'f']
	p = [q[randint(0, 3)] for i in range(limit)]
	ct = clock()
	l,r = 0, limit - 1
	for x in range(1000):
		a = 'c'
		b = 'f'
		#r = randint(1, limit)
		#l = randint(0, r)
		#print (a, b, l, r)
		
		ca = 0
		cr = 0
		for i in range(l - 1, r):
			if p[i] == a:
				ca += 1
			elif p[i] == b:
				cr += ca
		#print (cr)

	print(clock() - ct)
	
'''
ct = clock()
a = 10
for i in range(a ** 4):
	for j in range(a ** 4):
		pass
print(clock() - ct)
'''
q = ['c', 'h', 'e', 'f']

def gen_str(n):
	p = [q[randint(0, 3)] for i in range(n)]
	s = ''
	for x in p:
		s += x;	
	s += '\n'
	return s

def gen_case(n):
	s = ''
	for i in range(n):
		r = randint(1, n);
		l = randint(1, r);
		a = q[randint(0, 3)]
		b = q[randint(0, 3)]
		while b == a:
			b = q[randint(0, 3)]
		s += "%s %s %d %d\n" %(a, b, l, r)
	return s

def gen_file(n):
	s = gen_str(n)
	s += str(n) + '\n'
	s += gen_case(n)
	with open("D:\\My Documents\\Movie\Movie\\Release\\input_gen.txt", 'w') as file:
		file.write(s)
		
	with open("input_gen.txt", 'w') as file:
		file.write(s)
		
#gen_str(10000)
#print(gen_case(10))

#gen_file(1000000)

def benchmark():
	ct = clock()
	call("\"D:\\My Documents\\Movie\\Movie\\Release\\Movie.exe\" < input_gen.txt > output.txt", shell=True)
	print(clock() - ct)

benchmark()
def count():
	stats = {}
	with open("input_gen.txt") as file:
		for line in file:
			if stats.get(line):
				print("duplicate found")
			else:
				stats[line] = 1
	print(len(stats))

def count2():	
	stats = 0
	with open("input_gen.txt") as file:
		for line in file:
			for ch in line:
				stats += 1
	print(stats)
#count()
#count2()