#!/usr/bin/env python

points = {"X": 1, "Y": 2, "Z": 3}
# "X": 1, "Y": 2, "Z": 3
matrix = [[3,6,0], [0,3,6], [6,0,3]]

ans = 0
# def calc(oppo, me):
#     if (oppo == "A" and me == "X") or (oppo == "B" and me == "Y") or (oppo == "C" and me == "Z"):
#         return 3
#     if (me == "X" and oppo == "C") or (me == "Y" and oppo == "A") or (me == "Z" and oppo == "A"):
#         return 6
#     return 0

# with open("input.txt") as file:
#     for line in file:
#         split = line.rstrip().split(" ")
#         oppo = split[0]
#         me = split[1]
#         # ans += calc(oppo, me)
#         ans += matrix[ord(oppo)-ord("A")][ord(me)-ord("X")]
#         ans += points.get(me)

# print(ans)
winPoints = {"X": 0, "Y": 3, "Z": 6}
matrix2 = [["Z","X","Y"],["X","Y","Z"],["Y","Z","X"]]
with open("input.txt") as file:
    for line in file:
        split = line.rstrip().split(" ")
        oppo = split[0]
        me = split[1]
        ans += winPoints.get(me)
        ans += points.get(matrix2[ord(oppo)-ord("A")][ord(me)-ord("X")])
print (ans)
# X lose
# Y Draw
# Z Win

