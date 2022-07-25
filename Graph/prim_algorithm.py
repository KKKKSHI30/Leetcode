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

def prim(graph):
    edge_set = []
    node_set = []
    result = []
    for node in graph.nodes.values():
        # for random tree situations
        if node not in node_set:
            node_set.append(node)
            for edge in node.edges:
                edge_set.append(edge)
            while len(edge_set) != 0:
                edge_set = sorted(edge_set, key=lambda edge: edge.weight)
                smallest_weight_edge = edge_set.pop(0)
                to_node = smallest_weight_edge.node_to
                if to_node not in node_set:
                    node_set.append(to_node)
                    result.append(smallest_weight_edge)
                    for next_edge in to_node.edges:
                        edge_set.append(next_edge)
    return result


graph1 = graph()
graph1.nodes = {"A": node("A"), "B": node("B"), "C": node("C"), "D": node("D"), "E": node("E"), "F": node("F")}
graph1.nodes["A"].nodes_in = 3
graph1.nodes["A"].nodes_out = 3
graph1.nodes["A"].nexts = [graph1.nodes["B"], graph1.nodes["C"], graph1.nodes["D"]]
graph1.nodes["A"].edges = [edge(graph1.nodes["A"],graph1.nodes["B"], 6),
                           edge(graph1.nodes["A"],graph1.nodes["C"], 1),
                           edge(graph1.nodes["A"],graph1.nodes["D"], 5)]
graph1.nodes["B"].nodes_in = 3
graph1.nodes["B"].nodes_out = 3
graph1.nodes["B"].nexts = [graph1.nodes["A"], graph1.nodes["C"], graph1.nodes["E"]]
graph1.nodes["B"].edges = [edge(graph1.nodes["B"],graph1.nodes["A"], 6),
                           edge(graph1.nodes["B"],graph1.nodes["C"], 5),
                           edge(graph1.nodes["B"],graph1.nodes["E"], 3)]
graph1.nodes["C"].nodes_in = 5
graph1.nodes["C"].nodes_out = 5
graph1.nodes["C"].nexts = [graph1.nodes["A"], graph1.nodes["B"], graph1.nodes["D"], graph1.nodes["E"], graph1.nodes["F"]]
graph1.nodes["C"].edges = [edge(graph1.nodes["C"],graph1.nodes["A"], 1),
                           edge(graph1.nodes["C"],graph1.nodes["B"], 5),
                           edge(graph1.nodes["C"],graph1.nodes["D"], 5),
                           edge(graph1.nodes["C"],graph1.nodes["E"], 6),
                           edge(graph1.nodes["C"],graph1.nodes["F"], 4)]
graph1.nodes["D"].nodes_in = 3
graph1.nodes["D"].nodes_out = 3
graph1.nodes["D"].nexts = [graph1.nodes["A"], graph1.nodes["C"], graph1.nodes["F"]]
graph1.nodes["D"].edges = [edge(graph1.nodes["D"],graph1.nodes["A"], 5),
                           edge(graph1.nodes["D"],graph1.nodes["C"], 5),
                           edge(graph1.nodes["D"],graph1.nodes["F"], 2)]
graph1.nodes["E"].nodes_in = 3
graph1.nodes["E"].nodes_out = 3
graph1.nodes["E"].nexts = [graph1.nodes["B"], graph1.nodes["C"], graph1.nodes["F"]]
graph1.nodes["E"].edges = [edge(graph1.nodes["E"],graph1.nodes["B"], 3),
                           edge(graph1.nodes["E"],graph1.nodes["C"], 6),
                           edge(graph1.nodes["E"],graph1.nodes["F"], 6)]
graph1.nodes["F"].nodes_in = 3
graph1.nodes["F"].nodes_out = 3
graph1.nodes["F"].nexts = [graph1.nodes["C"], graph1.nodes["D"], graph1.nodes["E"]]
graph1.nodes["F"].edges = [edge(graph1.nodes["F"],graph1.nodes["C"], 4),
                           edge(graph1.nodes["F"],graph1.nodes["D"], 2),
                           edge(graph1.nodes["F"],graph1.nodes["E"], 6)]
graph1.edges = [edge(graph1.nodes["A"],graph1.nodes["B"], 6), edge(graph1.nodes["B"],graph1.nodes["A"], 6),
                edge(graph1.nodes["A"],graph1.nodes["C"], 1), edge(graph1.nodes["C"],graph1.nodes["A"], 1),
                edge(graph1.nodes["A"],graph1.nodes["D"], 5), edge(graph1.nodes["D"],graph1.nodes["A"], 5),
                edge(graph1.nodes["B"], graph1.nodes["C"], 5), edge(graph1.nodes["C"], graph1.nodes["B"], 5),
                edge(graph1.nodes["B"], graph1.nodes["E"], 3), edge(graph1.nodes["E"], graph1.nodes["B"], 3),
                edge(graph1.nodes["C"], graph1.nodes["D"], 5), edge(graph1.nodes["D"], graph1.nodes["C"], 5),
                edge(graph1.nodes["C"], graph1.nodes["E"],6), edge(graph1.nodes["E"], graph1.nodes["C"], 6),
                edge(graph1.nodes["C"], graph1.nodes["F"], 4), edge(graph1.nodes["F"], graph1.nodes["C"], 4),
                edge(graph1.nodes["D"], graph1.nodes["F"], 2), edge(graph1.nodes["F"], graph1.nodes["D"], 2),
                edge(graph1.nodes["E"], graph1.nodes["F"], 6), edge(graph1.nodes["F"], graph1.nodes["E"], 6)]

result = prim(graph1)






