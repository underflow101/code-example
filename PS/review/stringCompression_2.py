# stringCompression_2.py
# book p.323

import sys
input = sys.stdin.readline

def solution(s):
    ans = 1e9
    length = len(s)
    tmp = []
    
    for i in range(1, length//2+1):
        res = ''
        cnt = 1
        print(i)
        for j in range(i, length, i):
            if s[j-i:j] == s[j:j+i]:
                cnt += 1
            else:
                if cnt > 1:
                    res += str(cnt)
                    res += s[j-i:j]
                    cnt = 1
                else:
                    res += s[j-i:j]
        res += str(cnt) + s[j-i:] if cnt > 1 else s[j-i:]
        ans = min(ans, len(res))
        print('=================')
    return ans

s = "aabbacccc"
print(solution(s))