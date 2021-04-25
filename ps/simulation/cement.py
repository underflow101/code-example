def fill(block):
    _tmp = [0] * len(block)
    flag = 0
    
    while True:
        for i in range(1, len(block)-1):
            if block[i] < block[i-1] and block[i] < block[i+1]:
                _tmp[i] += min(block[i-1], block[i+1]) - block[i]
                block[i] += _tmp[i]
            else:
                flag += 1
            print("_tmp: ", end='')
            print(_tmp)
        if flag > len(block) - 3:
            break
    return _tmp

def solution(day, width, blocks):
    ans = 0
    
    currBlocks = []
    for i in range(len(blocks[0])):
        currBlocks.append(blocks[0][i])
    tmp = fill(currBlocks)
    ans += (sum(tmp))
    print(tmp)
    
    for i in range(1, day):
        for j in range(len(blocks[i-1])):
            currBlocks[j] += (blocks[i-1][j])
        tmp = fill(currBlocks)
        ans += (sum(tmp))
        print(tmp)
    
    
    return ans