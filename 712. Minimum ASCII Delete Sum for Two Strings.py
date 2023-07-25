# Bottom-up Dynamic Programming
# Time: O(mn)
# Space: O(mn)
# 2023.07.25: yes
import copy
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m, n = len(s1), len(s2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 and j == 0:
                    dp[0][0] = 0
                elif i == 0:
                    dp[0][j] = dp[0][j-1] + ord(s2[j-1])
                elif j == 0:
                    dp[i][0] = dp[i-1][0] + ord(s1[i-1])
                elif s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i-1]), dp[i][j - 1] + ord(s2[j-1]))
        return dp[m][n]

# Top-down Dynamic Programming
# Time: O(mn)
# Space: O(mn)
# 2023.07.25: yes
class Solution2:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        # Dictionary to store the result of each sub-problem
        saved_result = {}

        # Return minimum cost to make s1[0...i] and s2[0...j] equal
        def compute_cost(i, j):

            # If both strings are empty, then no deletion is required
            if i < 0 and j < 0:
                return 0

            # If already computed, then return the result from the dictionary
            if (i, j) in saved_result:
                return saved_result[(i, j)]

            # If any one string is empty, delete all characters of the other string
            if i < 0:
                saved_result[(i, j)] = ord(s2[j]) + compute_cost(i, j - 1)
                return saved_result[(i, j)]
            if j < 0:
                saved_result[(i, j)] = ord(s1[i]) + compute_cost(i - 1, j)
                return saved_result[(i, j)]

            # Call sub-problem depending on s1[i] and s2[j]
            # Save the computed result.
            if s1[i] == s2[j]:
                saved_result[(i, j)] = compute_cost(i - 1, j - 1)
            else:
                saved_result[(i, j)] = min(
                    ord(s1[i]) + compute_cost(i - 1, j),
                    ord(s2[j]) + compute_cost(i, j - 1)
                )

            return saved_result[(i, j)]

        # Return the result of the main problem
        return compute_cost(len(s1) - 1, len(s2) - 1)


# Bottom-up Dynamic Programming
# Time: O(mn)
# Space: O(m)
# 2023.07.25: yes
# notes: 我自己的方法用了两行，上一行和本行，本质上也是保存左边，上面，左上三个点
class Solution4(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        if len(s1) < len(s2):
            return self.minimumDeleteSum(s1=s2, s2=s1)
        m, n = len(s1), len(s2)
        dp = [0 for _ in range(n+1)]
        temp = [0 for _ in range(n + 1)]
        for j in range(1, n+1):
            temp[j] = temp[j-1]+ ord(s2[j-1])
        for i in range(1, m+1):
            for j in range(n+1):
                if j == 0:
                    dp[0] = temp[0] + ord(s1[i-1])
                elif s1[i-1] == s2[j-1]:
                    dp[j] = temp[j-1]
                else:
                    dp[j] = min(temp[j] + ord(s1[i-1]), dp[j-1]+ord(s2[j-1]))
            temp = copy.deepcopy(dp)
        return dp[n]

# Space-Optimized Bottom-up Dynamic Programming
# Time: O(mn)
# Space: O(min(n,m))
# 2023.07.25: no
# notes: 这道题确实可以只用一行，但是要存储左上角的值，因为如果两个字符相同，不需要做任何变化，就需要左上角的值
# 左边的值就是更新过的左边的值，上行的值就是未更新的列，只有左上角的值需要单独用一个字符记录下来
class Solution5:
    def minimumDeleteSum(self, s1, s2):

        # Make sure s2 is smaller string
        if len(s1) < len(s2):
            return self.minimumDeleteSum(s1=s2, s2=s1)

        # Case for empty s1
        m, n = len(s1), len(s2)
        curr_row = [0] * (n + 1)
        for j in range(1, n + 1):
            curr_row[j] = curr_row[j - 1] + ord(s2[j - 1])

        # Compute answer row-by-row
        for i in range(1, m + 1):

            diag = curr_row[0]
            curr_row[0] += ord(s1[i - 1])

            for j in range(1, n + 1):

                # If characters are the same, the answer is top-left-diagonal value
                if s1[i - 1] == s2[j - 1]:
                    answer = diag

                # Otherwise, the answer is minimum of top and left values with
                # deleted character's ASCII value
                else:
                    answer = min(
                        ord(s1[i - 1]) + curr_row[j],
                        ord(s2[j - 1]) + curr_row[j - 1]
                    )

                # Before overwriting curr_row[j] with the answer, save it in diag
                # for the next column
                diag = curr_row[j]
                curr_row[j] = answer

        # Return answer
        return curr_row[-1]

# Tests:
test = Solution5()
test.minimumDeleteSum(s1 = "sea", s2 = "eat")
test.minimumDeleteSum(s1 = "delete", s2 = "leet")

