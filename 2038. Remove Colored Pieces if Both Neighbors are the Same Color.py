# Loop Approach
# Time: O(n)
# Space: O(n)
# 2023.07.18: yes
# No specific
class Solution(object):
    def winnerOfGame(self, colors):
        a, b = 0, 0
        a_chances, b_chances = 0, 0
        if colors[0] == "A":
            a += 1
        else:
            b += 1
        for i in range(1, len(colors)):
            if colors[i] == "A":
                if colors[i] == colors[i-1]:
                    a += 1
                else:
                    if b > 2:
                        b_chances += (b-2)
                    a, b = 1, 0
            if colors[i] == "B":
                if colors[i] == colors[i-1]:
                    b += 1
                else:
                    if a > 2:
                        a_chances += (a-2)
                    a, b = 0, 1
        if a > 2:
            a_chances += a-2
        if b > 2:
            b_chances += b - 2

        if a_chances <= b_chances:
            return False
        else:
            return True

# Tests:
test = Solution()
test.winnerOfGame("AAAABBBB")
test.winnerOfGame("BBAAABBABBABB")
