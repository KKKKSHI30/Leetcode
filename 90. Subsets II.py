# Backtracking
# Time: O(n2^n)
# Space: O(n)
# 2023.08.02: no
# notes: 子集情况都差不多，遇到这个情况入循环的时候直接加进去即可，但是加进去的时候，这里需要判断和前面一个元素重不重复
class Solution:
    def subsetsWithDup(self, nums):
        def backtrack(first, curr):
            output.append(curr[:])
            for i in range(first, n):
                if i > first and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()
        output = []
        n = len(nums)
        nums = sorted(nums)
        backtrack(0,[])
        return output


# Bitmasking
# Time: O(n2^n)
# Space: O(n)
# 2023.08.02: no
# notes: 和78的bitmask没什么区别，只是加了个seen，去保证不一样
class Solution2:
    def subsetsWithDup(self, nums):
        subsets = []
        n = len(nums)
        nums.sort()

        maxNumberOfSubsets = 1 << n
        seen = set()

        for subsetIndex in range(maxNumberOfSubsets):
            currentSubset = []
            hashcode = []
            for j in range(n):
                mask = 1 << j
                isSet = mask & subsetIndex
                if isSet != 0:
                    currentSubset.append(nums[j])
                    hashcode.append(str(nums[j]))

            # Generate the hashcode as a comma-separated string.
            hashcode = ",".join(hashcode)

            if hashcode not in seen:
                seen.add(hashcode)
                subsets.append(currentSubset)

        return subsets



# Bitmasking
# Time: O(n2^n)
# Space: O(logn)
# 2023.08.02: no
# notes: 标答写的很不错，如果该元素和前面一样，那就从上次开始的地方继续粘贴新元素，如果和前面元素不一样，就从头开始粘粘新元素
class Solution3:
    def subsetsWithDup(self, nums):
        nums.sort()
        subsets = [[]]
        subset_size = 0
        for i in range(len(nums)):
            starting_index = subset_size if i >= 1 and nums[i] == nums[i - 1] else 0
            # subset_size refers to the size of the subset in the previous step.
            # This value also indicates the starting index of the subsets generated in this step.
            subset_size = len(subsets)
            for j in range(starting_index, subset_size):
                current_subset = subsets[j][:]
                current_subset.append(nums[i])
                subsets.append(current_subset)

        return subsets


# Tests:
test = Solution2()
test.subsetsWithDup([1,2,2,3])
test.subsetsWithDup([4,4,4,1,4])