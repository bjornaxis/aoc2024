#!/usr/bin/python3


file = open('d05_real','r')
a = file.read()
file.close()
sum = 0
sum2 = 0
in_c = 1
mm = {}

for l in a.splitlines():
    if l == "":
        in_c = 0
        continue
    if in_c:
        b = l.split('|')
        if not b[0] in mm:
            mm[b[0]] = []
        mm[b[0]].append(b[1])
    else:
        b = l.split(',')
        dd = 1
        print(b)
        s = len(b)
        for i in range(s):
            for j in range(i):
                if b[i] in mm:
                    if b[j] in mm[b[i]]:
                        dd = 0
        if dd:
            sum = sum + int(b[(len(b))//2])
        else:
            # reorder
            nlist = []
            while len(b) > 0:
                s = len(b)
                for i in range(s):
                    # find if this page can be added
                    qq = 1
                    for j in range(s):
                        if b[j] in mm:
                            if b[i] in mm[b[j]]:
                                qq = 0
                    if qq:
                        nlist.append(b[i])
                        del b[i]
                        break
            print(nlist)
            sum2 = sum2 + int(nlist[(len(nlist))//2])

print(sum)
print(sum2)
