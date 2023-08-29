class Solution:
    def canMakeSubsequence(self, str1, str2):
        def change_plus(s):
            if ord(s) == 122:
                return "a"
            else:
                return chr(ord(s)+1)
        if len(str1) < len(str2):
            return False
        hash_table = {}
        for i in range(97, 123):
            hash_table[chr(i)] = [change_plus(chr(i)), chr(i)]
        for i in range(len(str2)):
            for j in range(i, len(str1)):
                if str2[i] in hash_table[str1[j]]:
                    break
                if j == len(str1)-1:
                    return False
        return True

# Tests:
test = Solution()
test.canMakeSubsequence("","a")
test.canMakeSubsequence("c", "b") # F
test.canMakeSubsequence(str1 = "ab", str2 = "d") # F
test.canMakeSubsequence(str1 = "zc", str2 = "ad") # T
test.canMakeSubsequence(str1 = "abc", str2 = "ad") # T

