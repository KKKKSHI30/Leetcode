# Ke Shi on July 15th, 2022

from queue import LifoQueue

class node:
    def __init__(self, element, left = None, right = None):
        self.element = element
        self.left = left
        self.right = right

def pre_order(head):
    if head == None:
        return
    print(head.element)
    pre_order(head.left)
    pre_order(head.right)

def in_order(head):
    if head == None:
        return
    in_order(head.left)
    print(head.element)
    in_order(head.right)

def post_order(head):
    if head == None:
        return
    post_order(head.left)
    post_order(head.right)
    print(head.element)

def pre_order_no_recursion(head):
    pre_order_stack = LifoQueue()
    pre_order_stack.put(head)
    while (not pre_order_stack.empty() and head != None):
        cur = pre_order_stack.get()
        print(cur.element)
        if cur.right:
            pre_order_stack.put(cur.right)
        if cur.left:
            pre_order_stack.put(cur.left)

def in_order_no_recursion(head):
    in_order_stack = LifoQueue()
    cur = head
    while (cur != None or not in_order_stack.empty()):
        while cur:
            in_order_stack.put(cur)
            cur = cur.left
        cur = in_order_stack.get()
        print(cur.element)
        if cur.right:
            cur = cur.right
        else:
            cur = None

def post_order_no_recursion(head):
    post_order_stack = LifoQueue()
    post_order_save_stack = LifoQueue()
    post_order_stack.put(head)
    while (not post_order_stack.empty() and head != None):
        cur = post_order_stack.get()
        post_order_save_stack.put(cur)
        if cur.left:
            post_order_stack.put(cur.left)
        if cur.right:
            post_order_stack.put(cur.right)
    while not post_order_save_stack.empty():
        cur = post_order_save_stack.get()
        print(cur.element)



tree1 = node(1,
             node(2, node(4), node(5)),
             node(3, node(6), node(7))
             )
pre_order(tree1)
pre_order_no_recursion(tree1)
in_order(tree1)
in_order_no_recursion(tree1)
post_order(tree1)
post_order_no_recursion(tree1)