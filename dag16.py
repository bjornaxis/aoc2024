#!/usr/bin/python3
import copy

file = open('d16_real','r')
aa = file.read()
file.close()
sum = 0

b = []
bb = []
tot_w = []

ff = []

for l in aa.splitlines():
    d = []
    dd = []
    ee = []
    gg =[]
    for i in l:
        gg.append(0)
        d.append(i)
        dd.append([[], [], [], []])
        #ee.append([10000000000000000000000, 10000000000000000000000, 10000000000000000000000, 10000000000000000000000])
        ee.append([ [10000000000000000000000, []],[10000000000000000000000, []],[10000000000000000000000, []],[10000000000000000000000, []] ])
    b.append(d)
    bb.append(dd)
    tot_w.append(ee)
    ff.append(gg)

# 0 N 1 E 2 S 3 W

for y in range(len(d)):
    for x in range(len(b[0])):
        if b[y][x] == 'S':
            xs = x
            ys = y
            b[y][x] = '.'
        if b[y][x] == 'E':
            xe = x
            ye = y
            b[y][x] = '.'

        if b[y][x] == '.':
            bb[y][x][0].append([x,y,3,1000])
            bb[y][x][1].append([x,y,0,1000])
            bb[y][x][2].append([x,y,1,1000])
            bb[y][x][3].append([x,y,2,1000])
            bb[y][x][0].append([x,y,1,1000])
            bb[y][x][1].append([x,y,2,1000])
            bb[y][x][2].append([x,y,3,1000])
            bb[y][x][3].append([x,y,0,1000])
            if b[y+1][x] == '.':
                bb[y][x][2].append([x,y+1,2,1])
            if b[y-1][x] == '.':
                bb[y][x][0].append([x,y-1,0,1])
            if b[y][x+1] == '.':
                bb[y][x][1].append([x+1,y,1,1])
            if b[y][x-1] == '.':
                bb[y][x][3].append([x-1,y,3,1])

li = []

def lin(a):
    for i in range(len(li)):
        if li[i][3] > a[3]:
            li.insert(i,a)
            return
    li.append(a)

lin([xs,ys,1,0])

tot_w[ys][xs][1][0] = 0
while(len(li)):
    h = li.pop(0)
    #print('h', h)
    for a in bb[ h[1] ][ h[0] ][ h[2] ]:
        q = copy.deepcopy(a)
        #print('a', a)
        q[3] += h[3]
        if q[3] < tot_w[ q[1] ][ q[0] ][ q[2] ][0]:
            tot_w[ q[1] ][ q[0] ][ q[2] ][0] = q[3]
            tot_w[ q[1] ][ q[0] ][ q[2] ][1] = []
            tot_w[ q[1] ][ q[0] ][ q[2] ][1].append(h)
            #print('q',q)
            lin(q)
        elif q[3] == tot_w[ q[1] ][ q[0] ][ q[2] ][0]:
            tot_w[ q[1] ][ q[0] ][ q[2] ][1].append(h)

#for j in tot_w:
#    print(j)

#print(ys,xs)
mmm = 100000000000000000000
for i in tot_w[ye][xe]:
    if i[0] < mmm:
        mmm = i[0]
        st = i

ff[ye][xe] = 1
ff[ys][xs] = 1

def stepj(vv):
    #print(vv)
    for i in vv:
        #print(i, tot_w[i[1]][i[0]][i[2]][1])
        ff[i[1]][i[0]] = 1
        stepj(tot_w[i[1]][i[0]][i[2]][1])

stepj(st[1])
print(st)
sum = 0
for i in ff:
    for j in i:
        sum = sum+j

print(sum)


