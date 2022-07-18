# Ke Shi on July 17th, 2022

class node:
    def __init__(self, element, left = None, right = None):
        self.element = element
        self.left = left
        self.right = right

def BBT(head):
    """check if a tree is a balance binary tree"""
    balanced, height  = check_balanced_binary_tree(head)
    return balanced

def check_balanced_binary_tree(head):
    if head == None:
        return (True, 0)

    left_balanced, left_height = check_balanced_binary_tree(head.left)
    right_balanced, right_height = check_balanced_binary_tree(head.right)

    height = max(left_height, right_height) + 1
    if (left_balanced and right_balanced and
            (abs(left_height - right_height) < 2)):
        balanced = True
    else:
        balanced = False
    return (balanced, height)

tree1 = node(1,
             node(2, node(4), node(5)),
             node(3, node(6), node(7))
             )

tree2 = node(1,
             node(2, node(3, node(4), None), None),
             node(3, None, None))

check_balanced_binary_tree(tree1)
BBT(tree1)
BBT(tree2)


