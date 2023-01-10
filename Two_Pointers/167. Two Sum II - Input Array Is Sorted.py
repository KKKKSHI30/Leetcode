class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        small, big = 0, len(numbers)-1
        while small < big:
            if numbers[small] + numbers[big] > target:
                big -= 1
            elif numbers[small] + numbers[big] < target:
                small += 1
            else:
                return [small+1,big+1]

test = Solution()
test.twoSum([2,7,11,15], 9)

