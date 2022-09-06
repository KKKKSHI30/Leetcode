# Definition for a Node.
import copy
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    # good space but not speed lol
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return None
        cur = head
        while cur:
            cur_next = cur.next
            cur.next = Node(cur.val)
            cur.next.next = cur_next
            cur = cur.next.next
        cur = head
        new = head.next
        while cur:
            if cur.random == None:
                cur.next.random = None
            else:
                cur.next.random = cur.random.next
            cur = cur.next.next
        cur = head
        while cur:
            if cur.next.next != None:
                cur_next = cur.next.next
                cur.next.next = cur_next.next
                cur.next = cur_next
                cur = cur_next
            else:
                cur.next = None
                return new


from collections import defaultdict
class Solution2(object):
    # time saving
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        d_org = defaultdict(int)
        d_new = defaultdict(Node)
        curr = head
        h = Node(0)
        prev = h
        i = 0
        while curr != None:
            if head.next == None:
                c = Node(curr.val)
                h.next = c
                prev = c
            else:
                c = Node(curr.val)
                prev.next = c
                prev = c

            d_org[curr] = i
            d_new[i] = c
            curr = curr.next
            i += 1

        curr = head
        c = h.next
        while curr != None and c != None:
            r = curr.random
            if r == None:
                c.random = None
            else:
                ind = d_org[r]
                c.random = d_new[ind]
            curr = curr.next
            c = c.next

        return h.next


class Solution3(object):
    # space saving
    def __init__(self):
        self.visited = {}

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None

        old_node = head
        new_node = Node(old_node.val)
        new_head = new_node
        self.visited[old_node] = new_node
        while old_node:
            if old_node.next in self.visited:
                new_node.next = self.visited[old_node.next]
            else:
                if old_node.next:
                    node = Node(old_node.next.val)
                    new_node.next = node
                    self.visited[old_node.next] = new_node.next
            if old_node.random in self.visited:
                new_node.random = self.visited[old_node.random]
            else:
                if old_node.random:
                    node = Node(old_node.random.val)
                    new_node.random = node
                    self.visited[old_node.random] = new_node.random
            old_node = old_node.next
            new_node = new_node.next
        return new_head

node1 = Node(7)
node2 = Node(13)
node3 = Node(11)
node4 = Node(10)
node5 = Node(1)
node1.next = node2
node1.random = None
node2.next = node3
node2.random = node1
node3.next = node4
node3.random = node5
node4.next = node5
node4.random = node3
node5.next = None
node5.random = node3

test = Solution2()
result1 = test.copyRandomList(node1)
