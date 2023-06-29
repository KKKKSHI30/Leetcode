# Merge sort Approach
# Time: O(nlogn)
# Space: O(n)
# 2023.06.28: no
# notes: 重点是排序的时候，j-i+1中间的部分也就是mid+1 到j的部分就是小于i的部分，把这部分加到Results就可以
# 保持最初的value和index对应，才可以加到results里面去
class Solution:
    def countSmaller(self, nums):
        n = len(nums)
        arr = [[v, i] for i, v in enumerate(nums)]  # record value and index
        result = [0] * n

        def merge_sort(arr, left, right):
            # merge sort [left, right) from small to large, in place
            if right - left <= 1:
                return
            mid = (left + right) // 2
            merge_sort(arr, left, mid)
            merge_sort(arr, mid, right)
            merge(arr, left, right, mid)

        def merge(arr, left, right, mid):
            # merge [left, mid) and [mid, right)
            i = left  # current index for the left array
            j = mid  # current index for the right array
            # use temp to temporarily store sorted array
            temp = []
            while i < mid and j < right:
                if arr[i][0] <= arr[j][0]:
                    # j - mid numbers jump to the left side of arr[i]
                    result[arr[i][1]] += j - mid
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1
            # when one of the subarrays is empty
            while i < mid:
                # j - mid numbers jump to the left side of arr[i]
                result[arr[i][1]] += j - mid
                temp.append(arr[i])
                i += 1
            while j < right:
                temp.append(arr[j])
                j += 1
            # restore from temp
            for i in range(left, right):
                arr[i] = temp[i - left]

        merge_sort(arr, 0, n)

        return result


# Segment Tree Approach
# Time: O(nlogm)
# Space: O(m)
# 2023.06.28: no
# notes: 第二遍刷的话，还是重新看一下segment tree的implementation吧，虽然这道题的重点不是segmentation tree
class Solution2:
    def countSmaller(self, nums):
        # implement segment tree
        # 更新index点上的值，因为遇到一个就加一个
        def update(index, value, tree, size):
            index += size  # shift the index to the leaf
            # update from leaf to root
            tree[index] += value
            while index > 1:
                index //= 2
                tree[index] = tree[index * 2] + tree[index * 2 + 1]
        # 找到left和right中间的和
        def query(left, right, tree, size):
            # return sum of [left, right)
            result = 0
            left += size  # shift the index to the leaf
            right += size
            while left < right:
                # if left is a right node
                # bring the value and move to parent's right node
                # 并不一定直接都被计算出来，多余的部分在left上面
                if left % 2 == 1:
                    result += tree[left]
                    left += 1
                # else directly move to parent
                left //= 2
                # if right is a right node
                # bring the value of the left node and move to parent
                # 多余的部分在right上面3
                if right % 2 == 1:
                    right -= 1
                    result += tree[right]
                # else directly move to parent
                right //= 2
            return result

        offset = 10  # offset negative to non-negative
        size = 2 * 10 + 1  # total possible values in nums
        tree = [0] * (2 * size)
        result = []
        for num in reversed(nums):
            smaller_count = query(0, num + offset, tree, size)
            result.append(smaller_count)
            update(num + offset, 1, tree, size)
        return reversed(result)


# Binary Indexed Tree (Fenwick Tree) Approach
# Time: O(nlogm)
# Space: O(m)
# 2023.06.28: no
class Solution3:
    def countSmaller(self, nums):
        # implement Binary Index Tree
        # 更新BIT，把当前节点加一
        def update(index, value, tree, size):
            index += 1  # index in BIT is 1 more than the original index
            while index < size:
                tree[index] += value
                index += index & -index  # add the last bit which is remove

        # 加起来
        def query(index, tree):
            # return sum of [0, index)
            result = 0
            while index >= 1:
                result += tree[index]
                index -= index & -index    # remove the last bit which is remove
            return result

        offset = 10**4  # offset negative to non-negative
        size = 2 * 10**4 + 2  # total possible values in nums plus one dummy
        tree = [0] * size
        result = []
        for num in reversed(nums):
            smaller_count = query(num + offset, tree)
            result.append(smaller_count)
            update(num + offset, 1, tree, size)
        return reversed(result)

# Tests:
test = Solution3()
test.countSmaller([4,3,2,1,0])

