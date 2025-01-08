#!/usr/bin/python3
import copy

#file = open('d19_test','r')
file = open('d19_real','r')
a = file.read()
file.close()
aa = a.splitlines()


v = aa[0].split(', ')
print(v)
t = aa[2:]

sum = 0

ff2 = {}

def mt(s):
    #print("hej", s)
    sss = 0
    for i in range(len(s)):
        ee = s[0:(i+1)]
        ff = s[(i+1):]
        if ee in v:
            #print(s,ee,ff)
            if len(ff) > 0:
                if ff not in ff2:
                    gg = mt(ff)
                    ff2[ff] = gg
                else:
                    gg = ff2[ff]
                sss += gg
            else:
                sss += 1
        else:
            continue
    return sss

for l in t:
    done = 0
    w = mt(l)
    print(l, w)
    sum += w

print(sum)

