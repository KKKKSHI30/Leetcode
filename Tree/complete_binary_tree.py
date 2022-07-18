# Ke Shi on July 17th, 2022
from queue import Queue

class node:
    def __init__(self, element, left = None, right = None):
        self.element = element
        self.left = left
        self.right = right

def check_CBT(head):
    """Check whether a tree is a complete binary tree"""
    q = Queue()
    critical_point = False
    cur = head
    q.put(cur)
    while (cur != None and not q.empty()):
        cur = q.get()
        if critical_point:
            if cur.left != None and cur.right != None:
                return False
        if cur.left:
            q.put(cur.left)
        if cur.right:
            q.put(cur.right)
        if (not cur.left and cur.right):
            return False
        if (cur.left and not cur.right) or (not cur.left and not cur.right):
            critical_point = True
    return True

tree1 = node(1,
             node(2, node(4), node(5)),
             node(3, node(6), node(7))
             )
tree2 = node(1,
             node(2, node(4), None),
             node(3, node(6), node(7))
             )

check_CBT(tree1)
check_CBT(tree2)