# 题目: https://www.1point3acres.com/bbs/thread-1010642-1-1.html
def max_length(a, k):
    n = len(a)
    max_length = 0
    curr_sum = 0
    start = 0

    for end in range(n):
        curr_sum += a[end]

        while curr_sum > k:
            curr_sum -= a[start]
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length

# Example usage
a = [1, 2, 3, 4, 5]
k = 9
result = max_length(a, k)
print(result)


class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_window = 0
        cur_window_length = 0
        cur_element = []
        cur_sum = 0
        for i in nums:
            cur_sum += i
            cur_element.append(i)
            cur_window_length += 1
            while cur_sum > k:
                temp = cur_element.pop(0)
                cur_sum -= temp
                cur_window_length -= 1
            max_window = max(max_window, cur_window_length)
        return max_window

# Tests:
test = Solution()
test.maxSubArrayLen([1,-1,5,-2,3], 3)
test.maxSubArrayLen([1, 2, 3, 4, 5], 9)
test.maxSubArrayLen([-2,-1,2,1],1)


















