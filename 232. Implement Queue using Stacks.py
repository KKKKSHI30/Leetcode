# Deque Approach
# Time: peek: O(n), other: O(1)
# Space: O(n)
# 2023.07.07: yes
# notes: 重点是peek，如果第二个栈里有东西，永远peek第二个栈，也就是反过来的那个，除非没元素了，才把s1倒过去

class MyQueue(object):
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.peek()
        return self.s2.pop()


    def peek(self):
        """
        :rtype: int
        """
        if len(self.s2) == 0:
            # 把 s1 元素压入 s2
            while len(self.s1) != 0:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.s1) == 0 and len(self.s2) == 0



myQueue = MyQueue()
myQueue.push(1) #  queue is: [1]
myQueue.push(2) #  queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek() #  return 1
myQueue.peek()
myQueue.push(3)
myQueue.peek()
myQueue.pop() #  return 1, queue is [2]
myQueue.peek()
myQueue.empty() # return false