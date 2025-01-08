#!/usr/bin/python3
import copy

file = open('d12_real','r')
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
            ff.append('.')
        k[0] = ff
    m = []
    m.append('.')
    for c in l:
        m.append(c)
    m.append('.')
    k.append(m)
k.append(ff)

ss2 = len(k)-2

for j in k:
    print(j)

k3_org = []
for q in k:
    r = []
    for z in q:
        r.append([])
    k3_org.append(r)

k2 = copy.deepcopy(k)

def bb(y,x, c):
    ar = 1
    cir = 0
    c = k[y][x]
    k[y][x] = '.'
    
    if k[y-1][x] == c:
        [aa, cc] = bb(y-1,x, c)
        ar = ar+aa
        cir = cir+cc
    if k[y+1][x] == c:
        [aa, cc] = bb(y+1,x, c)
        ar = ar+aa
        cir = cir+cc
    if k[y][x-1] == c:
        [aa, cc] = bb(y,x-1, c)
        ar = ar+aa
        cir = cir+cc
    if k[y][x+1] == c:
        [aa, cc] = bb(y,x+1, c)
        ar = ar+aa
        cir = cir+cc

    bor = []
    if k2[y-1][x] != c:
        cir = cir+1
        bor.append('t')
    if k2[y+1][x] != c:
        cir = cir+1
        bor.append('b')
    if k2[y][x-1] != c:
        cir = cir+1
        bor.append('l')
    if k2[y][x+1] != c:
        cir = cir+1
        bor.append('r')

    k3[y][x] = bor

    return [ar,cir]

sum = 0
sum2 = 0
for x in range(ss2):
    for y in range(ss):
        if k[y+1][x+1] != '.':
            k3 = copy.deepcopy(k3_org)
            [ar,cir] = bb(y+1, x+1, k[y+1][x+1])
            print (ar, cir)
            sum = sum + ar*cir

            kant = 0
            for yy in range(len(k3)):
                for xx in range(len(k3[0])):

                    if 'r' in k3[yy][xx]:
                        kant = kant+1
                        y2 = yy
                        while 'r' in k3[y2][xx]:
                            k3[y2][xx].remove('r')
                            y2 = y2+1

                    if 'l' in k3[yy][xx]:
                        kant = kant+1
                        y2 = yy
                        while 'l' in k3[y2][xx]:
                            k3[y2][xx].remove('l')
                            y2 = y2+1

                    if 't' in k3[yy][xx]:
                        kant = kant+1
                        x2 = xx
                        while 't' in k3[yy][x2]:
                            k3[yy][x2].remove('t')
                            x2 = x2+1

                    if 'b' in k3[yy][xx]:
                        kant = kant+1
                        x2 = xx
                        while 'b' in k3[yy][x2]:
                            k3[yy][x2].remove('b')
                            x2 = x2+1
            print(kant)
            sum2 = sum2 + ar * kant

print(sum)
print(sum2)
