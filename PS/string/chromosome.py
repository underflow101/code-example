# BOJ 9342
# chromosome

start = ['A', 'B', 'C', 'D', 'E', 'F']
nextone = ['A']
nexttwo = ['F']
nextthree = ['C']
last = ['A', 'B', 'C', 'D', 'E', 'F']

def check(s):
    cnt = 0
    visited = [False] * 4
    # special case
    if len(s) < 3:
        return False
    elif len(s) == 3:
        if s[0] == 'A' and s[1] == 'F' and s[2] == 'C':
            return True
        else:
            return False
    elif len(s) == 4:
        if s[0] == 'A' and s[1] == 'F' and s[2] == 'C':
            if s[3] in last:
                return True
            else:
                return False
        elif s[0] in start and s[1] == 'A' and s[2] == 'F' and s[3] == 'C':
            return True
        else:
            return False
    else:
        i = 0
        if s[i] in start and not visited[0]:
            i += 1
            while True:
                if i >= len(s)-1:
                    return False
                if s[0] == 'A' and s[1] == 'F':
                    i += 1
                    visited[1] = True
                    break
                if s[i] in nextone and not visited[1]:
                    if s[i+1] in nextone:
                        i += 1
                        continue
                    else:
                        i += 1
                        visited[1] = True
                        break
                else:
                    return False
            while True:
                if i >= len(s)-1:
                    return False
                if s[i] in nexttwo and not visited[2]:
                    if s[i+1] in nexttwo:
                        i += 1
                        continue
                    else:
                        i += 1
                        visited[2] = True
                        break
                else:
                    return False
            while True:
                if i >= len(s)-1:
                    break
                if s[i] in nextthree and not visited[3]:
                    if s[i+1] in nextthree:
                        i += 1
                        continue
                    else:
                        i += 1
                        visited[3] = True
                        break
                else:
                    return False
            if i >= len(s):
                    return True
            else:
                if s[i] in last:
                    return True
                else:
                    return False
        else:
            return False

T = int(input())
for _ in range(T):
    word = input()
    if len(word) == 0:
        print("Good")
    else:
        if check(word):
            print("Infected!")
        else:
            print("Good")