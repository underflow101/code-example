# BOJ 18258
# queue2

from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

q = deque()

T = int(input())
for _ in range(T):
    op = list(map(str, input().split()))
    
    if op[0] == 'push':
        op[1] = int(op[1])
        q.append(op[1])
    elif op[0] == 'pop':
        try:
            print(str(q.popleft()))
            print('\n')
        except:
            print('-1')
            print('\n')
    elif op[0] == 'size':
        print(str(len(q)))
        print('\n')
    elif op[0] == 'empty':
        if q:
            print('0')
            print('\n')
        else:
            print('1')
            print('\n')
    elif op[0] == 'front':
        try:
            print(str(q[0]))
            print('\n')
        except:
            print('-1')
            print('\n')
    elif op[0] == 'back':
        try:
            print(str(q[-1]))
            print('\n')
        except:
            print('-1')
            print('\n')