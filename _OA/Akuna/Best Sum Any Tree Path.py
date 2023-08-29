def bestSumAnyTreePath(parent, value):
    max_path = -float('inf')
    tree = createTree(parent, value)
    def gain_from_subtree(node):
        nonlocal max_path
        if node not in tree:
            return 0
        maximumBranchSum1 = 0
        maximumBranchSum2 = 0
        for i in tree[node]:
            temp = gain_from_subtree(node[i])
            if temp > maximumBranchSum1:
                maximumBranchSum1, maximumBranchSum2 = temp, maximumBranchSum1
            elif temp > maximumBranchSum2:
                maximumBranchSum2 = temp
        max_path = max(max_path, tree[node][i][1] + maximumBranchSum1 + maximumBranchSum2)
        return maximumBranchSum1 + tree[node][i][1]
    gain_from_subtree(tree[-1])
    return max_path


def createTree(parent, value):
    tree = {}
    for i in range(len(parent)):
        if parent[i] not in tree:
            tree[parent[i]] = [[i, value[i]]]
        else:
            tree[parent[i]].append([i, value[i]])
    return tree

parent = [-1,0,1,2,0]
value = [-2,10,10,-3,10]
createTree(parent, value)

bestSumAnyTreePath(parent, value)