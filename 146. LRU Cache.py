# Doubly Linked List
# Time: O(1) for get and put
# Space: O(capactiy)
# 2023.06.17: yes
# notes: LRU本质上是用了DoubleLinkedList 和hash map来做到get, put都为O(1)
# 所以在新加nodes的时候，要考虑同时更新两个节点
# 另一个技巧就是，linked list在更新头尾的时候，非常麻烦，可以用dummy head, dummy tail去解决
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class DoubleList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def addLast(self, x):
        x.prev = self.tail.prev
        x.next = self.tail
        self.tail.prev.next = x
        self.tail.prev = x
        self.size += 1

    def remove(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev
        self.size -= 1

    def removeFirst(self):
        if self.head.next == self.tail:
            return None
        first = self.head.next
        self.remove(first)
        return first

    def size(self):
        return self.size

class LRUCache:
    def makeRecently(self, key: int):
        # 将某个 key 提升为最近使用的
        x = self.map.get(key)
        # 先从链表中删除这个节点
        self.cache.remove(x)
        # 重新插到队尾
        self.cache.append(x)

    def addRecently(self, key: int, val: int):
        # 添加最近使用的元素
        x = Node(key, val)
        # 链表尾部就是最近使用的元素
        self.cache.append(x)
        # 别忘了在 map 中添加 key 的映射
        self.map[key] = x

    def deleteKey(self, key: int):
        # 删除某一个 key
        x = self.map.get(key)
        # 从链表中删除
        self.cache.remove(x)
        # 从 map 中删除
        self.map.pop(key)

    def removeLeastRecently(self):
        # 删除最久未使用的元素
        # 链表头部的第一个元素就是最久未使用的
        deletedNode = self.cache.pop(0)
        # 同时别忘了从 map 中删除它的 key
        deletedKey = deletedNode.key
        self.map.pop(deletedKey)

    def __init__(self, capacity: int):
        self.cache = []
        self.map = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        # 读操作
        if key not in self.map:
            return -1
        self.makeRecently(key)
        return self.map.get(key).val

    def put(self, key: int, value: int) -> None:
        # 写操作
        if key in self.map:
            self.map.get(key).val = value
            self.makeRecently(key)
            return
        if len(self.cache) == self.capacity:
            self.removeLeastRecently()
        self.addRecently(key, value)


class LRUCache2(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dic = {}
        self.head = Node(-1,-1) # 处理边缘case，同时去头去尾用dummy head很好
        self.tail = Node(-1, -1)
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
        node = Node(key, value)
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
class LRUCache3(object):

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



