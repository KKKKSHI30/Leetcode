def indicator1(arr, N):
    num, pre, cur = 0, 0, 0
    while pre < N and cur < N:
        if arr[pre] == arr[cur]:
            cur += 1
        else:
            if arr[pre] == cur-pre:
                num += 1
            pre = cur
    if arr[pre] == cur-pre:
        num += 1
    return num

def indicator2(arr, N):
    num, pre, cur = 0, 0, 0
    while pre < N and cur < N:
        if arr[pre] == arr[cur]:
            cur += 1
        else:
            if arr[pre] == cur-pre and 2*pre+1 == cur:
                num += 1
            pre = cur
    if arr[pre] == cur - pre and 2*pre+1 == cur:
        num += 1
    return num

def getIndicator(arr, N):
    return indicator1(arr, N) - indicator2(arr, N)

arr = [3,3,2,2,5,5,5,5,5,3,3,3,2,2]
arr2 = [1, 2, 2, 3, 3, 6, 6]
N = len(arr)
indicator2(arr, N)