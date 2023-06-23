# Greedy Approach
# Time: O(nlogn)
# Space: O(n)
# 2023.06.22: yes
# notes: 有两个点，第一，数值是可以重复的，所以一个nums2的element可以对应多个nums1，所以需要ditionary  = {1: [], 2: []}
# 第二个点，输出的时候，可以直接根据未排序的顺序（根据序号）去输出结果，想法不难，但是细节还挺折磨人的
class Solution(object):
    def advantageCount(self, nums1, nums2):
        assigned = {num2: [] for num2 in nums2}
        sorted_nums2 = sorted(nums2, reverse = True)
        sorted_nums1 = sorted(nums1, reverse = True)
        for j in range(len(sorted_nums2)):
            if sorted_nums1[0] > sorted_nums2[j]:
                assigned[sorted_nums2[j]].append(sorted_nums1.pop(0))
            else:
                assigned[sorted_nums2[j]].append(sorted_nums1.pop(-1))
            j += 1
        return [assigned[b].pop() for b in nums2]

# Tests:
test = Solution()
test.advantageCount([2,0,4,1,2],[1,3,0,0,2])
test.advantageCount([12,24,8,32],[13,25,32,11])


