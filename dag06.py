#!/usr/bin/python3
import copy

file = open('dag06_real','r')
a = file.read()
file.close()
sum = 0

x = 0
y = 0
for l in a.splitlines():
    ss = len(l)
    if not 'k' in vars():
        k = []
        k.append([])
        ff = []
        for i in range(ss+2):
            ff.append(0)
        k[0] = ff
    m = []
    m.append(0)
    x = 0
    y = y + 1
    for c in l:
        x = x + 1
        match c:
            case '.':
                m.append(1)
            case '#':
                m.append(2)
            case '^':
                m.append(1)
                xx=x
                yy=y
                xx2=x
                yy2=y
                p = [0, -1]
                p2 = [0, -1, 0]
                print(x,y)
    m.append(0)
    k.append(m)
k.append(ff)

k2 = []
for i in k:
    w = []
    for j in i:
        w.append(0)
    k2.append(w)


while k[yy][xx] != 0:
    k2[yy][xx] = 1
    if k[yy+p[1]][xx+p[0]] == 2:
        if p[1] == -1:
            p = [1, 0]
        elif p[0] == 1:
            p = [0, 1]
        elif p[1] == 1:
            p = [-1, 0]
        elif p[0] == -1:
            p = [0, -1]
    else:
        yy = yy + p[1]
        xx = xx + p[0]

for i in k2:
    for j in i:
        sum = sum + j

print(sum)


k2 = []
for i in k:
    w = []
    for j in i:
        w.append([])
    k2.append(w)

k3 = copy.deepcopy(k)
k4 = copy.deepcopy(k2)

sum = 0
for ey in range(len(k3)):
    for ex in range(len(k3[0])):
        xx = xx2
        yy = yy2
        p = p2
        loop = 0
        k = copy.deepcopy(k3)
        k2 = copy.deepcopy(k4)
        if ey == yy2 and ex == xx2:
            continue
        if k[ey][ex] != 1:
            continue
        k[ey][ex] = 2

        while k[yy][xx] != 0:
            if p[2] in k2[yy][xx]:
                loop = 1
                break
            else:
                k2[yy][xx].append(p[2])

            if k[yy+p[1]][xx+p[0]] == 2:
                if p[1] == -1:
                    p = [1, 0, 1]
                elif p[0] == 1:
                    p = [0, 1, 2]
                elif p[1] == 1:
                    p = [-1, 0, 3]
                elif p[0] == -1:
                    p = [0, -1, 0]
            else:
                yy = yy + p[1]
                xx = xx + p[0]
        sum = sum+loop

print(sum)
