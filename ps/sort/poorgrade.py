# poorgrade.py
# book p.180

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = list()
for i in range(n):
    input_data = input().split()
    arr.append((input_data[0], int(input_data[1])))

arr.sort(key=lambda student: student[1])

for student in arr:
    print(student[0], end=' ')