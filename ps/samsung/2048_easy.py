# 2048_easy.py
# boj 12100

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

n = int(input())
maze = [list(input().split()) for _ in range(n)]

def 