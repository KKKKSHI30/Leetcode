# Math
# Time: O(n)
# Space: O(1)
# 2023.08.18: no
# notes: 很难表明，两个条件，一个循环之后要不返回原点，要不不朝北，之后就可以返回原点
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        x = y = 0
        idx = 0
        for i in instructions:
            if i == "L":
                idx = (idx + 3) % 4
            elif i == "R":
                idx = (idx + 1) % 4
            else:
                x += directions[idx][0]
                y += directions[idx][1]
        return (x == 0 and y == 0) or idx != 0

# Test:
test = Solution()
test.isRobotBounded("GGGLGLGLGG")
test.isRobotBounded("G")
test.isRobotBounded("L")
test.isRobotBounded("RGRG")
