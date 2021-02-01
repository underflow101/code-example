# BOJ 9342
# chromosome

import sys
#input = sys.stdin.readline

start = ['A', 'B', 'C', 'D', 'E', 'F']
nextone = ['A']
nexttwo = ['F']
nextthree = ['C']
last = ['A', 'B', 'C', 'D', 'E', 'F']
check = {'start':False,
         'nextone':False,
         'nexttwo':False,
         'nextthree':False,
         'last':False}

def check(s):
    cnt = 0
    # special case
    if len(s) > 2:
        if s[0] == 'A' and s[1] == 'F':
            for i in range(2, len(s)):
                if s[i] in nexttwo:
                    continue
                else:
                    if s[i] not in nextthree:
                        return False
                    else:
                        if i == len(s) - 1:
                            return True
                        else:
                            return False
                    

T = int(input())
for _ in range(T):
    word = input()
    if len(word) == 0:
        print("Good")
    else:
        