class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deserialize_BFS(root):
    if not root:
        return None
    nodes = [None if val is None else TreeNode(val) for val in root]
    child_index = 1
    for node in nodes:
        if node:
            if child_index < len(nodes):
                node.left = nodes[child_index]
                child_index += 1
            if child_index < len(nodes):
                node.right = nodes[child_index]
                child_index += 1
    return nodes[0]

def serialize_BFS(root):
    if not root:
        return []

    queue = [root]
    result = []

    while queue:
        node = queue.pop(0)

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result