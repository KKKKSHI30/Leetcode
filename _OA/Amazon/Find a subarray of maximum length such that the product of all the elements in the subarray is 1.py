# 题目: https://leetcode.com/discuss/interview-question/1692832/amazon-online-first-round-sde
class Solution:
    # notes: 1567的正确解法
    # 参考1567. Maximum Length of Subarray With Positive Product
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

    # notes: 第二个方法，比较好理解，但是难想到
    # 分两个情况，1. 所有乘积是1，直接返回即可
    # 2. 乘积是-1，那就看是从左到右的-1先出现还是从右到左的-1先出现，长的那段就是最长的
    # update一下，如果有0的话，这个方法不可行
    def maxSubArrayLength(self, arr):
        best_window_size = 0
        curr_window_size = 0
        curr_product = 1
        for a in arr:
            curr_product = curr_product * a
            curr_window_size += 1
            if curr_product == 1:
                best_window_size = curr_window_size

        for a in arr:
            curr_product = curr_product * a
            curr_window_size -= 1
            if curr_product == 1:
                if curr_window_size > best_window_size:
                    best_window_size = curr_window_size
                break

        return best_window_size


test = Solution()
test.getMaxLen([1, -1, -1, -1, 1, 1, -1])
test.getMaxLen([1, -1, -1, -1, 1, 1])
test.maxSubArrayLength([-1, -1, -1, -1, 1, -1])
