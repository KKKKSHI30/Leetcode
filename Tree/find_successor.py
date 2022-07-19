# Ke Shi on July 19th, 2022

class node:
    def __init__(self, element, left = None, right = None, parent = None):
        self.element = element
        self.left = left
        self.right = right
        self.parent = parent

def successor(node):
    if node == None:
        return node
    if node.right:
        return left_most(node.right)
    else:
        while node.parent:
            if node.parent.right == node:
                node = node.parent
            else:
                return node.parent

def left_most(node):
    if node == None:
        return node
    while node.left != None:
        node = node.left
    return node


tree4 = node(4, None, None)
tree5 = node(5, None, None)
tree6 = node(6, None, None)
tree7 = node(7, None, None)
tree2 = node(2, tree4, tree5)
tree3 = node(3, tree6, tree7)
tree4.parent = tree2
tree5.parent = tree2
tree6.parent = tree2
tree7.parnet = tree3
tree1 = node(1,tree2, tree3, None)
tree2.parent = tree1
tree3.parent = tree1
successor(tree2)