#!/usr/bin/python3


file = open('d04_real','r')
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
            ff.append(0)
        k[0] = ff
    m = []
    m.append(0)
    for c in l:
        match c:
            case 'X':
                m.append(1)
            case 'M':
                m.append(2)
            case 'A':
                m.append(3)
            case 'S':
                m.append(4)
            case _:
                m.append(0)
    m.append(0)
    k.append(m)
k.append(ff)

ss2 = len(k)-2
#print(k)
def che(x,y, dx, dy):
    if k[y][x]+1 != k[y+dy][x+dx]:
        return 0
    if k[y+dy][x+dx] == 4:
        return 1
    return che(x+dx,y+dy, dx, dy)

sum = 0
for x in range(ss2):
    for y in range(ss):
        if k[y+1][x+1] == 1:
            for dx in range(3):
                for dy in range(3):
                    sum = sum + che(x+1,y+1, dx-1, dy-1)
print(sum)


sum = 0
for x in range(ss2):
    for y in range(ss):
        if k[y+1][x+1] == 3:
            d1 = 0
            d2 = 0
            if k[y-1+1][x-1+1] == 2 and k[y+1+1][x+1+1] == 4:
                d1 = 1
            if k[y-1+1][x-1+1] == 4 and k[y+1+1][x+1+1] == 2:
                d1 = 1

            if k[y-1+1][x+1+1] == 2 and k[y+1+1][x-1+1] == 4:
                d2 = 1
            if k[y-1+1][x+1+1] == 4 and k[y+1+1][x-1+1] == 2:
                d2 = 1
            if d1 and d2:
                sum = sum+1
print(sum)

