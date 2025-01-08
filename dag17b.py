#!/usr/bin/python3
import copy

# test
A = 729
B =  0
C = 0

pr =[ 0,1,5,4,3,0 ]

#test2
A = 2024
B = 0
C = 0

pr = [ 0,3,5,4,3,0]

# Real
A = 33024962
B = 0
C = 0

pr = [ 2,4,1,3,7,5,1,5,0,3,4,2,5,5,3,0]

pc = 0
out = []

done = 0
AA = 0xc4fb70a94e6d
while not done:
    done2 = 0
    ind = 0
    pc = 0
    A=AA
    while not done2 and pc < len(pr):
        op = pr[pc]
        i = pr[pc+1]
        ii = 0
        match i:
            case 0:
                ii = i
            case 1:
                ii = i
            case 2:
                ii = i
            case 3:
                ii = i
            case 4:
                ii = A
            case 5:
                ii = B
            case 6:
                ii = C

        match op:
            case 0: # adv
                A = A >> ii
            case 1: # bxl
                B = B ^ i
            case 2: # bst
                B = ii % 8
            case 3: # jnz
                if A != 0:
                    pc = ii - 2
            case 4: # bxc
                B = B ^ C
            case 5: # out
                out.append(ii%8)
                #if ind >= len(pr):
                #    done2 = 1
                #    ind = 0
                #if ii%8 != pr[ind]:
                #    done2 = 1
                #ind += 1
            case 6: # bdv
                B = A >> ii
            case 7: # cdv
                C = A >> ii
                    
        pc += 2

    print(pr)
    print(out)
    print(hex(AA))
    break
    if ind == len(pr):
        done = 1
    if done:
        print(AA)
        break


