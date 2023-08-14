# Subarray is a contiguous block of an array's elements. Given an array of integers,
# find the sum of all elements of all subarrays of that array.
def SubArraySum(arr, n):
    temp, result = 0, 0
    # Pick starting point
    for i in range(0, n):
        # Pick ending point
        temp = 0
        for j in range(i, n):
            # sum subarray between
            # current starting and
            # ending points
            temp += arr[j]
            result += temp
    return result

# Driver code
arr = [1, 2, 3]
n = len(arr)
print("Sum of SubArray :", SubArraySum(arr, n))

# explaination:
# i)  In subarrays beginning with arr[i]. There are
#     (n-i) such subsets. For example [2] appears
#     in [2] and [2, 3].

# ii) In (n-i)*i subarrays where this element is not
#     first element. For example [2] appears in [1, 2] and [1, 2, 3].
#
# Total of above (i) and (ii) = (n-i) + (n-i)*i  = (n-i)(i+1)
def SubArraySum2(arr, n): # best approach
    result = 0

    # computing sum of subarray
    # using formula
    for i in range(0, n):
        result += (arr[i] * (i + 1) * (n - i))

    # return all subarray sum
    return result


# Driver code
arr = [2,3,4]
n = len(arr)
print("Sum of SubArray : ",
      SubArraySum2(arr, n))