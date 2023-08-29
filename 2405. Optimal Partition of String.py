# Greedy
# Time: O(n)
# Space: O(1)
# 2023.08.17: yes
class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        saving = []
        res = 0
        for i in s:
            if i not in saving:
                saving.append(i)
            else:
                res += 1
                saving = [i]
        return res+1

# Tests:
test = Solution()
test.partitionString("abacaba")
test.partitionString("ssssss")