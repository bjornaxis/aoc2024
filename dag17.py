#!/usr/bin/python3
import copy

# test
A = 7294,2,
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

bb = [{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}]

done = 0
AA = 0x94e6d
AA = 0x94ebf



AA = 0x294e6d
AA = 0xa94e6d


AA = 0xfb70a94e6d

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
                if ind >= len(pr):
                    done2 = 1
                    ind = 0
                if ii%8 != pr[ind]:
                    done2 = 1
                    ind = 0
                else:
                    ind = ind+1
                    if ind > 10:
                        m = hex(AA)
                        bb[ind][m[-10:]] = 1
                        print(ind, m, bb)
                        #print(ind, len(pr), hex(AA))
            case 6: # bdv
                B = A >> ii
            case 7: # cdv
                C = A >> ii
                    
        pc += 2
    if ind == len(pr):
        done = 1
    #if AA % 1000000 == 0:
    #    print(AA)   
    if done:
        print(ind, len(pr), hex(AA))
        break
    #AA += 1
    AA += 0x10000000

