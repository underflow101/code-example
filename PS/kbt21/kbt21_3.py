# kbt21_3
# 3. kakaoPeople

def solution(info, query):
    ans = []
    hashtable = {}
        
    for item in info:
        j = 0
        tmp = list(item.split())
        for i in range(len(tmp)-1):
            hashtable[j][tmp[i]] = 1
        hashtable['score'].append(int(tmp[-1]))
        j += 1
    print(hashtable)
    
    for q in query:
        cnt = 0
        tmp = list(q.split(' and '))
        tmpscore = tmp[-1].split()
        tmp.pop()
        tmp.append(tmpscore[0])
        tmp.append(tmpscore[1])

        tmpans = list()
        for qitem in tmp:
            if qitem.isdigit():
                for score_item in hashtable['score']:
                    if score_item >= int(qitem):
                        cnt += 1
                tmpans.append(cnt)
            elif qitem == '-':
                continue
            else:
                tmpans.append(hashtable[qitem])
        ans.append(min(tmpans))
    return ans
    
info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))