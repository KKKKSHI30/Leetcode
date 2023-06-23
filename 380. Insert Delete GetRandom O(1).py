# HashMap + ArrayList Approach
# Time: O(1)
# Space: O(1)
# 2023.06.22:no
# notes: 对各种数据结构不够了解，思路不难，但是很难想到用hashmap+arraylist
import random

class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.valToIndex = {}

    def insert(self, val):
        if val in self.valToIndex:
            return False
        self.valToIndex[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        if val not in self.valToIndex:
            return False
        index = self.valToIndex[val]
        self.valToIndex[self.nums[-1]] = index
        self.nums[index], self.nums[-1] = self.nums[-1], self.nums[index]
        self.nums.pop()
        del self.valToIndex[val]
        return True

    def getRandom(self):
        return random.choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()