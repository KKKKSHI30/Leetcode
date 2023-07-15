# Sorting via Custom Comparator Approach
# Time: O(nlogn)
# Space: O(n)
# 2023.07.05: yes
# notes: 非常简洁的方法，比较string
class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num

# Tests:
test = Solution()
test.largestNumber([10,2])