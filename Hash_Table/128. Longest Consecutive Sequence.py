class Solution:
    # brute-force, but space complexity is O(1), similar sort as the Solution3
    def longestConsecutive(self, nums):
        longest_streak = 0

        for num in nums:
            current_num = num
            current_streak = 1

            while current_num + 1 in nums:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak

class Solution2:
    # sort methods, same as mine, but not permitted
    # time complexity O(nlogn)
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1

        return max(longest_streak, current_streak)

class Solution3:
    # best solution
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        # 虽然是double loop，但是每个element只检查一次
        for num in num_set:
            # check if the previous is in the set, otherwise, we will have a link in the futher, or linked before
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


nums = [100,4,200,1,3,2]
test = Solution3()
test.longestConsecutive(nums)