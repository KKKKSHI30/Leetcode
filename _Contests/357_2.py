class Solution(object):
    def canSplitArray(self, A, m):
        return len(A) <= 2 or any(A[i] + A[i + 1] >= m for i in range(len(A) - 1))


class Solution2(object):
    def canSplitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: bool
        """
        def recursion(nums):
            if len(nums) == 1 or len(nums) == 2:
                return True
            for i in range(len(nums)-1):
                left_check, right_check = False, False
                left = nums[:i+1]
                right = nums[i+1:]
                if len(left) == 1:
                    left_check = True
                elif sum(left) >= m:
                    left_check = recursion(left)
                else:
                    continue
                if len(right) == 1:
                    right_check = True
                elif sum(right) >= m:
                    right_check = recursion(right)
                else:
                    continue
                if left_check and right_check:
                    return True
            return False
        return recursion(nums)

# Tests:
test = Solution()
test.canSplitArray([7, 6, 1, 6, 8, 3, 6, 2, 3, 11, 3, 7, 7, 3, 3, 2, 5, 9, 4, 4], 15)
test.canSplitArray([2, 3, 3, 2, 3], 6)
test.canSplitArray([2,1,3], 5)
test.canSplitArray([2, 2, 1], 4)



