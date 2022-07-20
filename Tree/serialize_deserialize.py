# Ke Shi on July 19th, 2022
from queue import Queue

class node:
    def __init__(self, element, left = None, right = None, parent = None):
        self.element = element
        self.left = left
        self.right = right

def serialize_preorder(head):
    if head == None:
        return "#_"
    s1 = str(head.element) + "_"
    s1 += serialize_preorder(head.left)
    s1 += serialize_preorder(head.right)
    return s1


def deserialize_preorder(s1):
    q1 = Queue()
    s2 = s1.split('_')
    for i in range(len(s2)-1):
        q1.put(s2[i])
    return create_nodes(q1)

def create_nodes(q1):
    value = q1.get()
    if value == '#':
        return None
    head = node(int(value))
    head.left = create_nodes(q1)
    head.right = create_nodes(q1)
    return head




tree1 = node(1,
             node(2, node(4), node(5)),
             node(3, node(6), node(7))
             )
str1 = serialize_preorder(tree1)
str2 = '1_2_4_#_#_5_#_#_3_6_#_#_7_#_#_'
tree2 = deserialize_preorder(str1)