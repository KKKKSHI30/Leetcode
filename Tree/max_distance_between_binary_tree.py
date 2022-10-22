class Node(object):
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def max_distance(head):
    distance, height = max_distance_between_nodes(head)
    return distance

def max_distance_between_nodes(head):
    if head == None:
        return 0, 0
    left_distance, left_height = max_distance_between_nodes(head.left)
    right_distance, right_height = max_distance_between_nodes(head.right)
    total_distance = left_height + right_height + 1
    max_total = max(total_distance, max(left_distance, right_distance))
    height = max(left_height, right_height) + 1
    return max_total, height

tree1 = Node(1,
             Node(2, Node(4), Node(5)),
             Node(3, Node(6), Node(7))
             )
max_distance(tree1)
tree2 = Node(1,
             Node(2, Node(4), Node(5, Node(8,Node(9)))),
             Node(3, Node(6), Node(7))
             )
max_distance(tree2)