def counterClockspiralPrint(arr):
    k = 0
    l = 0
    cnt = 0
    m = len(arr)
    n = len(arr[0])
    total = m * n
    new_array = []
    while (k < m and l < n):
        if (cnt == total):
            break
        for i in range(k, m):
            new_array.append(arr[i][l])
            cnt += 1
        l += 1
        if (cnt == total):
            break
        for i in range(l, n):
            new_array.append(arr[m - 1][i])
            cnt += 1
        m -= 1
        if (cnt == total):
            break
        if (k < m):
            for i in range(m - 1, k - 1, -1):
                new_array.append(arr[i][n - 1])
                cnt += 1
            n -= 1
        if (cnt == total):
            break
        if (l < n):
            for i in range(n - 1, l - 1, -1):
                new_array.append(arr[k][i])
                cnt += 1

            k += 1
    if total %2 == 0:
        return new_array[-2]
    else:
        return new_array[-1]


# Driver Code
arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]  # 11
arr2 = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12]]   # 6
arr3 = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16],
        [17,18,19,20]]   # 11


counterClockspiralPrint(arr2)
