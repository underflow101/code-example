# lunchtime_2.py
# Samsung SW Expert Academy
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5-BEE6AK0DFAVl

def Calculation(stair_list, stair):
    count, d_count = 0, 0
    delete_queue = []
    while stair_list or delete_queue or d_count:
        while d_count:
            if len(delete_queue) == 3:
                break
            delete_queue.append(stair[2])
            d_count -= 1
 
        for i in range(len(delete_queue)-1, -1, -1):
            delete_queue[i] -= 1
            if delete_queue[i] <= 0:
                delete_queue.pop(i)
        
        for i in range(len(stair_list)-1, -1, -1):
            stair_list[i] -= 1
            if stair_list[i] <= 0:
                stair_list.pop(i)
                d_count += 1
        count+=1
    return count

def dfs(idx):
    if idx == Num:
        global min_count
        stair_list1, stair_list2 = [], []
        for i in range(Num):
            if check[i]:
                stair_list1.append(Peoples[i][0])
            else:
                stair_list2.append(Peoples[i][1])
        count = max(Calculation(sorted(stair_list1), Stairs[0]), Calculation(sorted(stair_list2), Stairs[1]))
        min_count = min(count, min_count)
        return
    check[idx] = False
    dfs(idx+1)
    check[idx] = True
    dfs(idx+1)
    
 
T = int(input())
for t in range(1, T+1):
    N = int(input())
    map_list = [list(map(int, input().split())) for _ in range(N)]
    Peoples, Stairs = [], []
    Num, min_count = 0, 987654321
    for i in range(N):
        for j in range(N):
            temp_num = map_list[i][j]
            if temp_num:
                if temp_num == 1:
                    Num += 1
                    Peoples.append([i, j])
                else:
                    Stairs.append([i, j, temp_num])
    for i in range(len(Peoples)):
        distance1 = abs(Peoples[i][0] - Stairs[0][0]) + abs(Peoples[i][1] - Stairs[0][1])
        distance2 = abs(Peoples[i][0] - Stairs[1][0]) + abs(Peoples[i][1] - Stairs[1][1])
        Peoples[i][0] = distance1
        Peoples[i][1] = distance2
    check = [False for _ in range(Num)]
    dfs(0)
    print('#{} {}'.format(t, min_count+1))