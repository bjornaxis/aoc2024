
#test
kod = [
'029A',
'980A',
'179A',
'456A',
'379A']

# real
kod2 = [
'140A',
'180A',
'176A',
'805A',
'638A'
]

kod = kod2

#029A: <vA<A A>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
#980A: <v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A
#179A: <v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
#456A: <v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A
#379A: <v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A

#<vA <A A>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
#v<<A>>^A <A>A vA <^A A >A <vA AA >^A
#<A^A>^^AvvvA
#029A

#    +---+---+
#    | ^ | A |
#+---+---+---+
#| < | v | > |
#+---+---+---+

#+---+---+---+
#| 7 | 8 | 9 |
#+---+---+---+
#| 4 | 5 | 6 |
#+---+---+---+
#| 1 | 2 | 3 |
#+---+---+---+
#    | 0 | A |
#    +---+---+

#v<A <AA ^>>AA<A>vA^AvA^Av<<A^>>AAvA^Av<A^>AA<A>Av<A<A^>>AAA<A>vA^A
#v<<

#<v<A >>^A <vA <A  >>^A A vA A <^A >A <v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
#<A v<A A >>^A
#^<<A
#1

first = {}
second = {}
third = {}
third2 = {}
third_w = {}
forth2 = {}
forth_w = {}

dj = 25

ll = [
['A', 2, 0],
['^', 1, 0],
['>', 2, 1],
['v', 1, 1],
['<', 0, 1]
    ]

def step2(s, e, v, mm, kk):
    if s[0] == 0 and s[1] == 0:
        return
    
    if v[0] == 1:
        mm = mm + '>'
    if v[0] == -1:
        mm = mm + '<'
    if v[1] == 1:
        mm = mm + 'v'
    if v[1] == -1:
        mm = mm + '^'
    ns = [s[0]+v[0], s[1]+v[1]]
    if ns[0] == e[0] and ns[1] == e[1]:
        mm = mm + 'A'
        if kk not in third2:
            third2[kk] = []
        third2[kk].append(mm)
    if ns[0] < e[0]:
        step2(ns, e, [1, 0] , mm, kk)
    if ns[0] > e[0]:
        step2(ns, e, [-1, 0] , mm, kk)
    if ns[1] > e[1]:
        step2(ns, e, [0, -1] , mm, kk)
    if ns[1] < e[1]:
        step2(ns, e, [0, 1] , mm, kk)

for i in ll:
    for j in ll:
        k = i[0]+j[0]
        dx = j[2]-i[2]
        dy = j[1]-i[1]
        m = ""
        step2([i[1], i[2]], [j[1], j[2]], [0, 0] , m, k)


ll = [
['A', 2,3],
['0', 1,3],
['1', 0,2],
['2', 1,2],
['3', 2,2],
['4', 0,1],
['5', 1,1],
['6', 2,1],
['7', 0,0],
['8', 1,0],
['9', 2,0]
    ]


def step(s, e, v, mm, kk):
    if s[0] == 0 and s[1] == 3:
        return
    if v[0] == 1:
        mm = mm + '>'
    if v[0] == -1:
        mm = mm + '<'
    if v[1] == 1:
        mm = mm + 'v'
    if v[1] == -1:
        mm = mm + '^'
    ns = [s[0]+v[0], s[1]+v[1]]
    if ns[0] == e[0] and ns[1] == e[1]:
        mm = mm + 'A'
        if kk not in forth2:
            forth2[kk] = []
        forth2[kk].append(mm)
    if ns[0] < e[0]:
        step(ns, e, [1, 0] , mm, kk)
    if ns[0] > e[0]:
        step(ns, e, [-1, 0] , mm, kk)
    if ns[1] > e[1]:
        step(ns, e, [0, -1] , mm, kk)
    if ns[1] < e[1]:
        step(ns, e, [0, 1] , mm, kk)

for i in ll:
    for j in ll:
        k = i[0]+j[0]
        dx = j[2]-i[2]
        dy = j[1]-i[1]
        m = ""
        step([i[1], i[2]], [j[1], j[2]], [0, 0] , m, k)

for i in third2:
    print(i, third2[i])

#for i in forth2:
#    print(i, forth2[i])

hej = []

def step7(h, jj):
    if len(h) == 1:
        hej.append(jj)
        return
    g = forth2[h[0:2]]
    h2 = h[1:]
    for t in g:
        step7(h2, jj+t)

alles = [ {},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}] 

patt = {}


def ts(h, rr):
    if h in alles[rr]:
        return alles[rr][h]
            
    if rr == 0:
        alles[rr][h] = len(h)
    else:
        varia = [ "" ]
        h2 = 'A'+h
        for i in range(len(h2)-1):
            k6 = third2[h2[i:(i+2)]]
            var2 = []
            for j in varia:
                for k9 in k6:
                    var2.append(j + k9)
            varia = var2
        
        hmin = 100000000000000000000000000
        y=""
        for k6 in varia:
            hsum = 0
            trd = k6[:-1].split('A')
            for g in trd:
                hsum = hsum + ts(g+'A', rr-1)
            if hsum < hmin:
                y = k6
                hmin = hsum

        #print(rr, " ",h, " ", y, hmin)
        alles[rr][h] = hmin        
    return alles[rr][h]

sum=0  
for l in kod:
    print(l)
    l2 = int(l[0:3])
    l = 'A' + l
    hej = []
    step7(l, "")
    hminn = 100000000000000000
    for g7 in hej:
        print(g7)
        hhsum = 0
        trd = g7[:-1].split('A')
        for ii in trd:
            qw = ts(ii+'A',dj)
            #print("ko: ", ii+'A', qw)
            hhsum = hhsum + qw
        #print(g7, hhsum)
        if hhsum < hminn:
            hminn = hhsum
    print(hminn, l2)
    sum = sum + hminn * l2
print(sum)
