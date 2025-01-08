#!/usr/bin/python3
import copy

file = open('d20_real','r')
a = file.read()
file.close()
sum = 0

xs = 0
ys = 0
xe = 0
ye = 0
k = []
y=0

for l in a.splitlines():
    m = []
    x = 0
    for c in l:
        match c:
            case '.':
                m.append(0)
            case '#':
                m.append(-1)
            case 'S':
                m.append(0)
                xs=x
                ys=y
            case 'E':
                m.append(0)
                xe=x
                ye=y
        x = x + 1
    y = y + 1
    k.append(m)

for i in k:
    print(i)
print(ys,xs)
print(ye,xe)

m = []

x=xs
y=ys

ind = 1
k[y][x] = ind
m.append([x,y, ind])
while (x != xe) or (y != ye):
    if k[y+1][x] == 0:
        y=y+1
    elif k[y-1][x] == 0:
        y=y-1
    elif k[y][x+1] == 0:
        x=x+1
    elif k[y][x-1] == 0:
        x=x-1
    ind = ind+1
    k[y][x] = ind
    m.append([x,y, ind])

print(x,y, xe, ye)
print(m)

sc = {}

for l in range(len(m)):
    g = m[l]
    for n in range(l+1,len(m)):
        g2 = m[n]
        l1n = abs(g[0]- g2[0])+abs(g[1]- g2[1])
        if l1n <= 20:
            dd = g2[2] - g[2]
            if dd > l1n:
                if dd-l1n not in sc:
                    sc[dd-l1n] = 0
                sc[dd-l1n] += 1   
print(sc)
sum = 0
for ii in sc:
    if ii > 99:
        print(ii, sc[ii])
        sum = sum + sc[ii]
print(sum)
