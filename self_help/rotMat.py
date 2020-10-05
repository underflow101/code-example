def rotMat(a):
    n = len(a)
    m = len(a[0])
    res = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            res[j][n-i-1] = a[i][j]
    return res