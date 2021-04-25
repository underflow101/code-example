# stringRearrange_2.py
# book p.322

import sys
input = sys.stdin.readline

string = list(input())
sum = 0
res = []

for item in string:
    if item.isdigit():
        sum += int(item)
    elif item.isalpha():
        res.append(item)

res.sort()
res = ''.join(res)
res += str(sum)

print(res)