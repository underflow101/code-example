# kbt21_3
# 3. kakaoPeople

def solution(info, query):
    ans = []
    people = []
        
    for item in info:
        tmp = list(item.split())
        people.append(tmp)

    for q in query:
        cnt = 0
        tmp = list(q.split(' and '))
        tmpscore = tmp[-1].split()
        tmp.pop()
        tmp.append(tmpscore[0])
        tmp.append(tmpscore[1])

        for i in range(len(people)):
            for j in range(len(tmp)):
                if tmp[j] == '-':
                    continue
                elif tmp[j].isdigit():
                    if int(people[i][-1]) >= int(tmp[-1]):
                        cnt += 1
                    else:
                        break
                else:
                    if tmp[j] in people[i]:
                        continue
                    else:
                        break
        ans.append(cnt)
    return ans
            
    
info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))