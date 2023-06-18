class Solution:
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        diff = [0] * (length + 2)
        ori = [0] * (length + 2)
        for update in updates:
            diff[update[0]] += update[2]
            diff[update[1] + 1] -= update[2]

        for i in range(length + 1):
            ori[i] = ori[i - 1] + diff[i]
        ori.pop()
        ori.pop()
        return ori


test = Solution()
test.getModifiedArray(5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]])
test.getModifiedArray(10, [[2, 4, 6], [5, 6, 8], [1, 9, -4]])


class Solution2:
    # same solution but easier
    def getModifiedArray(self, length, updates):
        res = [0] * (length + 1)
        for s, e, c in updates:
            res[s] += c
            res[e + 1] += -c
        for i in range(1, len(res)):
            res[i] += res[i - 1]
        return res[:-1]
