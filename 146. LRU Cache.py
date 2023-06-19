# Doubly Linked List
# Time: O(1) for get and put
# Space: O(capactiy)
# 2023.06.17: yes
# notes: LRU本质上是用了DoubleLinkedList 和hash map来做到get, put都为O(1)
# 所以在新加nodes的时候，要考虑同时更新两个节点
# 另一个技巧就是，linked list在更新头尾的时候，非常麻烦，可以用dummy head, dummy tail去解决
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dic = {}
        self.head = ListNode(-1,-1) # 处理边缘case，同时去头去尾用dummy head很好
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail # 特别容易忘
        self.tail.prev = self.head

    def add(self, node):
        # update links of the new added node
        # 只是加，不考虑越界的问题
        previous_end = self.tail.prev
        previous_end.next = node
        node.next = self.tail
        node.prev = previous_end
        self.tail.prev = node


    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dic:
            old_node = self.dic[key]
            self.remove(old_node)
        node = ListNode(key, value)
        self.dic[key] = node    # update hash table的内容
        self.add(node)

        if len(self.dic) > self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.dic[node_to_delete.key]



# Built-in Approach:
# Time: O(1) for get and put
# Space: O(1)
# 2023.06.17: no
# notes: 是一个built in function,用的基本都是OrderedDict的功能，面试要问能不能用才能用，最重要的还是double linked list得方法
import collections
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dic = collections.OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return -1
        self.dic.move_to_end(key)
        return self.dic[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dic:
            self.dic.move_to_end(key)
        self.dic[key] = value
        if len(self.dic) > self.capacity:
            self.dic.popitem(False)


# Test
obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
obj.get(1)
obj.put(3,3)
obj.get(2)
obj.put(4,4)
obj.get(3)
obj.get(4)



