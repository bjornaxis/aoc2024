
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
forth = {}
forth2 = {}
forth_w = {}

forth['A0'] = '<A'
forth['02'] = '^A'
forth['29'] = '>^^A'
forth['9A'] = 'vvvA'

third['A<'] = 'v<<A'
third['<A'] = '>>^A'
third['A^'] = '<A'
third['^A'] = '>A'
third['A>'] = 'vA'
third['>^'] = '<^A'
third['^^'] = 'A'
third['Av'] = '<vA'
third['vv'] = 'A'
third['vA'] = '>^A'


second['Av'] = '<vA'
second['<v'] = '<A'

ll = [
['A', 0 ,2],
['^', 0 ,1],
['>', 1 ,2],
['v', 1 ,1],
['<', 1 ,0]
    ]

for i in ll:
    for j in ll:
        k = i[0]+j[0]
        dx = j[2]-i[2]
        dy = j[1]-i[1]
        m = ""
        if dy <= 0:
            while dx > 0:
                m = m + '>'
                dx -= 1
            while dy < 0:
                m = m + '^'
                dy += 1
            while dx < 0:
                m = m + '<'
                dx += 1
        else:
            while dx > 0:
                m = m + '>'
                dx -= 1
            while dy > 0:
                m = m + 'v'
                dy -= 1
            while dx < 0:
                m = m + '<'
                dx += 1
        m = m+'A'
        print(k,m)
        third[k] = m


ll = [
['A', 3 ,2],
['0', 3 ,1],
['1', 2 ,0],
['2', 2 ,1],
['3', 2 ,2],
['4', 1 ,0],
['5', 1 ,1],
['6', 1 ,2],
['7', 0 ,0],
['8', 0 ,1],
['9', 0 ,2]
    ]

def ts(h):
    tm2 = ""
    tm1 = 'A' + h
    for i in range(len(tm1)-1):
        tm2 = tm2 + third[tm1[i:(i+2)]]
    tm3 = ""
    tm2 = 'A' + tm2
    for i in range(len(tm2)-1):
        tm3 = tm3 + third[tm2[i:(i+2)]]
    return len(tm3)



for i in ll:
    for j in ll:
        k = i[0]+j[0]
        dx = j[2]-i[2]
        dy = j[1]-i[1]
        m = ""
        if dy <= 0:
            while dx > 0:
                m = m + '>'
                dx -= 1
            while dy < 0:
                m = m + '^'
                dy += 1
            while dx < 0:
                m = m + '<'
                dx += 1
        else:
            while dx > 0:
                m = m + '>'
                dx -= 1
            while dy > 0:
                m = m + 'v'
                dy -= 1
            while dx < 0:
                m = m + '<'
                dx += 1
        m = m+'A'
        forth[k] = m

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
        ll = ts(mm)
        if not kk in forth_w:
            forth_w[kk] = ll
            forth2[kk] = mm
        else:
            if ll < forth_w[kk]:
                forth_w[kk] = ll
                forth2[kk] = mm
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
        step([i[2], i[1]], [j[2], j[1]], [0, 0] , m, k)


#for i in forth:
#    print(i, forth[i], forth2[i])

print(forth['37'], forth2['37'], ts("^^<<A"), ts("<<^^A"))
sum = 0
print(kod)
for l in kod:
    l2 = int(l[0:3])
    l = 'A' + l
    m1 = ""
    for i in range(len(l)-1):
        m1 = m1 + forth2[l[i:(i+2)]]
    print(m1)
    m2 = ""
    m1 = 'A' + m1
    for i in range(len(m1)-1):
        m2 = m2 + third[m1[i:(i+2)]]
    print(m2)    
    m3 = ""
    m2 = 'A' + m2
    for i in range(len(m2)-1):
        m3 = m3 + third[m2[i:(i+2)]]
    print(m3)
    print(len(m3), l2)
    sum = sum + len(m3) * l2
print(sum)

