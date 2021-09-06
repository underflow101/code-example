# KAKAO INTERN 2021
# Number and Strings

def solution1(s):
    ans = 0
    res = ''
    tmp = ''

    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for item in s:
        if item.isdigit():
            res += item
        else:
            tmp += item
            if tmp in num:
                res += str(num.index(tmp))
                tmp = ''
                continue

    ans = int(res)
    return ans

def solution2(s):
    ans = 0
    res = ''
    tmp = ''

    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    while not s.isdigit():
        for i in range(10):
            if s.find(num[i]) != -1:
                s = s.replace(num[i], str(num.index(num[i])))
    
    return int(s)

assert solution1("one4seveneight") == 1478
assert solution1("23four5six7") == 234567
assert solution1("2three45sixseven") == 234567
assert solution1("123") == 123