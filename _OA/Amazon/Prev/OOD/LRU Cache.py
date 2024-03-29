class LRUCache1:
    # no, cannot work, or it become really complex, because we need add another index
    def __init__(self, capacity: int):
        if capacity > 0:
            self.capacity = capacity
            self.order_list = []
            self.dictionary = {}
        else:
            return False

    def get(self, key):
        if key in self.dictionary:
            self.order_list.pop(self.order_list.index(key))
            self.order_list.append(key)
            return self.dictionary[key]
        else:
            return -1

    def put(self, key, value):
        if len(self.dictionary) >= self.capacity:
            if key in self.dictionary:
                self.dictionary[key] = value
                self.order_list.pop(self.order_list.index(key))
                self.order_list.append(key)
            else:
                self.dictionary.pop(self.order_list.pop())
                self.order_list.append(key)
                self.dictionary[key] = value
        else:
            if key in self.order_list:
                self.dictionary[key] = value
                self.order_list.pop(self.order_list.index(key))
                self.order_list.append(key)
            else:
                temp_key = self.order_list.pop()
                self.order_list.append(key)
                self.dictionary.pop(temp_key)
                self.dictionary[key] = value


from collections import OrderedDict


class LRUCache2(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return - 1

        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)

class LRUCache():
    def __init__(self, capacity):
        self.dict = OrderedDict()
        self.capacity = capacity
    def get(self, key):
        if key not in self.dict:
            return - 1
        self.dict.move_to_end(key)
        return self.dict[key]
    def put(self, key, value):
        if key in self.dict:
            self.dict.move_to_end(key)
        self.dict[key] = value
        if len(self.dict) > self.capacity:
            self.dict.popitem(last=False)


class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache():
    def _add_node(self, node):
        """
        Always add the new node right after head.
        """
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """
        Remove an existing node from the linked list.
        """
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        """
        Move certain node in between to the head.
        """
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """
        Pop the current tail.
        """
        res = self.tail.prev
        self._remove_node(res)
        return res

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.get(key, None)
        if not node:
            return -1

        # move the accessed node to the head;
        self._move_to_head(node)

        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self.cache.get(key)

        if not node:
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self._add_node(newNode)

            self.size += 1

            if self.size > self.capacity:
                # pop the tail
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            # update the value.
            node.value = value
            self._move_to_head(node)

test = LRUCache(2)
test.put(1,1)
test.put(2,2)
v1 = test.get(1)
# test.put(1,3)
test.put(3,3)
test.get(2)
test.put(4,4)
test.get(1)
test.get(3)
test.get(4)
