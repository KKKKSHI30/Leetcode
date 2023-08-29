# A sorting based program to
# count pairs with difference k
def countPairsWithDiffK(arr, k):
    count = 0

    # Sort array elements
    arr.sort()

    l = 0
    r = 0
    n = len(arr)

    while r < n:
        if arr[r] - arr[l] == k:
            count += 1
            l += 1
            r += 1

        # arr[r] - arr[l] < sum
        elif arr[r] - arr[l] > k:
            l += 1
        else:
            r += 1
    return count


arr = [1, 5, 3, 4, 2]
k = 3
countPairsWithDiffK(arr, k)
countPairsWithDiffK([1,3,5],2)

