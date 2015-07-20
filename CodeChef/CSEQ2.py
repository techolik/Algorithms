from random import *

t = 100
l = 10 ** 3
with open('cseq3.txt', 'wt')  as file:
    file.write(str(t) + '\n')
    for i in range(t):
        r = randint(1, l)
        file.write(''.join([str(randint(1, l)), ' ',  str(randint(1, r)), ' ', str(r), '\n']))
