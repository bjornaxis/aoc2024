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
                    ee.append('.')
                elif j == '.':
                    ee.append('.')
                    ee.append('.')
                elif j == '#':
                    ee.append('#')
                    ee.append('#')
                elif j == 'O':
                    ee.append('[')
                    ee.append(']')

                xx+=2
            ll.append(ee)
            yy+=1
            
        else:   
            pl.append(line.rsplit()[0])

ll[y][x] = '@'
for i in ll:
    print(i)
ll[y][x] = '.'

def ok_to_move(x1,y1,v1):
    if ll[y1][x1] == '#':
        return False
    if ll[y1][x1] == '.':
        return True
    if v1[1] == 0:
        # horizontell
        return ok_to_move(x1 + 2 * v1[0], y1, v1)
    else:
        # vertikal
        if ll[y1][x1] == '[':
            return ok_to_move(x1, y1 + v1[1], v1) and ok_to_move(x1+1, y1 + v1[1], v1)
        else:
            return ok_to_move(x1, y1 + v1[1], v1) and ok_to_move(x1-1, y1 + v1[1], v1)

def do_move(x1,y1,v1):
    if ll[y1][x1] == '#':
        return
    if ll[y1][x1] == '.':
        return
    if v1[1] == 0:
        # horizontell
        if v1[0] == 1:
            do_move(x1 + 2, y1, v1)
            ll[y1][x1+1] = '['
            ll[y1][x1+2] = ']'
            ll[y1][x1] = '.'
        else:
            do_move(x1 - 2, y1, v1)
            ll[y1][x1-2] = '['
            ll[y1][x1-1] = ']'
            ll[y1][x1] = '.'
    else:
        # vertikal
        if ll[y1][x1] == '[':
            do_move(x1, y1 + v1[1], v1)
            do_move(x1+1, y1 + v1[1], v1)
            ll[y1+ v1[1]][x1] = '['
            ll[y1+ v1[1]][x1+1] = ']'
            ll[y1][x1] = '.'
            ll[y1][x1+1] = '.'
            
        else:
            do_move(x1, y1 + v1[1], v1)
            do_move(x1-1, y1 + v1[1], v1)
            ll[y1+ v1[1]][x1] = ']'
            ll[y1+ v1[1]][x1-1] = '['
            ll[y1][x1] = '.'
            ll[y1][x1-1] = '.'
    
for i in pl:
    for j in i:
        #ll[y][x] = '@'
        #for t in ll:
        #    print(t)
        #ll[y][x] = '.'
        #print(j)

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
        if ok_to_move(x+v[0],y+v[1],v):
            #print("ok")
            do_move(x+v[0],y+v[1],v)
            x+=v[0]
            y+=v[1]

for i in ll:
    print(i)

sum = 0
for y in range(len(ll)):
    for x in range(len(ll[0])):
        if ll[y][x] == '[':
           sum = sum + y*100+x     
print(sum)
