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
def pop():   # if pop is O(n)
    q1 = queue.Queue()
    q2 = queue.Queue()
    while len(q1) > 1:
        top = q1.pop(0)
        q2.append(top)
    q1.pop(0)
    q1, q2 = q2, q1

# Pushes an element onto the stack
def push(x):  # if push is O(n)
    q1 = queue.Queue()
    q2 = queue.Queue()
    q2.append(x)
    top = x
    while len(q1) > 0:
        q2.append(q1.pop(0))
    q1, q2 = q2, q1

# Pushes an element onto the stack
def push(x): # 用单queue去解决stack
    q1 = queue.Queue()
    q2 = queue.Queue()
    q1.append(x)
    sz = len(q1)
    while sz > 1:
        q1.append(q1.pop(0))
        sz -= 1


# Tests:
obj = MyStack()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.pop()
param_5 = obj.empty()