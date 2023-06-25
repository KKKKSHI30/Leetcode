# Left and Right product lists Approach
# Time: O(n)
# Space: O(n)
# 2023.06.23: yes
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_product = [1]
        right_product = [1]
        results = []
        nums_reverse = nums[::-1]
        for i in range(len(nums)):
            left_product.append(left_product[i] * nums[i])
            right_product.append(right_product[i] * nums_reverse[i])
        for j in range(len(nums)):
            results.append(left_product[j] * right_product[len(nums)-(j+1)])
        return results

# O(1) space approach
# Time: O(n)
# Space: O(1)
# 2023.06.23: no
# notes: 和上面方法基本一样，只不过把left变成results， 然后right是一边算一边乘上去，因为results不算space
class Solution2:
    def productExceptSelf(self, nums):

        # The length of the input array
        length = len(nums)

        # The answer array to be returned
        answer = [0] * length

        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):
            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]

        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1;
        for i in reversed(range(length)):
            # For the index 'i', R would contain the
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]

        return answer

nums = [1,2,3,4]
test = Solution()
test.productExceptSelf(nums)

