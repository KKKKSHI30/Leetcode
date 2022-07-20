# Ke Shi on July 20th, 2022

# 邻接表
# 适合稀疏图的表示，但是不能快速定位到某条边， 且不能表示逆邻接矩阵， 只能关心入度和出度其中之一
# 邻接矩阵
# 简单，适合密集图，稀疏图浪费空间
# 十字链表
# 邻接表的改良， 可同时表示邻接矩阵和逆邻接矩阵， 入度和出度
# 邻接多重表
# 关注边， 且存在删除边的操作
# 边集数组
# 关注边，且需要依次处理每一条边

class graph:
    def __init__(self):
        nodes = {}
        edges = []

class node:
    def __init__(self, element):
        element = element
        nodes_in = 0
        nodes_out = 0
        nexts = []
        edges = []


class edge:
    def __init__(self, weight, node_from, node_to):
        weight = weight
        node_from = node_from
        node_to = node_to


def create_graph(m):
    """m1 is a matrix [][], matrix[0][0] is from, matrix[0][1] is to, matrix[0][2] is weight"""
    for i in range(len(m)):
        node_from = m[i][0]
        node_to = m[i][1]
        weight = m[i][2]
        if node_from not in graph.nodes:
            graph.nodes[node_from] = node(node_from)
        if node_to not in graph.nodes:
            graph.nodes[node_to] = node(node_to)
        fromnode = graph.nodes[node_from]
        tonode = graph.nodes[node_to]
        newedge = edge(weight, fromnode, tonode)
        fromnode.nexts.append(tonode)
        fromnode.nodes_out += 1
        tonode.nodes_in += 1
        fromnode.edges.append(newedge)
        graph.edges.append(newedge)
        return graph



