class node:
    def __init__(self, element, left=None, right=None):
        self.element = element
        self.left = left
        self.right = right

def morris(head):
    if head == None:
        return
    cur = head
    while cur != None:
        most_right = cur.left
        if most_right != None:  # there is left tree
            while most_right.right != None and most_right.right != cur:   # find the most right on the left tree
                most_right = most_right.right
            if most_right.right == None:   # and let it point back to the root
                most_right.right = cur
                cur = cur.left           # cur goes left
                continue
            else:
                most_right.right = None      # let the pointer back to none, keep to the original tree
        cur = cur.right  # no left tree


# 如果只出现一次，直接打印，如果出现两次，第一次的时候打印
def morris_pre_order(head):
    if head == None:
        return
    cur = head
    while cur != None:
        most_right = cur.left
        if most_right != None:  # there is left tree
            while most_right.right != None and most_right.right != cur:
                most_right = most_right.right
            if most_right.right == None:
                print(cur.element)
                most_right.right = cur
                cur = cur.left
                continue
            else:
                most_right.right = None
        else:
            print(cur.element)
        cur = cur.right  # no left tree


# 如果只出现一次，直接打印，如果出现两次，第二次打印
def morris_in_order(head):
    if head == None:
        return
    cur = head
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
                # print(cur.element)
                most_right.right = None
        # else:
        # print(cur.element)
        print(cur.element)
        cur = cur.right  # no left tree


# 如果只有一次，直接打印，如果会来到两次，第二次来到这个节点时，逆序打印有边界
def morris_post_order(head):
    if head == None:
        return
    cur = head
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
                print_edge(cur.left)
        cur = cur.right  # no left tree
    print_edge(head)


def print_edge(head):
    tail = reverse_edge(head)
    cur = tail
    while cur:
        print(f"{cur.element} ")
        cur = cur.right
    reverse_edge(head)


def reverse_edge(head):
    pre = None
    while head:
        next = head.right
        head.right = pre
        pre = head
        head = next
    return pre


tree1 = node(1, node(2, node(4), node(5)), node(3, node(6), node(7)))
morris_pre_order(tree1)
morris_in_order(tree1)
morris_post_order(tree1)
