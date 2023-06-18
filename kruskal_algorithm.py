# Ke Shi on July 24th, 2022

class graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

class node:
    def __init__(self, element):
        self.element = element
        self.nodes_in = 0
        self.nodes_out = 0
        self.nexts = []
        self.edges = []

class edge:
    def __init__(self, node_from, node_to, weight = None):
        self.node_from = node_from
        self.node_to = node_to
        self.weight = weight

def set_init(graph):
    map_set = {}
    graph1.nodes.values()
    for node in graph1.nodes.values():
        lst = []
        lst.append(node)
        map_set[node] = lst
    return  map_set

def is_same_set(map_set, node_from, node_to):
    from_set = map_set[node_from]
    to_set = map_set[node_to]
    if from_set == to_set:
        return True
    else:
        return False

def union(map_set, node_from, node_to):
    from_set = map_set[node_from]
    to_set = map_set[node_to]
    for item in to_set:
        from_set.append(item)
        map_set[node_to] = from_set

def kruskal(graph):
    map_set = set_init(graph)
    graph.edges = sorted(graph.edges, key=lambda edge: edge.weight)
    result = []
    while len(graph.edges) != 0:
        cur = graph.edges.pop(0)
        if not is_same_set(map_set, cur.node_from, cur.node_to):
            result.append(cur)
            union(map_set,cur.node_from, cur.node_to)
    return result

graph1 = graph()
graph1.nodes = {"A": node("A"), "B": node("B"), "C": node("C"), "D": node("D"), "E": node("E")}
graph1.nodes["A"].nodes_in = 3
graph1.nodes["A"].nodes_out = 3
graph1.nodes["A"].nexts = [graph1.nodes["B"], graph1.nodes["C"], graph1.nodes["D"]]
graph1.nodes["A"].edges = [edge(graph1.nodes["A"],graph1.nodes["B"], 7),
                           edge(graph1.nodes["A"],graph1.nodes["C"], 2),
                           edge(graph1.nodes["A"],graph1.nodes["D"], 100)]
graph1.nodes["B"].nodes_in = 3
graph1.nodes["B"].nodes_out = 3
graph1.nodes["B"].nexts = [graph1.nodes["A"], graph1.nodes["D"], graph1.nodes["E"]]
graph1.nodes["B"].edges = [edge(graph1.nodes["A"],graph1.nodes["B"], 7),
                           edge(graph1.nodes["B"],graph1.nodes["D"], 1000),
                           edge(graph1.nodes["B"],graph1.nodes["E"], 100000)]
graph1.nodes["C"].nodes_in = 2
graph1.nodes["C"].nodes_out = 2
graph1.nodes["C"].nexts = [graph1.nodes["A"], graph1.nodes["D"]]
graph1.nodes["C"].edges = [edge(graph1.nodes["A"],graph1.nodes["C"], 2),
                           edge(graph1.nodes["C"],graph1.nodes["D"], 4)]
graph1.nodes["D"].nodes_in = 3
graph1.nodes["D"].nodes_out = 3
graph1.nodes["D"].nexts = [graph1.nodes["A"], graph1.nodes["B"], graph1.nodes["C"]]
graph1.nodes["D"].edges = [edge(graph1.nodes["A"],graph1.nodes["D"], 100),
                           edge(graph1.nodes["B"],graph1.nodes["D"], 1000),
                           edge(graph1.nodes["C"],graph1.nodes["D"], 4)]
graph1.nodes["E"].nodes_in = 1
graph1.nodes["E"].nodes_out = 1
graph1.nodes["E"].nexts = [graph1.nodes["B"]]
graph1.nodes["E"].edges = [edge(graph1.nodes["B"],graph1.nodes["E"], 100000)]
graph1.edges = [edge(graph1.nodes["A"],graph1.nodes["B"], 7), edge(graph1.nodes["A"],graph1.nodes["C"], 2),
                edge(graph1.nodes["A"],graph1.nodes["D"], 100), edge(graph1.nodes["B"],graph1.nodes["D"], 1000),
                edge(graph1.nodes["B"],graph1.nodes["E"], 100000), edge(graph1.nodes["C"],graph1.nodes["D"], 4)]

edges = kruskal(graph1)
