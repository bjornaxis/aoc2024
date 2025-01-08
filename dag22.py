sum = 0
al = []
a4 =[]
with open("d:\projekt\\aoc2024\d22_real.txt") as file:
#with open("d:\projekt\\aoc2024\d22_test2.txt") as file:
    for line in file:
        snum = int(line)
        
        a2 = []
        a4b = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],]
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
            if j < 2000-3:
                a4b[fd+9].append(j)
        al.append(a2)
        a4.append(a4b)
        sum = sum+snum

print("sum: ", sum)



