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

def dijkstra(graph):
    pass


graph1 = graph()
graph1.nodes = {"A": node("A"), "B": node("B"), "C": node("C"), "D": node("D"), "E": node("E")}
graph1.nodes["A"].nodes_in = 3
graph1.nodes["A"].nodes_out = 3
graph1.nodes["A"].nexts = [graph1.nodes["B"], graph1.nodes["C"], graph1.nodes["D"]]
graph1.nodes["A"].edges = [edge(graph1.nodes["A"],graph1.nodes["B"], 3),
                           edge(graph1.nodes["A"],graph1.nodes["C"], 15),
                           edge(graph1.nodes["A"],graph1.nodes["D"], 9)]
graph1.nodes["B"].nodes_in = 3
graph1.nodes["B"].nodes_out = 3
graph1.nodes["B"].nexts = [graph1.nodes["A"], graph1.nodes["C"], graph1.nodes["E"]]
graph1.nodes["B"].edges = [edge(graph1.nodes["B"],graph1.nodes["A"], 3),
                           edge(graph1.nodes["B"],graph1.nodes["C"], 2),
                           edge(graph1.nodes["B"],graph1.nodes["E"], 200)]
graph1.nodes["C"].nodes_in = 4
graph1.nodes["C"].nodes_out = 4
graph1.nodes["C"].nexts = [graph1.nodes["A"], graph1.nodes["B"], graph1.nodes["D"], graph1.nodes["E"]]
graph1.nodes["C"].edges = [edge(graph1.nodes["C"],graph1.nodes["A"], 15),
                           edge(graph1.nodes["C"],graph1.nodes["B"], 2),
                           edge(graph1.nodes["C"],graph1.nodes["D"], 7),
                           edge(graph1.nodes["C"],graph1.nodes["E"], 14)]
graph1.nodes["D"].nodes_in = 3
graph1.nodes["D"].nodes_out = 3
graph1.nodes["D"].nexts = [graph1.nodes["A"], graph1.nodes["C"], graph1.nodes["E"]]
graph1.nodes["D"].edges = [edge(graph1.nodes["D"],graph1.nodes["A"], 9),
                           edge(graph1.nodes["D"],graph1.nodes["C"], 7),
                           edge(graph1.nodes["D"],graph1.nodes["E"], 16)]
graph1.nodes["E"].nodes_in = 3
graph1.nodes["E"].nodes_out = 3
graph1.nodes["E"].nexts = [graph1.nodes["B"], graph1.nodes["C"], graph1.nodes["D"]]
graph1.nodes["E"].edges = [edge(graph1.nodes["E"],graph1.nodes["B"], 200),
                           edge(graph1.nodes["E"],graph1.nodes["C"], 14),
                           edge(graph1.nodes["E"],graph1.nodes["D"], 16)]
graph1.edges = [edge(graph1.nodes["A"],graph1.nodes["B"], 3), edge(graph1.nodes["B"],graph1.nodes["A"], 3),
                edge(graph1.nodes["A"],graph1.nodes["C"], 15), edge(graph1.nodes["C"],graph1.nodes["A"], 15),
                edge(graph1.nodes["A"],graph1.nodes["D"], 9), edge(graph1.nodes["D"],graph1.nodes["A"], 9),
                edge(graph1.nodes["B"],graph1.nodes["C"], 2), edge(graph1.nodes["C"],graph1.nodes["B"], 2),
                edge(graph1.nodes["B"],graph1.nodes["E"], 200), edge(graph1.nodes["E"],graph1.nodes["B"], 200),
                edge(graph1.nodes["C"],graph1.nodes["D"], 7), edge(graph1.nodes["D"],graph1.nodes["C"], 7),
                edge(graph1.nodes["C"],graph1.nodes["E"], 14), edge(graph1.nodes["E"],graph1.nodes["C"], 14),
                edge(graph1.nodes["D"],graph1.nodes["E"], 16), edge(graph1.nodes["E"],graph1.nodes["D"], 16)]