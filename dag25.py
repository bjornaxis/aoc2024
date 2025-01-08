

mk = []

with open('d:\\aoc2024\\d25_real.txt', 'r') as file:
    for line in file:
        mk.append(line[:-1])                
mk.append('')
print(len(mk))

ll=[]
kk=[]

for i in range(len(mk)//8):
    hh = [0,0,0,0,0]
    for j in range(5):
        d = mk[i*8+1+j]
        if d[0] == '#':
            hh[0] += 1
        if d[1] == '#':
            hh[1] += 1
        if d[2] == '#':
            hh[2] += 1
        if d[3] == '#':
            hh[3] += 1
        if d[4] == '#':
            hh[4] += 1
    if mk[i*8] == '#####':
        ll.append(hh)
    if mk[i*8] == '.....':
        kk.append(hh)


print('lock: ', len(ll))
print('key: ', len(kk))

sum = 0
for i in ll:
    for j in kk:
        ok = 1
        for h in range(5):
            if i[h]+j[h] > 5:
                ok = 0
        sum += ok

print(sum)
