#!/usr/bin/env python

ans = 0;
cur = 0;
with open("input.txt") as file:
    for line in file:
        if line.rstrip() == "":
            cur = 0
            continue
        cur += int(line.rstrip())
        ans = max(cur, ans)
        
    print(ans)