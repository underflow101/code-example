# stringCompression_2.py
# book p.323

import sys
input = sys.stdin.readline

def solution(s):
    ans = len(s)
    length = len(s)
    
    for i in range(1, length//2+1):
        res = ''
        prev = s[:i]
        cnt = 1
        for j in range(i, length, i):
            if prev == s[j:j+i]:
                cnt += 1
            else:
                res += str(cnt) + prev if cnt > 1 else prev
                cnt = 1
                prev = s[j:j+i]
        res += str(cnt) + prev if cnt > 1 else prev
        ans = min(ans, len(res))
    
    return ans

s = ""
print(solution(s))