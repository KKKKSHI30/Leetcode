# Recursion Approach
# Time: O(n^2)
# Space: O(n)
# 2023.08.03: no
# notes: 真的有必要用recursion？典型脱裤子放屁好吗，原理都是一样的，找到最大的，翻到最底下
class Solution:
    def pancakeSort(self, cakes):
        # 记录反转操作序列
        self.res = []
        self.sort(cakes, len(cakes))
        return self.res

    def sort(self, cakes, n):
        # base case
        if n == 1:
            return
        # 寻找最大饼的索引
        max_cake = 0
        max_cake_index = 0
        for i in range(n):
            if cakes[i] > max_cake:
                max_cake_index = i
                max_cake = cakes[i]
        # 第一次翻转，将最大饼翻到最上面
        self.reverse(cakes, 0, max_cake_index)
        self.res.append(max_cake_index + 1)
        # 第二次翻转，将最大饼翻到最下面
        self.reverse(cakes, 0, n - 1)
        self.res.append(n)

        # 递归调用
        self.sort(cakes, n - 1)

    def reverse(self, arr, i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

# Recursion Approach
# Time: O(n^2)
# Space: O(n)
# 2023.08.03: no
# notes: 题目给的不清晰的原因是没说array是从1开始到k的，随机的就不行，如果要随机的，就需要找到最大的
# 但是每次flip都一定是2次
class Solution2:
    def pancakeSort(self, A):
        """ sort like bubble-sort
            sink the largest number to the bottom at each round
        """
        def flip(sublist, k):
            i = 0
            while i < k / 2:
                sublist[i], sublist[k-i-1] = sublist[k-i-1], sublist[i]
                i += 1

        ans = []
        value_to_sort = len(A)
        while value_to_sort > 0:
            # locate the position for the value to sort in this round
            index = A.index(value_to_sort)

            # sink the value_to_sort to the bottom,
            #   with at most two steps of pancake flipping.
            if index != value_to_sort - 1:
                # flip the value to the head if necessary
                if index != 0:
                    ans.append(index+1)
                    flip(A, index+1)
                # now that the value is at the head, flip it to the bottom
                ans.append(value_to_sort)
                flip(A, value_to_sort)

            # move on to the next round
            value_to_sort -= 1

        return ans

# Tests:
test = Solution2()
test.pancakeSort([3,2,4,1])
test.pancakeSort([6,2,4,9])