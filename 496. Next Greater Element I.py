# Using Stack Approach
# Time: O(n)
# Space: O(n)
# 2023.07.14: yes
# notes: 好处，按顺序的，坏处，难理解
# 通过倒序的方法，如果栈是空的，map到-1，把自己压进去，继续反着看倒数第二个元素，如果比栈顶大，把栈里比他小的都踢出来
# map栈顶，有就map，没有同上，把自己压进去，循环往复，每次都要压自己进栈
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        def greater(nums):
            n = len(nums)
            res = [0] * n
            s = []
            for i in range(n-1, -1, -1):
                while s and s[-1] <= nums[i]:
                    s.pop()
                res[i] = s[-1] if s else -1
                s.append(nums[i])
            return res
        next_nums2 = greater(nums2)
        hash_table = {}
        for i in range(len(nums2)):
            hash_table[nums2[i]] = next_nums2[i]
        next_nums1 = []
        for i in range(len(nums1)):
            next_nums1.append(hash_table[nums1[i]])
        return next_nums1

# Tests:
test = Solution()
test.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2])

# Using Stack
# Time: O(n)
# Space: O(n)
# 2023.07.14: yes
# notes: 遇到比自己大的就map然后退出当前节点，没遇到的话，就继续压下一个节点，遇到最大的点，就可以把最上面的都map了，如果遍历结束了，都
# 没有压出栈，就是map，-1作为结果，坏处是乱序的
class Solution2:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        map = {}
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                map[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        while stack:
            map[stack.pop()] = -1
        res = []
        for num in nums1:
            res.append(map.get(num))
        return res
