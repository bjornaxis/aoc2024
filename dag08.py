sum = 0
k = []
k2 = []
with open("d:\projekt\\aoc2024\d08_real.txt") as file:
    for line in file:
        m = []
        m2 = []
        for b in line.rstrip():
            m.append(b)
            m2.append(0)
        k.append(m)
        k2.append(m2)

xx = len(k[0])
yy = len(k)

for x in range(xx):
    for y in range(yy):
        if k[y][x] != '.':
            for x2 in range(xx):
                for y2 in range(yy):
                    if x == x2 and y == y2:
                        continue
                    if k[y2][x2] != k[y][x]:
                        continue
                    dx = x2-x
                    dy = y2-y
                    dd = 1
                    nyx = x
                    nyy = y
                    while dd:
                        nyx = nyx + dx
                        nyy = nyy + dy
                        if nyx < 0 or nyx >= xx:
                            dd = 0
                            continue
                        if nyy < 0 or nyy >= yy:
                            dd = 0
                            continue
                        k2[nyy][nyx] = 1
sum = 0
for x in range(xx):
    for y in range(yy):
        sum = sum + k2[y][x]
print(sum)

                    
