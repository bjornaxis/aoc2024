ll = []
pl = []

x = 0
y = 0
a = 0
with open("d:\projekt\\aoc2024\d15_real.txt") as file:
    yy = 0
    for line in file:
        if line == "\n":
            a = 1
        elif a == 0:
            ee = []
            b = line.rsplit()
            xx=0
            for j in b[0]:
                if j == '@':
                    x = xx
                    y=yy
                    ee.append('.')
                else:
                    ee.append(j)
                xx+=1
            ll.append(ee)
            yy+=1
            
        else:   
            pl.append(line.rsplit()[0])

ll[y][x] = '@'
for i in ll:
    print(i)
ll[y][x] = '.'


for i in pl:
    for j in i:
        if j == 'v':
            v = [0, 1]
        elif j == '>':
            v = [1, 0]
        elif j == '<':
            v = [-1, 0]
        elif j == '^':
            v = [0, -1]
        else:
            continue
        #print(j,x,y,v)
        if ll[y+v[1]][x+v[0]] == ".":
            y += v[1]
            x += v[0]
        elif ll[y+v[1]][x+v[0]] == "#":
            continue
        else:
            q = 1
            w = 0
            x2 = x
            y2 = y
            while q:
                #print(x2, y2)
                if ll[y2+v[1]][x2+v[0]] == 'O':
                    #print('c')
                    y2 += v[1]
                    x2 += v[0]
                elif ll[y2+v[1]][x2+v[0]] == '.':

                    # blank, flytta
                    q = 0
                    y2 += v[1]
                    x2 += v[0]
                    #print('d', x2,y2)

                    while y2 != y+v[1] or x2 != x+v[0]:
                        #print('g', x2,y2)
                        ll[y2][x2] = 'O'
                        y2 -= v[1]
                        x2 -= v[0]
  
                    ll[y2][x2] = '.'
                    w = 1
                else:
                    # vägg, går inte
                    q = 0
            if w:
                y += v[1]
                x += v[0]
        #ll[y][x] = '@'
        #for i in ll:
        #    print(i)
        #ll[y][x] = '.'


for i in ll:
    print(i)

sum = 0
for y in range(len(ll)):
    for x in range(len(ll[0])):
        if ll[y][x] == 'O':
           sum = sum + y*100+x     
print(sum)
