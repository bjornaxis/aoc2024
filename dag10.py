#!/usr/bin/python3
import copy

file = open('d10_real','r')
a = file.read()
file.close()
sum = 0

for l in a.splitlines():
    ss = len(l)
    if not 'k' in vars():
        k = []
        k.append([])
        ff = []
        for i in range(ss+2):
            ff.append(-1)
        k[0] = ff
    m = []
    m.append(-1)
    for c in l:
        m.append(int(c))
    m.append(-1)
    k.append(m)
k.append(ff)

ss2 = len(k)-2
print(k)
k2=[]
for y in range(len(k)):
    q=[]
    for x in range(len(k[0])):
        q.append(0)
    k2.append(q)

def koll(xx,yy, v):
    if kk[yy][xx] != 0:
        return
    if k[yy][xx] != v:
        return
    if v == 9:
        kk[yy][xx] = 2
    else:
        kk[yy][xx] = 1

    koll(xx+1,yy,v+1)
    koll(xx-1,yy,v+1)
    koll(xx,yy+1,v+1)
    koll(xx,yy-1,v+1)

sum = 0
for y in range(len(k)):
    for x in range(len(k[0])):
        if k[y][x] == 0:
            kk = copy.deepcopy(k2)
            koll(x,y,0)
            s = 0
            for y1 in range(len(kk)): 
                for x1 in range(len(kk[0])):
                    if kk[y1][x1] == 2:
                        s = s+1
            print(x,y, s)
            sum = sum + s

print(sum)

def koll2(xx,yy, v):
    if k[yy][xx] != v:
        return 0
    if v == 9:
        return 1

    ee = 0
    ee = ee + koll2(xx+1,yy,v+1)
    ee = ee + koll2(xx-1,yy,v+1)
    ee = ee + koll2(xx,yy+1,v+1)
    ee = ee + koll2(xx,yy-1,v+1)
    return ee

sum = 0
for y in range(len(k)):
    for x in range(len(k[0])):
        if k[y][x] == 0:
            kk = copy.deepcopy(k2)
            s = koll2(x,y,0)
            print(x,y, s)
            sum = sum + s
print(sum)