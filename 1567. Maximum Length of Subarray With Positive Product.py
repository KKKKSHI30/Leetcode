# Recursion
# Time: O(n)
# Space: O(1)
# 2023.08.17: no
# notes: 参考帖子https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/solutions/820072/easy-soultion-with-dry-run-java/
# 具体解法在下面，本质上是记录positive的长度和negative的长度，交换，更新即可
class Solution:
    def getMaxLen(self, nums):
        positive = 0  # 到当前位置，最多几个构成positive
        negative = 0  # 到当前为止，最多几个构成negative
        res = 0
        for num in nums:
            temp = num
            if temp == 0:
                positive = 0
                negative = 0
            elif temp > 0:   # 如果遇到的是1
                positive += 1  # positive长度肯定+1
                negative = 0 if negative == 0 else negative + 1  # 如果negative是0的话，第一个是1也不会增加negative的长度
                # 不是0的话，negative的长度会加1
            else:
                # 本质上就是交换positive和negative，步骤和上面一样，只是判断条件一律都用negative = 0
                x = positive # 如果遇到的是-1，保存一下之前positive的长度
                positive = 0 if negative == 0 else negative + 1 # 如果negative是0，说明之前没有negative
                # positive和negative交换，positive也是0，因为他没有正的，不需要加一
                # 如果不等于0，positive跟negative交换之后需要+1
                negative = x + 1  # negative和positive交换之后，原来的positive还没+1，补加1
            res = max(res, positive)  # 每次只需要确认有多长的positive即可
        return res