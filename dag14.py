
ys = 7
xs = 11

ys = 103
xs = 101

xm = (xs)//2
ym = (ys)//2

sum = [0,0,0,0]

k = []
for i in range(ys):
    e = []
    for j in range(xs):
        e.append(0)
    k.append(e)

mmm = []

#with open("d:\projekt\\aoc2024\d14_test.txt") as file:
with open("d:\projekt\\aoc2024\d14_real.txt") as file:
    for line in file:
        b = line.split(' ')
        c = b[0].split('=')[1].split(',')
        p= [int(c[0]), int(c[1])]
        c = b[1].split('=')[1].split(',')
        v= [int(c[0]), int(c[1])]
        mmm.append(p + v)
        pp=[0,0]
        pp[0] = p[0] + v[0] * 100
        pp[1] = p[1] + v[1] * 100
        pp[0] = pp[0] % xs
        pp[1] = pp[1] % ys
        if pp[0] < xm and pp[1] < ym:
            sum[0] += 1
        if pp[0] < xm and pp[1] > ym:
            sum[1] += 1
        if pp[0] > xm and pp[1] < ym:
            sum[2] += 1
        if pp[0] > xm and pp[1] > ym:
            sum[3] += 1
print(sum[0]*sum[1]*sum[2]*sum[3])


rr = 0
while True:
    k = []  
    for i in range(ys):
        e = []
        for j in range(xs):
            e.append(0)
        k.append(e)
    for i in mmm:
        p = [i[0], i[1]]
        v = [i[2], i[3]]
        pp=[0,0]
        pp[0] = p[0] + v[0] * rr
        pp[1] = p[1] + v[1] * rr
        pp[0] = pp[0] % xs
        pp[1] = pp[1] % ys
        k[pp[1]][pp[0]] += 1
    # find a line
    sym = 0
    for i in k:
        ll = 0
        for q in i:
            if q == 0:
                ll = 0
            else:
                ll += 1
            if ll > 20:
                sym = 1
    if sym:
        for i in k:
            for j in i:
                print(j, end="")
            print("")
        break
    if rr % 100:
        print(rr)
    #print(rr)
    rr = rr+1
print(rr)
