

nc = {}
l2 = {}
oo = 1

mk = {}

with open('d:\\aoc2024\\d24a_real.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        if line == "\n":
            oo =0
        elif oo:
            a = line.split(': ')
            #print(a)
            nc[a[0]] = int(a[1])
        else:
            a = line.split(' -> ')
            #print(a)
            b = a[0].split(' ')
            c = sorted([b[0], b[2]])
            l2[a[1][:-1]] = [c[0], c[1], b[1] ]
            if b[1] == 'OR':
                mk[a[1][:-1]] = 1
            if c[0] == 'qrw' or c[1] == 'qrw':
                print(a[1][:-1])
            if b[1] == 'XOR' and a[1][:-1][0] != 'z' and c[0][0] != 'x':
                print('ko: ', a[1][:-1])
            
#print(nc)
#print(l2)

loop = 1
while loop:
    loop = 0
    for m in l2:
        if m not in nc:
            loop = 1
            if l2[m][0] in nc and l2[m][1] in nc:
                if l2[m][2] == 'AND':
                        nc[m] = nc[l2[m][0]] & nc[l2[m][1]]
                elif l2[m][2] == 'OR':
                        nc[m] = nc[l2[m][0]] | nc[l2[m][1]]
                elif l2[m][2] == 'XOR':
                        nc[m] = nc[l2[m][0]] ^ nc[l2[m][1]]

tal = 0

for i in nc:
    if i[0] == 'z':
        h = int(i[1:])
        #print(i, h, nc[i])
        tal = tal + (nc[i] << h)
print(tal)

# 44 bitar input
# 45 bitar

xin = []
yin = []
zin = []

for i in range(3,45):
    if i < 10:
        xin.append('x0' + str(i))
        yin.append('y0' + str(i))
        zin.append('z0' + str(i))
    else:
        xin.append('x' + str(i))
        yin.append('y' + str(i))
        zin.append('z' + str(i))

xin2 = []
yin2 = []

# z06
# z31
# z37:


def sw(a,b):
    aa = l2[a]
    bb = l2[b]
    l2[a] = bb
    l2[b] = aa

sw('z06', 'hwk')
sw('z37', 'cgr')
sw('tnt', 'qmd')

sw('z31', 'hpc')




def pr2(h):
    pass
    print([h, l2[h]])

pr2('z31')
pr2('qrw')
pr2('hgw')
pr2('mjr')



cin = {}
cin2 = {}
for i in zin:
    if l2[i][2] != 'XOR':
        print("wrong: zxor: ", i, l2[i])
    else:
        m1 = l2[i][0]
        m2 = l2[i][1]
        a = l2[m1]
        b = l2[m2]
        if a[2] != 'XOR':
            c = a
            a = b
            b = c
            c = m1
            m1 = m2
            m2 = c
        if a[2] != 'XOR':
            print("wrong: xor in", m1, a)
        elif b[2] != 'OR':
            print("wrong: or in", m2, b)
        else:
            cin[i] = m2
            cin2[m2] = 1


and_in = {}

#for u in mk:
#    if u not in cin2:
#        print(u)

for i in cin:
    ii = cin[i]
    #print(i,ii,l2[ii])
    m1 = l2[ii][0]
    m2 = l2[ii][1]
    a = l2[m1]
    b = l2[m2]
    if a[2] != 'AND':
        print("wrongor: ", m1, a)
    elif b[2] != 'AND':
        print("wrongor: ", m2, b)
    else:
        if a[0][0] == 'x':
            e = a
            e2 = b
            mm = m2
        else:
            e = b
            e2 = a
            mm=m1
        and_in[i] = mm
        if int(i[1:]) != (int(e[0][1:]) + 1) :
            print("wrong: ", i, e)

for i in and_in:
    ii = and_in[i]
    #print(ii,l2[ii])
    m1 = l2[i][0]
    m2 = l2[i][1]
    a = l2[m1]
    b = l2[m2]
    if a[2] != 'XOR':
            c = a
            a = b
            b = c
            c = m1
            m1 = m2
            m2 = c
    if a[2] != 'XOR':
            print("wrong and: xor in", m1, a)
    elif b[2] != 'OR':
            print("wrong and: or in", m2, b)
    else:
        if int(i[1:]) != (int(a[0][1:])) :
            print("wrong2: ", i, a)



print(','.join(sorted(['z06', 'hwk', 'z37', 'cgr','tnt', 'qmd','z31', 'hpc'])))



def pr(h):
    pass
    #print([h, l2[h]])

pr('z00')

pr('z01')
pr('dgj')
pr('nvd')

pr('z02')
pr('rbw')
pr('tgb')

pr('ggk')
pr('qwq')

pr('z03')
pr('hrp')
pr('sgn')

pr('gjk')
pr('vvj')

pr('z04')
pr('cjv')
pr('qws')

pr('bvk')
pr('mcf')


