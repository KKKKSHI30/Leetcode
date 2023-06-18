# Ke Shi on July 17th, 2022

class node:
    def __init__(self, element, left = None, right = None):
        self.element = element
        self.left = left
        self.right = right

def FBT(head):
    """Check whether a tree is a full binary tree"""
    height, nodes = full_binary_tree(head)
    return (2**height -1 == nodes)

def full_binary_tree(head):
    if head == None:
        return (0, 0)
    left_height, left_nodes = full_binary_tree(head.left)
    right_height, right_nodes = full_binary_tree(head.right)
    height = max(left_height, right_height) + 1
    nodes = left_nodes + right_nodes + 1
    return (height, nodes)



tree1 = node(1,
             node(2, node(4), node(5)),
             node(3, node(6), node(7))
             )
tree2 = node(4,
             node(2, None, node(3)),
             node(6, node(5), node(7))
             )
FBT(tree1)
FBT(tree2)