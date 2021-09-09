# KAKAO BLIND 2021
# New ID Recommendations

from collections import deque

def solution(new_id):
    ans = ''

    # step 1
    ans = new_id.lower()

    # step 2
    check_special_char = ['-', '_']
    tmp = ''
    if ans[0] in check_special_char or ans[0].isalnum():
        tmp += ans[0]
    for i in range(1, len(ans)):
        if ans[i].isalnum():
            tmp += ans[i]
        elif ans[i] in check_special_char:
            tmp += ans[i]
        elif ans[i] == '.':
            tmp += ans[i]
        else:
            continue
    
    # step 3
    while True:
        if tmp.find('..') != -1:
            tmp = tmp.replace('..', '.')
        else:
            break

    # step 4
    ans = tmp
    while True:
        if len(ans) == 0:
            break
        if ans[-1] == '.':
            ans = ans[:-1]
            continue
        elif ans[0] == '.':
            ans = ans[1:]
            continue
        break
    
    # step 5
    if len(ans) == 0:
        ans += 'a'
    
    # step 6
    if len(ans) > 15:
        ans = ans[:15]
    while ans[-1] == '.':
        ans = ans[:-1]
    
    # step 7
    if len(ans) < 3:
        while len(ans) < 3:
            ans += ans[-1]
    
    return ans

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
print(solution("./././././abcd/././././."))
print(solution("-_.~!@#$%^&*()=+[{]}:?,<>/._-"))