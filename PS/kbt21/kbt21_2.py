# kbt21_2
# 2. course menu

from itertools import combinations

def check(a, b):
    cnt = 0
    for i in range(len(a)):
        cnt = 0
        for j in range(len(b)):
            if a[i] != b[j]:
                continue
            else:
                cnt +=1
                break
        if cnt < 1:
            return False
    return True
        
def solution(orders, course):
    ans = []
    res = []
    tmp = []
    comb = []
    realcomb = []
    tmporder = []
    
    cnt = 0
    
    for item in orders:
        realtmp = list(item)
        realtmp.sort()
        tmporder.append(''.join(realtmp))
    orders = tmporder
    
    for item in orders:
        for i in course:
            comb.append(list(combinations(item, i)))

    for num in comb:
        for tmptmp in num:
            item = ''.join(tmptmp)
            cnt = 0
            for i in range(len(orders)):
                if check(item, orders[i]):
                    cnt += 1
            if cnt > 1:
                if (cnt, item) not in res:
                    res.append((cnt, item))
            
    res.sort(key=lambda x: (len(x[1]), -x[0]))
    ans.append(res[0][1])

    for i in course:
        for j in range(1, len(res)):
            if len(res[j][1]) != i:
                continue
            else:
                if len(res[j-1][1]) == len(res[j][1]) and res[j-1][0] > res[j][0]:
                    break
                elif len(res[j-1][1]) != len(res[j][1]):
                    ans.append(res[j][1])
                elif len(res[j-1][1]) == len(res[j][1]) and res[j-1][0] == res[j][0]:
                    ans.append(res[j][1])
                    
    ans.sort()
    return ans
                
                
                
order = ["XYZ", "XWY", "WXA"]
course = [2,3,4]

print(solution(order, course))