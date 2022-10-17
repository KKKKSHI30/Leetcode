# Ke Shi on July 19th, 2022

class node:
    def __init__(self, element, left = None, right = None):
        self.element = element
        self.left = left
        self.right = right

def lowest_common_ancestor(head, n1, n2):
    map = {}
    map[head] = head
    ancestor(head, map)
    lst = []
    cur = n1
    while cur != head:
        lst.append(cur)
        cur = map[cur]
    lst.append(head)
    cur2 = n2
    while cur2 not in lst:
        cur2 = map[cur2]
    return cur2.element

def ancestor(head, ancester_map):
    if head == None:
        return
    if head.left:
        ancester_map[head.left] = head
        ancestor(head.left, ancester_map)
    if head.right:
        ancester_map[head.right] = head
        ancestor(head.right, ancester_map)

def LCA(head, n1, n2):
    if head == None or head == n1 or head == n2:
        return head
    left = LCA(head.left, n1, n2)
    right = LCA(head.right, n1, n2)
    if (left != None and right != None):
        return head
    return left if left != None else right

tree4 = node(4)
tree5 = node(5)
tree6 = node(6)
tree7 = node(7)
tree2 = node(2, tree4, tree5)
tree3 = node(3, tree6, tree7)
tree1 = node(1,
             tree2, tree3
             )

lowest_common_ancestor(tree1, tree4, tree5)
LCA(tree1, tree4, tree5)

