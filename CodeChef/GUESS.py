#!/usr/local/bin/python3

num = int(input());
while num:
  o = input().partition(' ');
  m = int(o[0]);
  n = int(o[2]);
  if (m % 2 and n % 2):
    print (str(((m * n - 1) // 2)) + "/" + str(m * n));
  else:
    print ("1/2");
  num -= 1;