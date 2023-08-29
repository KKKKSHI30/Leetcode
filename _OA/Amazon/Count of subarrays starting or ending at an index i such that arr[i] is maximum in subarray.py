# 题目: https://www.geeksforgeeks.org/count-of-subarrays-starting-or-ending-at-an-index-i-such-that-arri-is-maximum-in-subarray/
# notes: 思路，单调栈，找到previous largest element和next largest element
# 每个位置上拿index减一下就可
def countSubarrays(arr):
    next_larger_element = []
    temp = []
    for i in range(len(arr) - 1, -1, -1):
        while temp and arr[i] > arr[temp[-1]]:
            temp.pop()
        if len(temp) == 0:
            next_larger_element.append(len(arr))
        else:
            next_larger_element.append(temp[-1])
        temp.append(i)
    next_larger_element.reverse()

    previous_larger_element = []
    temp = []
    for i in range(len(arr)):
        while temp and arr[i] > arr[temp[-1]]:
            temp.pop()
        if len(temp) == 0:
            previous_larger_element.append(-1)
        else:
            previous_larger_element.append(temp[-1])
        temp.append(i)

    result = []
    for i in range(len(arr)):
        result.append(next_larger_element[i] - previous_larger_element[i]-1)
    print(result)


arr = [3, 4, 1, 6, 2]
countSubarrays(arr)

# 2   -> temp空  压2  存5
# 6   ->  6 > 2  2 pop 压6   存5
# 1   ->  1 < 6   压1   存6的位置

