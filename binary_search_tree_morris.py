class node:
    def __init__(self, element, left=None, right=None):
        self.element = element
        self.left = left
        self.right = right


def morris_BST(head):
    if head == None:
        return
    cur = head
    pre_value = float("-Inf")
    while cur != None:
        most_right = cur.left
        if most_right != None:  # there is left tree
            while most_right.right != None and most_right.right != cur:
                most_right = most_right.right
            if most_right.right == None:
                most_right.right = cur
                cur = cur.left
                continue
            else:
                most_right.right = None
        if cur.element <= pre_value:
            return False
        pre_value = cur.element
        cur = cur.right  # no left tree
    return True


tree1 = node(1, node(2, node(4), node(5)), node(3, node(6), node(7)))
morris_BST(tree1)
tree2 = node(4, node(2, node(1), node(3)), node(6, node(5), node(7)))
morris_BST(tree2)
