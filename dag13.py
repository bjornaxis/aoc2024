#!/usr/bin/python3
import copy

file = open('d13_real2','r')
aa = file.read()
file.close()
sum = 0

for l in aa.splitlines():
    s = l.split(' ')
    s = s[0:-1]
    a = int(s[0])
    b = int(s[2])
    c = int(s[1])
    d = int(s[3])
    m1 = int(s[4]) + 10000000000000
    m2 = int(s[5]) + 10000000000000
    det = a*d-b*c
    q1 = d*m1-b*m2
    q2 = -c*m1+a*m2
    if det == 0:
        print("hej")
        print(a,b,c,d,m1,m2)
    if q1 % det == 0 and q2 % det == 0:
        sum = sum + (q1 // det) * 3 + (q2 // det)
    
print(sum)