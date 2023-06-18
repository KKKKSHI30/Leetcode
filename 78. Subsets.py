class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        chosen = []
        results = []
        self.recursion(nums, chosen, results)
        return results

    def recursion(self, nums, chosen, results):
        if not nums:
            results.append(chosen[:])
            return
        temp = nums.pop(0)
        chosen.append(temp)
        self.recursion(nums, chosen, results)
        chosen.pop()
        self.recursion(nums, chosen,results)
        nums.insert(0, temp)

test = Solution()
test.subsets(nums = [1,2,3])


class Solution2:
    def subsets(self, nums):
        def backtrack(first, curr):
            output.append(curr[:])
            for i in range(first, n):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()
        output = []
        n = len(nums)
        backtrack(0,[])
        return output
test = Solution2()
test.subsets(nums = [1,2,3])


class Solution3:
    #  Cascading, not recommended
    def subsets(self, nums):
        output = [[]]
        for num in nums:
            output += [curr + [num] for curr in output]
        return output

test = Solution3()
test.subsets(nums = [1,2,3])


class Solution4:
    def subsets(self, nums):
        n = len(nums)
        output = []
        for i in range(2 ** n, 2 ** (n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]
            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        return output

test = Solution4()
test.subsets(nums = [1,2,3])