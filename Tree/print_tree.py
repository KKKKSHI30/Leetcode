class node:
    def __init__(self, element, left = None, right = None):
        self.element = element
        self.left = None
        self.right = None


def printTree(root):
    if not root:
        return
    print('Binary Tree:')
    printInOrder(root, 0, 'H', 17)


def printInOrder(root, height, preStr, length):
    if not root:
        return
    printInOrder(root.right, height + 1, 'v', length)
    string = preStr + str(root.element) + preStr
    leftLen = (length - len(string)) // 2
    rightLen = length - len(string) - leftLen
    res = " " * leftLen + string + " " * rightLen
    print(" " * height * length + res)
    printInOrder(root.left, height + 1, '^', length)


head = node(1)
head.left = node(-222222222)
head.right = node(3)
head.left.left = node(523)
head.right.left = node(55555555)
head.right.right = node(66)
head.left.left.right = node(777)
printTree(head)