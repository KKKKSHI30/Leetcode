# Given an array arr containing n non-negative integers and an element x , in one operation, x can be added
# to or subtracted from any element of the array. MEX of an array is defined as the smallest non-negative integer
# which is not present in the array. For example, the MEX of [0, 1, 1, 3] is 2, and the MEX of [1, 2, 4] is 0.
# Find the maximum possible MEX of the array that can be achieved by doing the above operation any number of
# times.
# Example:
# arr = [0, 1, 2, 1, 3]
# x=3
# If we add x to arr[1] we get arr = [0, 4, 2, 1, 3] having MEX equal to 5.
# Function Description
# Complete the function getMaximumMex in the editor below. getMaximumMex has the following parameters
# int arr[n] : an array of n non-negative integers
# int x : an integer that can be added to or subtracted from any element of the array
# Returns
# int : the maximum possible MEX of arr
# notes: 又是一道题目比题难的题
# 把所有的nodes都mod一遍，然后计数mod的情况，从0开始遍历，看存不存在在hash map中，存在就减一，不存在就说明没这个值，直接返回

from collections import defaultdict
# Function to find maximum MEX of the array
# after doing some addition and subtraction
def mex(arr, n, K):
    # Create a map to store the frequency of
    # remainder of all element by K
    mp = defaultdict(lambda: 0)
    # Traverse the array
    for i in range(n):
        # Update frequency of arr[i]
        mp[arr[i] % K] += 1
    for i in range(n):
        # In order to generate i find an
        # element whose modulo value is equal
        # to i%K, return i as answer if no
        # such value is found
        if ((i % K) not in mp):
            return i
        # If we find element whose modulo
        # value equal to i%K
        mp[i % K] -= 1
        if (mp[i % K] == 0):
            del mp[i % K]
    return n

arr = [1,3,4]
N = len(arr)
K = 2
mex(arr, N, K)