# BOJ 1526
# keumminsoo

n = int(input())

def check(k):
    while k > 3:
        flag = False
        tmp = list(str(k))
        for i in range(len(tmp)):
            if tmp[i] != '4' and tmp[i] != '7':
                k -= 1
                flag = True
                break
        if flag:
            continue
        else:
            return k

print(check(n))