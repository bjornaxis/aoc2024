#!/usr/bin/python3
import copy

file = open('d09_real','r')
a = file.read()
file.close()
sum = 0
b =  a.rsplit()[0]
m=[]

for c in b:
    m.append(int(c))

ll = []
id = 0
for i in range(len(m)//2):
    ll.append([id, m[2*i]])
    id = id+1
    if m[2*i+1] > 0:
        ll.append([-1, m[2*i+1]])

ll.append([id, m[len(m)-1]])


ll2 = copy.deepcopy(ll)
print(ll)
rr = []
while len(ll):
    if ll[0][0] > -1:
        rr.append(ll[0])
        del ll[0]
        continue
    else:
        s = ll[0][1]
        del ll[0]
        while len(ll):
            if s == 0:
                break
            if ll[len(ll)-1][0] == -1:
                del ll[len(ll)-1]
                continue
            if ll[len(ll)-1][1] == s:
                rr.append([ll[len(ll)-1][0], s])
                del ll[len(ll)-1]
                s = 0
                continue
            if ll[len(ll)-1][1] < s:
                rr.append([ll[len(ll)-1][0], ll[len(ll)-1][1]])
                s = s - ll[len(ll)-1][1]
                del ll[len(ll)-1]
                continue
            if ll[len(ll)-1][1] > s:
                rr.append([ll[len(ll)-1][0], s])
                ll[len(ll)-1][1] =  ll[len(ll)-1][1] -s
                s = 0
                continue
sum = 0
idx = 0
for j in rr:
    for k in range(j[1]):
        sum = sum + idx * j[0]
        idx = idx + 1
print(sum)

for j in range(id+1):
    ii = id - j
    ddd = 0
    for k in range(len(ll2)):
        if (ddd):
            break
        if ll2[k][0] == ii:
            for h in range(k):
                if ll2[h][0] == -1:
                    if ll2[k][1] <= ll2[h][1]:
                        tmp = copy.deepcopy(ll2[k])
                        ll2[k][0]=-1
                        ll2.insert(h,  tmp)
                        ll2[h+1][1] = ll2[h+1][1] - tmp[1]
                        ddd = 1
                        break
sum = 0
idx = 0
print(ll2)
for j in ll2:
    for k in range(j[1]):
        if j[0] > 0:
            sum = sum + idx * j[0]
        idx = idx + 1
print(sum)

#00992111777.44.333....5555.6666.....8888..
