

nc = {}

with open('d:\\aoc2024\\d23_real.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        # Print each line
        a = line.strip().split('-')
        if a[0] not in nc:
            nc[a[0]] = []
        if a[1] not in nc:
            nc[a[1]] = []
        nc[a[1]].append(a[0])
        nc[a[0]].append(a[1])

sum = 0
for i in nc:
    if i[0] == 't':
        v = nc[i]
        for j1 in v:
            for j2 in v:
                if j1 == j2:
                    continue
                if j2 in nc[j1]:
                    if j1[0] == 't' and j2[0] == 't':
                        sum = sum + 1/6
                    elif j1[0] == 't' or j2[0] == 't':
                        sum = sum + 1/4 
                    else:
                        sum = sum + 1/2

print(sum)

print(len(nc.keys()))
#for i in nc:
#    print(nc[i], len(nc[i]))

def all_conn(f):
    for i in f:
        for j in f:
            if i == j:
                continue
            if i not in nc[j]:
                return False
    return True

#print(all_conn(['co', 'de', 'ka', 'ta']))
for h in range(13):
    for i in nc:
        v = nc[i]
        for d in range(len(v)):
            m = [i]
            for dd in range(len(v)):
                if d != dd:
                    m.append(v[dd])
            if (all_conn(m)):
                print(','.join(sorted(m)))

