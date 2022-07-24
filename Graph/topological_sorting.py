# Ke Shi on July 24th, 2022
from queue import Queue

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


def topological_sorting(graph):
    zeroinqueue = Queue()
    inmap = {}
    for node in graph1.nodes.values():
        inmap[node] = node.nodes_in
        if node.nodes_in == 0:
            zeroinqueue.put(node)
    result = []
    while not zeroinqueue.empty():
        cur = zeroinqueue.get()
        result.append(cur)
        for next in cur.nexts:
            inmap[next] -= 1
            if inmap[next] == 0:
                zeroinqueue.put(next)
    return result


graph1 = graph()
graph1.nodes = {"A": node("A"), "B": node("B"), "C": node("C"), "D": node("D")}
graph1.nodes["A"].nodes_in = 0
graph1.nodes["A"].nodes_out = 2
graph1.nodes["A"].nexts = [graph1.nodes["B"], graph1.nodes["C"]]
graph1.nodes["A"].edges = [edge(graph1.nodes["A"], graph1.nodes["B"]),
                           edge(graph1.nodes["A"], graph1.nodes["C"])]
graph1.nodes["B"].nodes_in = 1
graph1.nodes["B"].nodes_out = 2
graph1.nodes["B"].nexts = [graph1.nodes["C"], graph1.nodes["D"]]
graph1.nodes["B"].edges = [edge(graph1.nodes["B"], graph1.nodes["C"]),
                           edge(graph1.nodes["B"], graph1.nodes["D"])]
graph1.nodes["C"].nodes_in = 2
graph1.nodes["C"].nodes_out = 1
graph1.nodes["C"].nexts = [graph1.nodes["D"]]
graph1.nodes["C"].edges = [edge(graph1.nodes["C"], graph1.nodes["D"])]
graph1.nodes["D"].nodes_in = 2
graph1.nodes["D"].nodes_out = 0
graph1.nodes["D"].nexts = []
graph1.nodes["D"].edges = []
graph1.edges = [edge(graph1.nodes["A"], graph1.nodes["B"]), edge(graph1.nodes["A"], graph1.nodes["C"]),
                edge(graph1.nodes["B"], graph1.nodes["C"]), edge(graph1.nodes["B"], graph1.nodes["D"]),
                edge(graph1.nodes["C"], graph1.nodes["D"])]

result = topological_sorting(graph1)