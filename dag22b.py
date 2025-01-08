sum = 0
al = []
a4 =[]

a66 = {}
ggg = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u']

for h1 in range(-9,10):
    for h2 in range(-9,10): 
        for h3 in range(-9,10):
            for h4 in range(-9,10):
                sf = ggg[h1+9] +ggg[h2+9] +ggg[h3+9] +ggg[h4+9]
                a66[sf] = []

with open("d:\projekt\\aoc2024\d22_real.txt") as file:
#with open("d:\projekt\\aoc2024\d22_test2.txt") as file:
    for line in file:
        snum = int(line)
        
        a2 = []
        ttt = {}
        for j in range(2000):
            old_s = snum
            snum2 = snum * 64
            snum = snum ^ snum2
            snum = snum % 16777216

            snum2 = snum >> 5
            snum = snum ^ snum2
            snum = snum % 16777216

            snum2 = snum * 2048
            snum = snum ^ snum2
            snum = snum % 16777216

            fd = (snum%10) - (old_s%10)
            a2.append([snum%10, fd])
            if j > 2:
                sf = ggg[a2[j-3][1]+9] +ggg[a2[j-2][1]+9] +ggg[a2[j-1][1]+9] +ggg[a2[j][1]+9]
                if sf not in ttt:
                    ttt[sf] = a2[j][0]
        al.append(a2)
        print(len(ttt))
        for t in ttt:
            if t==0:
                print("h: ", t, ttt[t])
            a66[t].append(ttt[t])
        sum = sum+snum

print("sum: ", sum)

max_b = 0
i = 0
for r in a66:
    a = a66[r]
    ss = 0
    for b in a:
        ss = ss+b
    if ss > max_b:
        print(i,a)
        max_b = ss
    i = i+1
print("ban: ", max_b)
