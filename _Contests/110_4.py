# 1. N 是最大值，如果N还没有成功，那就是-1了，因为重复取同一个值没有任何意义，只会加大数值
# 2. 用backtrack+memorization来记录N*i这个表中取最大值，但是这个方法太慢了，需要用exchange argument
# 把backtrack每次从1-n选择，变成每次从i-n选择，根据n2从小到大sort来决定，谁后清零
# 3. 如果是上面这样，还是n^3的时间复杂度，我们要改成n^2的方法是，气质只需要考虑当前这个节点，要或者不要即可
# https://www.youtube.com/watch?v=7KaJamPY7yA
class Solution:
    def minimumTime(self, nums1, nums2, xx):
        n = len(nums1)
        p = sorted([(nums2[i], nums1[i]) for i in range(n)])
        f = [0] * (n + 1)
        for x, y in p:
            for i in reversed(range(n)):
                f[i + 1] = max(f[i + 1], f[i] + (i + 1) * x + y)
        k = sum(nums2)
        b = sum(nums1)
        for i in range(0, n + 1):
            if k * i + b - f[i] <= xx:
                return i
        return -1