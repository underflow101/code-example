# kbt21_1
# 1. kakao_id

def solution(new_id):
    ans = ''
    stack = []
    
    # Level 1
    new_id = new_id.lower()
    
    # Level 2
    for i in range(len(new_id)):
        if new_id[i].isalpha() or new_id[i].isdigit() or new_id[i] == '_' or new_id[i] == '-' or new_id[i] == '.':
            ans += new_id[i]
        else:
            continue
    
    # Level 3
    if len(ans) != 0:
        stack.append(ans[0])
        for i in range(1, len(ans)):
            if ans[i-1] == '.' and ans[i] == '.':
                continue
            else:
                stack.append(ans[i])
        ans = ''.join(stack)
    
    # Level 4
    ans = ans.strip('.')
    
    # Level 5
    if len(ans) == 0:
        ans += 'a'
    
    # Level 6
    if len(ans) > 15:
        ans = ans[:15]
        ans = ans.strip('.')

    # Level 7
    if len(ans) < 3:
        for _ in range(3-len(ans)):
            ans += ans[-1]

    return ans

print(solution(""))