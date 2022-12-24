#!/usr/bin/env python

ans = 0
count = 0
cur = 0
bagDict = {}
tmpBagDict = {}

with open("input.txt") as file:
    for line in file:
        if count == 3:
            count = 0
            cur = 0
            bagDict = {}
            # print(count)

        tmpBagDict = {}
        bag = line.strip()
        # print(bag)
        
        if count == 0:
            for item in bag:
                bagDict[item] = True
        else:
            for item in bag:
                if bagDict.get(item) == True:
                    tmpBagDict[item] = True
            bagDict = tmpBagDict

        # print(bagDict)
        # print(tmpBagDict)
        if (count == 2) :
            for item in bagDict:
                if (item.islower()):
                    ans += ord(item) - ord('a') + 1
                else:
                    ans += ord(item) - ord('A') + 27
        count += 1
        
print(ans)
