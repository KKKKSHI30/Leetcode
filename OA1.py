class node:
    def __init__(self, element, left = None, right = None, colour = None):
        self.element = element
        self.left = left
        self.right = right
        self.colour = colour

def t():
    head = node("1")
    pass

def create(head):
    total = int(input())
    while True:
        f1, f2 = input().split()
        f1 = int(f1)
        f2 = int(f2)
        if f1 > total or f2 > total:
            break
        if f1 < f2 and f2 % 2 == 0:
            node(str(f1)).left = node(str(f2))
        elif f1 < f2 and f2 % 2 == 1:
            node(str(f1)).right = node(str(f2))
        elif f2 < f1 and f1 % 2 == 0:
            node(str(f2)).left = node(str(f1))
        else:
            node(f2).right = node(f1)
    return head

tree = create()

"""
def r(head):
    if head == None:
        return None, 0
    left_head, left_children = r(head.left)
    right_head, right_children = r(head.right)
    if (left_children + right_children) % 2 == 0:
        head.colour = "B"
        return head, (left_children + right_children + 1) % 2
    else:
        head.colour = "R"
    return head, (left_children + right_children) % 2
tree1 = node(1,
             node(2, node(4), node(5)),
             node(3, node(6), None)
             )
head, odd = r(tree1)

from queue import Queue
def bfs(head):
    str = ""
    q = Queue()
    q.put(head)
    while not q.empty():
        head = q.get()
        str = str + head.colour
        if head.left:
            q.put(head.left)
        if head.right:
            q.put(head.right)
    return str


tree1 = node(1,
             node(2, node(4), node(5)),
             node(3, node(6), None)
             )
head, odd = r(tree1)
"""