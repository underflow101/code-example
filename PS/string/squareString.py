# BOJ 4354
# squareString

import sys
input = sys.stdin.readline

def solution(s):
  res = 1

  for i in range(len(s)//2):
    if len(s) % (i+1) == 0:
      if not i:
        prev = s[0]
      else:
        prev = s[:i+1]

      if prev * (len(s)//(i+1)) == s:
        res = len(s)//(i+1)
        break
    else:
      continue

  return res

while True:
    s = input().rstrip()
    if s == '.':
        break
    else:
        print(solution(s))