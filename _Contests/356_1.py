# Array
# Time: O(n)
# Space: O(1)
# 2023.07.29: yes
class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        res = 0
        for i in hours:
            if i >= target:
                res += 1
        return res

# Tests:
test = Solution()
test.numberOfEmployeesWhoMetTarget( hours = [0,1,2,3,4], target = 2)
test.numberOfEmployeesWhoMetTarget(hours = [5,1,4,2,2], target = 6)