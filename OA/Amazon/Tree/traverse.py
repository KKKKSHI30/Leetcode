from queue import LifoQueue
from queue import Queue

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 先序排列，中左右
def pre_order(head):
    if head == None:
        return
    print(head.val)
    pre_order(head.left)
    pre_order(head.right)

# Last in First out  = Heap
# First in First out = queue
def pre_order_no_recursion(head):
    h = LifoQueue()
    h.put(head)
    while not h.empty():
        temp = h.get()
        print(temp.val)
        head = temp
        if head.right:
            h.put(head.right)
        if head.left:
            h.put(head.left)

# 中序排列，左中右
def in_order(head):
    if head == None:
        return
    in_order(head.left)
    print(head.val)
    in_order(head.right)

# 所有树都可以被中序切割
def in_order_no_recursion(head):
    h = LifoQueue()
    while head != None or not h.empty():
        while head:
            h.put(head)
            head = head.left
        head = h.get()
        print(head.val)
        if head.right:
            head = head.right
        else:
            head = None

# 后序排列，左右中
def post_order(head):
    if head == None:
        return
    post_order(head.left)
    post_order(head.right)
    print(head.val)

# 后序排列就是把前序排列放到堆里左右顺序变一下，然后倒一下
def post_order_no_recursion(head):
    h = LifoQueue()
    h2 = LifoQueue()
    h.put(head)
    while not h.empty():
        temp = h.get()
        h2.put(temp)
        head = temp
        if head.left:
            h.put(head.left)
        if head.right:
            h.put(head.right)
    while not h2.empty():
        print(h2.get().val)

# 宽度优先遍历用队列，深度优先遍历用堆
def bfs(head):
    q = Queue()
    q.put(head)
    while not q.empty():
        head = q.get()
        print(head.val)
        if head.left:
            q.put(head.left)
        if head.right:
            q.put(head.right)

tree1 = TreeNode(1,
             TreeNode(2, TreeNode(4), TreeNode(5)),
             TreeNode(3, TreeNode(6), TreeNode(7))
             )
pre_order(tree1)
pre_order_no_recursion(tree1)
in_order(tree1)
in_order_no_recursion(tree1)
post_order(tree1)
post_order_no_recursion(tree1)
bfs(tree1)