#!/usr/bin/env python

ans = 0
with open("input.txt") as file:
    for line in file:
        combinedBag = line.strip()
        bagSize = int(len(combinedBag)/2)
        lBag = combinedBag[0:bagSize]
        rBag = combinedBag[bagSize:len(combinedBag)]
        lDict = {} 
        
        for item in lBag:
            lDict[item] = True
        for item in rBag:
            if lDict.get(item) == True:
                if (item.islower()):
                    ans += ord(item) - ord('a') + 1
                else:
                    ans += ord(item) - ord('A') + 27
                break
print(ans)
