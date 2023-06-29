# Merge sort Approach
# Time: O(nlogn)
# Space: O(n)
# 2023.06.28: no
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def merge(nums, left, mid, right):
            temp = []
            start_left, start_right = left, mid+1
            end_left, end_right = mid, right
            while start_left <= end_left and start_right <= end_right:
                if nums[start_left] <= nums[start_right]:
                    temp.append(nums[start_left])
                    start_left += 1
                else:
                    temp.append(nums[start_right])
                    start_right += 1
            while start_left <= end_left:
                temp.append(nums[start_left])
                start_left += 1
            while start_right <= end_right:
                temp.append(nums[start_right])
                start_right += 1
            nums[left:right+1] = temp[:]


        def process(nums, left, right):
            if left < right:
                mid = (left + right) //2
                process(nums, left, mid)
                process(nums, mid+1, right)
                merge(nums, left, mid, right)
            return nums

        if len(nums) == 1 or len(nums) == 1:
            return nums
        return process(nums, 0, len(nums)-1)

# Heap sort Approach
# Time: O(nlogn)
# Space: O(n)
# 2023.06.28: no
# notes: 直接看notes太多了
class Solution2(object):
    def sortArray(self, nums):
				# heapify，把当前节点插入到大根堆里并且在正确的位置（从index开始做heapify）
        def heapify(nums, index, heapSize):
            left = index * 2 + 1  # 确认index的左树
            while left < heapSize:  # 如果左树的值是在树内
                if (left + 1 < heapSize) and (nums[left + 1] > nums[left]):  # 如果右树也在树内，且右树大于左树
                    largest = left + 1  # 大的是右树
                else:
                    largest = left  # 否则大的是左树
                if nums[largest] < nums[index]:  # 比较当前节点和大子树，谁值大，谁是largest
                    largest = index
                if largest == index:  # 父节点已经是最大的，停止向下移动
                    break
                nums[largest], nums[index] = nums[index], nums[largest]  # 父节点不是最大的，交换
                index = largest   # 当前节点成为大子树的节点
                left = index * 2 + 1   # 找当当前树的左子树，重复判断
            return nums

        if (len(nums) == 0) or (len(nums) == 1):
            return nums
        else:
            heapSize = len(nums)
            i = heapSize - 1
            while i >= 0:   # 从右往左确认大根堆的顺序， 时间复杂度为O(1)
                heapify(nums, i, heapSize)
                i -= 1

        heapSize = len(nums)
        nums[0], nums[heapSize - 1] = nums[heapSize - 1], nums[0]   # 把当前top拿出来，放到最后面成为已经排序的
        heapSize -= 1
        while heapSize > 0:
            heapify(nums, 0, heapSize)  # 对刚换上来的值进行heapify
            nums[0], nums[heapSize - 1] = nums[heapSize - 1], nums[0]  # 重复上面的过程
            heapSize -= 1    # size减一，证明最后一个已经排好了
        return nums


# Count sort Approach
# Time: O(n+k)
# Space: O(n)
# 2023.06.28: no
# notes: 找出最大最小边界，然后沿着最小开始往最大一个个找
class Solution3:
    def sortArray(self, nums):
        def counting_sort():
            # Create the counting hash map.
            counts = {}
            # Find the minimum and maximum values in the array.
            minVal, maxVal = min(nums), max(nums)
            # Update element's count in the hash map.
            for val in nums:
                counts[val] = counts.get(val, 0) + 1

            index = 0
            # Place each element in its correct position in the array.
            for val in range(minVal, maxVal + 1, 1):
                # Append all 'val's together if they exist.
                while counts.get(val, 0) > 0:
                    nums[index] = val
                    index += 1
                    counts[val] -= 1

        counting_sort()
        return nums


# Radix sort Approach
# Time: O(d(n+b))
# Space: O(n+b)
# 2023.06.28: no
# notes: 写起来有点麻烦，但是很容易理解
class Solution4:
    # Radix sort function.
    def radix_sort(self, nums):
        # Find the absolute maximum element to find max number of digits.
        max_element = nums[0]
        for val in nums:
            max_element = max(abs(val), max_element)

        max_digits = 0
        while max_element > 0:
            max_digits += 1
            max_element = max_element // 10

        place_value = 1

        # Bucket sort function for each place value digit.
        def bucket_sort():
            buckets = [[] for i in range(10)]
            # Store the respective number based on it's digit.
            for val in nums:
                digit = abs(val) / place_value
                digit = int(digit % 10)
                buckets[digit].append(val)

            # Overwrite 'nums' in sorted order of current place digits.
            index = 0
            for digit in range(10):
                for val in buckets[digit]:
                    nums[index] = val
                    index += 1

        # Radix sort, least significant digit place to most significant.
        for _ in range(max_digits):
            bucket_sort()
            place_value *= 10

        # Seperate out negatives and reverse them.
        positives = [val for val in nums if val >= 0]
        negatives = [val for val in nums if val < 0]
        negatives.reverse()

        # Final 'arr' will be 'negative' elements, then 'positive' elements.
        return negatives + positives

    def sortArray(self, nums):
        return self.radix_sort(nums)


    # Tests:
test = Solution4()
test.sortArray([5,2,3,1])
test.sortArray([-2,3,-5])
test.sortArray(nums = [5,1,1,2,0,0])







