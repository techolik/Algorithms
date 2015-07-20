def pw(n):
	i = 1
	t = i ** n
	a = 10 ** (n - 1)
	b = 10 ** n
	while i < 10:
		if t >= a:
			print (n, i, t)
		i += 1
		t = i ** n

for i in range(1, 30):
	pw(i)