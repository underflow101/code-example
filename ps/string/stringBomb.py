# BOJ 9935
# stringBomb

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def compressWord(word, bomb):
    ans = list()
    for i in range(0, len(word)):
        ans.append(word[i])
        j = len(ans)
        x = len(bomb)
        cnt = 0
        while j >= x:
            if ans[j-1] == bomb[x-1]:
                cnt += 1
                if cnt == len(bomb):
                    for _ in range(cnt):
                        ans.pop()
                    j = len(ans)
                    x = len(bomb)
                    continue
                j -= 1
                x -= 1
            else:
                break
    if len(ans) == 0:
        return 'FRULA'
    else:
        return ''.join(ans)
    
    
word = input().rstrip()
bomb = input().rstrip()
print(compressWord(word, bomb))