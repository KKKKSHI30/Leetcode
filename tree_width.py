# Ke Shi on July 16th, 2022
from queue import Queue

class node:
    def __init__(self, element, left = None, right = None):
        self.element = element
        self.left = left
        self.right = right

def breath_first(head):
    """Width traversal"""
    q = Queue()
    cur = head
    q.put(cur)
    while (cur != None and not q.empty()):
        cur = q.get()
        print(cur.element)
        if cur.left:
            q.put(cur.left)
        if cur.right:
            q.put(cur.right)

def tree_width(head):
    """Check the largest width of the tree using dictionary"""
    q = Queue()
    cur = head
    q.put(cur)
    map = {}
    map[cur] = 1
    width = 0
    max_width = 0
    cur_level = 1
    while not q.empty():
        cur = q.get()
        cur_node_level = map[cur]
        if cur_node_level == cur_level:
            width += 1
        else:
            max_width = max(width, max_width)
            cur_level += 1
            width = 1
        if cur.left:
            map[cur.left] = cur_node_level + 1
            q.put(cur.left)
        if cur.right:
            map[cur.right] = cur_node_level + 1
            q.put(cur.right)
    max_width = max(max_width, width)
    print(max_width)

def tree_width2(head):
    """Check the largest width of the tree not using dictionary"""
    q = Queue()
    cur = head
    q.put(cur)
    cur_end = head
    next_end = None
    max_width = 0
    width = 1
    while (cur != None and not q.empty()):
        cur = q.get()
        if cur.left:
            q.put(cur.left)
            next_end = cur.left
        if cur.right:
            q.put(cur.right)
            next_end = cur.right
        if cur_end == cur:
            max_width = max(max_width, width)
            cur_end = next_end
            next_end = None
            width = 1
        else:
            width += 1
    max_width = max(max_width, width)
    print(max_width)


tree1 = node(1,
             node(2, node(4), node(5)),
             node(3, node(6), node(7))
             )


breath_first(tree1)
tree_width(tree1)
tree_width2(tree1)