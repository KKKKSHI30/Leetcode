# Ke Shi on July 16th, 2022
from queue import LifoQueue
import sys

class node:
    def __init__(self, element, left = None, right = None):
        self.element = element
        self.left = left
        self.right = right

pre_value = -sys.maxsize - 1
def in_order(head):
    """Change the in-order traverse to check search binary tree"""
    global pre_value
    if head == None:
        return True
    BST = in_order(head.left)
    if BST == False:
        return False
    if head.element <= pre_value:
        return False
    pre_value = head.element
    return in_order(head.right)

def in_order_lst(head):
    """Put all the numbers in-order into a list and check if it's a binary search tree"""
    global lst
    if head == None:
        return
    in_order_lst(head.left)
    lst.append(head.element)
    in_order_lst(head.right)

def check_lst(lst):
    for i in range(len(lst) -1 ):
        if lst[i] > lst[i+1]:
            return False
        i += 1
    return True

def in_order_no_recursion(head):
    """Change the in_order_no_recursion algorithm to check if  it's a binary search tree"""
    global pre_value
    in_order_stack = LifoQueue()
    cur = head
    while (cur != None or not in_order_stack.empty()):
        while cur:
            in_order_stack.put(cur)
            cur = cur.left
        cur = in_order_stack.get()
        if cur.element < pre_value:
            return False
        pre_value = cur.element
        if cur.right:
            cur = cur.right
        else:
            cur = None
    return True

def SBT(head):
    search_binary, cur_min, cur_max = search_binary_tree(head)
    return search_binary

def search_binary_tree(head):
    """Using resursion with min, max, search_binary_tree as three variables and do the recursion"""
    if head == None:
        return (True, None, None)
    cur_min = head.element
    cur_max = head.element
    left_search, left_min, left_max = search_binary_tree(head.left)
    right_search, right_min, right_max = search_binary_tree(head.right)

    if head.left != None:
        cur_min = min(cur_min, left_min)
        cur_max = max(cur_max, left_max)
    if head.right != None:
        cur_min = min(cur_min, right_min)
        cur_max = max(cur_max, left_max)
    search_binary = True

    if left_max != None and (not left_search or left_max > head.element):
        search_binary = False
    if right_min != None and (not right_search or right_min < head.element):
        search_binary = False
    return (search_binary, cur_min, cur_max)

tree1 = node(1,
             node(2, node(4), node(5)),
             node(3, node(6), node(7))
             )
tree2 = node(4,
             node(2, node(1), node(3)),
             node(6, node(5), node(7))
             )

pre_value = -sys.maxsize - 1
in_order(tree1)
pre_value = -sys.maxsize - 1
in_order(tree2)

lst = []
in_order_lst(tree1)
check_lst(lst)
lst = []
in_order_lst(tree2)
check_lst(lst)

pre_value = -sys.maxsize - 1
in_order_no_recursion(tree1)
pre_value = -sys.maxsize - 1
in_order_no_recursion(tree2)

SBT(tree1)
SBT(tree2)

