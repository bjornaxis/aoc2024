#!/usr/bin/python3


file = open('02.txt','r')
a = file.read()
file.close()
sum = 0

def che(inp):
    b = inp
    g = int(b[0])
    g2 = int(b[1])
    
    if g < g2:
        v = 1
    if g > g2:
        v = -1
    if g== g2:
        return 0
    dd = 1
    for j in b[1:]:
        h = int(j)
        w = (h-g)*v
        if not (w >0 and w < 4):
            dd = 0
        g = h
    return dd

for l in a.splitlines():
    b = l.split(' ')
    dd = che(b)

    if not dd:
        print(b)
        for j in range(len(b)):
            e = []
            for q in range(len(b)):
                if q != j:
                    e.append(b[q])
            print(e)
            dd2 = che(e)
            if(dd2):
                dd = 1

    if dd:
        sum = sum+1
print(sum)
