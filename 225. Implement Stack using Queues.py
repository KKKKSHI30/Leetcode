# Deque Approach
# Time: O(n)
# Space: O(n)
# 2023.07.07: yes
import queue
from collections import deque

class MyStack(object):

    def __init__(self):
        self.q = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q.append(x)

    def pop(self):
        """
        :rtype: int
        """
        pop = self.q.pop()
        return pop

    def top(self):
        """
        :rtype: int
        """
        return self.q[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q) == 0

# Two Queue Approach
# Time: O(n)  # 写pop的话，pop就是O(n),其他事O(1);要不就是push O(n)，其他O(1);最后一个用的单queue,一样是O(n)
# Space: O(1)
# 2023.07.07: yes
# notes: 三个方法，除了单独的不一样，其他都和queue一样不需要修改
# Removes the element on top of the stack
# 1      #      # 3     # 3 2 1
# 2      # 2 1  # 2 1   #
class MyStack2:
    def __init__(self):
        self.q = deque()
        self.top_elem = 0

    def push(self, x: int):
        self.q.append(x)
        self.top_elem = x

    def pop(self) -> int:
        size = len(self.q)
        # 留下队尾 2 个元素
        while size > 2:
            self.q.append(self.q.popleft())
            size -= 1
        # 记录新的队尾元素
        self.top_elem = self.q[0]
        self.q.append(self.q.popleft())
        # 删除之前的队尾元素
        return self.q.popleft()

    def top(self) -> int:
        return self.top_elem

    def empty(self) -> bool:
        return len(self.q) == 0


# Tests:
obj = MyStack()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.pop()
param_5 = obj.empty()