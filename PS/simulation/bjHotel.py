# BOJ 10250
# bjHotel

T = int(input())
for _ in range(T):
    h, w, n = map(int, input().split())
    res = ""
    cnt = 1
    while n > h:
        n -= h
        cnt += 1
    res += str(n)
    if cnt < 10:
        res += "0"
        res += str(cnt)
    else:
        res += str(cnt)
    print(res)