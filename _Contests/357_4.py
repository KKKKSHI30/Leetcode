# notes: https://www.youtube.com/watch?v=J4BcQ-pjbuc
# 主要说一下思路，A是记录重复set的元素，比如这个例子，5和10都在1这个category里面，那么根据第一步排序之后
# 10在5前面，5就会进A，如果这个category的元素第一次遇到，就加到seen里面，第二次遇到也会加，只不过seen是个set
# 加了也没用，是用来记录distinct category的，然后每次遇到下一个element的时候，把A中最小的pop出来即可
# 比较大小，因为A的category是重复的，pop出来也不糊及影响distinct category的平方数
# 如果已经达到k的大小，那么就算重复出现同一个category的东西也不需要运算了，因为根据大小排序，同一个category
# 的东西不会比前面大，不需要pop
# 如果k个东西都不同category，即没有重复category的元素，因为按大小排序，之后也不会增大distinct category的平方数了
# 到这个时候为止，就是最大的值了
class Solution:
    def findMaximumElegance(self, items, k):
        items = sorted(items, key=lambda v: -v[0])
        res = cur = 0
        A = []
        seen = set()
        for i, (p, c) in enumerate(items):
            if i < k:
                if c in seen:
                    A.append(p)
                cur += p
            elif c not in seen:
                if not A:
                    break
                cur += p - A.pop()
            seen.add(c)
            res = max(res, cur + len(seen) * len(seen))
        return res


# Tests:
test = Solution()
test.findMaximumElegance(items = [[3,2],[5,3],[10,1]], k = 2)