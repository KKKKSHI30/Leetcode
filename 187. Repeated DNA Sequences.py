# Rabin-Karp Approach
# Time: O(n)
# Space: O(n-l)
# 2023.06.20: yes
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        # 先把字符串转化成四进制的数字数组
        nums = [0] * len(s)
        for i in range(len(nums)):
            if s[i] == 'A':
                nums[i] = 0
            elif s[i] == 'G':
                nums[i] = 1
            elif s[i] == 'C':
                nums[i] = 2
            elif s[i] == 'T':
                nums[i] = 3

        # 记录重复出现的哈希值
        seen = set()
        # 记录重复出现的字符串结果
        res = set()

        # 数字位数
        L = 10
        # 进制
        R = 4
        # 存储 R^(L - 1) 的结果
        RL = R ** (L - 1)
        # 维护滑动窗口中字符串的哈希值
        windowHash = 0

        # 滑动窗口代码框架，时间 O(N)
        left, right = 0, 0
        while right < len(nums):
            # 扩大窗口，移入字符，并维护窗口哈希值（在最低位添加数字）
            windowHash = R * windowHash + nums[right]
            right += 1

            # 当子串的长度达到要求
            if right - left == L:
                # 根据哈希值判断是否曾经出现过相同的子串
                if windowHash in seen:
                    # 当前窗口中的子串是重复出现的
                    res.add(s[left:right])
                else:
                    # 当前窗口中的子串之前没有出现过，记下来
                    seen.add(windowHash)
                # 缩小窗口，移出字符，并维护窗口哈希值（删除最高位数字）
                windowHash -= nums[left] * RL
                left += 1
        # 转化成题目要求的 List 类型
        return list(res)


# Linear-time Slice Using Substring + HashSet Approach (brute force)
# Time: O(n)
# Space: O((n-l)*l)
# 2023.06.20: yes
class Solution2:
    def findRepeatedDnaSequences(self, s):
        L, n = 10, len(s)
        seen, output = set(), set()

        # iterate over all sequences of length L
        for start in range(n - L + 1):
            tmp = s[start:start + L]
            if tmp in seen:
                output.add(tmp[:])
            seen.add(tmp)
        return output

# Bit Manipulation
# Time: O(n-l)
# Space: O((n-l)*l)
# 2023.06.20: no
# notes: 完全不懂，但是核心思路和rabin karp差不多
class Solution3:
    def findRepeatedDnaSequences(self, s):
        L, n = 10, len(s)
        if n <= L:
            return []

        # convert string to the array of 2-bits integers:
        # 00_2, 01_2, 10_2 or 11_2
        to_int = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        nums = [to_int.get(s[i]) for i in range(n)]

        bitmask = 0
        seen, output = set(), set()
        # iterate over all sequences of length L
        for start in range(n - L + 1):
            # compute bitmask of the sequence in O(1) time
            if start != 0:
                # left shift to free the last 2 bit
                bitmask <<= 2
                # add a new 2-bits number in the last two bits
                bitmask |= nums[start + L - 1]
                # unset first two bits: 2L-bit and (2L + 1)-bit
                bitmask &= ~(3 << 2 * L)
            # compute bitmask of the first sequence in O(L) time
            else:
                for i in range(L):
                    bitmask <<= 2
                    bitmask |= nums[i]
            if bitmask in seen:
                output.add(s[start:start + L])
            seen.add(bitmask)
        return output