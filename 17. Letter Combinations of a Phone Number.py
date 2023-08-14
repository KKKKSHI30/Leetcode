# Backtrack
# Time: O(4^N*N)
# Space: O(n)
# 2023.08.03: yes
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        def backtrack(index, cur):
            if len(cur) == len(digits):
                results.append("".join(cur))
                return
            possible_letters = letters[digits[index]]
            for i in possible_letters:
                cur.append(i)
                backtrack(index+1, cur)
                cur.pop()
        results = []
        backtrack(0, [])
        return results

# Tests:
test = Solution()
test.letterCombinations(digits = "23")