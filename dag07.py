sum = 0

def testop(v, vv, b, op):
    if op == '*':
        vv = vv * b[0]
    if op == '+':
        vv = vv + b[0]
    if op == '||':
        vv = int(str(vv) + str(b[0]))
    if len(b) > 1:
        if testop(v,vv,b[1:], '*'):
            return True
        if testop(v,vv,b[1:], '+'):
            return True
        if testop(v,vv,b[1:], '||'):
            return True
    else:
        if v == vv:
            return True
        return False
    
#with open("d:\projekt\\aoc2024\d07_test.txt") as file:
with open("d:\projekt\\aoc2024\d07_real.txt") as file:
    for line in file:
        a = line.split(': ')
        b = a[1].split(' ')
        ss = int(a[0])
        k = []
        for i in b:
            k.append(int(i))
        #print(ss,k)
        if testop(ss,k[0],k[1:],'*') or testop(ss,k[0],k[1:],'+') or testop(ss,k[0],k[1:],'||'):
            #print('ok')
            sum = sum + ss

print(sum)
        
