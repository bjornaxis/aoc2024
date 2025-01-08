#!/usr/bin/python3
import copy

#file = open('d18_test','r')
file = open('d18_real','r')
aa = file.read()
file.close()
sum = 0

b = []

#test
xs = 7
ys = 7
fill = 12

#real
xs = 71
ys = 71
fill = 1024

d = []
for x in range(xs+2):
    d.append(1)
b.append(d)

for y in range(ys):
    d = []
    d.append(1)
    for x in range(xs):
        d.append(0)
    d.append(1)
    b.append(d)

d = []
for x in range(xs+2):
    d.append(1)
b.append(d)


p = []
for l in aa.splitlines():
    k = l.split(',')
    p.append([int(k[0])+1, int(k[1])+1])

print(p)


b2 = copy.deepcopy(b)

for fill in range(len(p)):

    for i in range(fill):
        pp=p[i]
        b[pp[1]][pp[0]] = 1

    #for i in b:
    #    print(i)


    bb = []
    tot_w = []
    for y in range(len(b)):
        bb.append([])
        ee = []
        for x in range(len(b[0])):
            bb[y].append([])
            ee.append(10000000000000000000000)
            if b[y][x] == 0:
                if b[y+1][x] == 0:
                    bb[y][x].append([x,y+1,1])
                if b[y-1][x] == 0:
                    bb[y][x].append([x,y-1,1])
                if b[y][x+1] == 0:
                    bb[y][x].append([x+1,y,1])
                if b[y][x-1] == 0:
                    bb[y][x].append([x-1,y,1])
        tot_w.append(ee)
    #print(bb)

    li = []

    def lin(a):
        for i in range(len(li)):
            if li[i][2] > a[2]:
                li.insert(i,a)
                return
        li.append(a)

    lin([1,1,0])

    tot_w[1][1] = 0

    while(len(li)):
        h = li.pop(0)
        #print('h', h)
        for a in bb[ h[1] ][ h[0] ]:
            q = copy.deepcopy(a)
            #print('a', a)
            q[2] += h[2]
            if q[2] < tot_w[ q[1] ][ q[0] ]:
                tot_w[ q[1] ][ q[0] ] = q[2]
                #print('q',q)
                lin(q)
            #elif q[3] == tot_w[ q[1] ][ q[0] ][ q[2] ][0]:
            #    tot_w[ q[1] ][ q[0] ][ q[2] ][1].append(h)

    #for j in tot_w:
    #    print(j)

    print(fill, p[fill-1][0]-1, p[fill-1][1]-1, tot_w[ys][xs])
