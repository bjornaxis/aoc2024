#!/usr/bin/python3
import copy

#ll = [125, 17]
ll = [64554, 35, 906, 6, 6960985, 5755, 975820, 0]


o = {}
o2 = {}

def add(k):
    if k in o:
        return
    m = str(k)
    if k == 0:
        o[k] = [1]
    elif (len(m) % 2) == 0:
        j = len(m)//2
        o[k] = [int(m[0:j]), int(m[j:])]
    else:
        o[k] = [k*2024]

def summ(k, dd):
    add(k)
    if k not in o2:
        o2[k] = {}

    if k in o2:
        if dd in o2[k]:
            return o2[k][dd]

    if dd == 0:
        if dd not in o2[k]:
            o2[k][dd] = len(o[k])
        return len(o[k])
    s = 0;
    for i in o[k]:
        s = s + summ(i, dd-1)
    if dd not in o2[k]:
        o2[k][dd] = s

    return s

sum = 0
for k in ll:    
    sum = sum + summ(k, 74)    

print(sum)

#for i in range(25):
#    ll2 = []
#    for k in ll:
#        m = str(k)
#        if k == 0:
#            ll2.append(1)
#        elif (len(m) % 2) == 0:
#            j = len(m)//2
#            ll2.append(int(m[0:j]))
#            ll2.append(int(m[j:]))
#        else:
#            ll2.append(k*2024)
#    ll = ll2
#    print(i, len(ll))

#print(ll)
#print(len(ll))

