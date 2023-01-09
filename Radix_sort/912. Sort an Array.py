class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0 or len(nums) == 1:
            return nums
        self.process(nums, 0, len(nums)-1)
        return nums

    def process(self, nums, left, right):
        if left != right:
            mid = (left + right)//2
            self.process(nums, left, mid)
            self.process(nums, mid+1, right)
            self.merge(nums, left, mid, right)
        return nums

    def merge(self, nums, left, mid, right):
        temp = []
        i, j = left, mid+1
        for k in range(right - left +1):
            if i == mid+1:
                temp.append(nums[j])
                j += 1
            elif j == right+1:
                temp.append(nums[i])
                i += 1
            elif nums[i] <= nums[j]:
                temp.append(nums[i])
                i +=1
            else:
                temp.append(nums[j])
                j +=1
        for k in range(len(temp)):
            nums[left] = temp[k]
            left += 1
        return nums

test = Solution()
test.sortArray([-2,3,-5])
test.sortArray([5,2,3,1])
test.sortArray(nums = [5,1,1,2,0,0])




