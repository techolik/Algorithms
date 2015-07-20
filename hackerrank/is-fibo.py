
def build_dict(n):
	r = [0, 1]
	i = 2
	while 1:
		r.append(r[i - 1] + r[i - 2])
		if r[i] > n:
			r.pop()
			break
		i += 1
	
	d = {}
	for x in r:
		d.setdefault(x, 1)
	return d

d = build_dict(10 ** 10)
n = int(input())
while n:
	x = int(input())
	if d.get(x):
		print('IsFibo')
	else:
		print('IsNotFibo')
	n -= 1
