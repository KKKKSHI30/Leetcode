# Ke Shi on July 23th, 2022
from queue import Queue
from queue import LifoQueue

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


def BFS(node):
    if node == None:
        return
    q = Queue()
    unique = []
    q.put(node)
    unique.append(node)
    while not q.empty():
        cur = q.get()
        print(cur.element)
        for i in cur.nexts:
            if i not in unique:
                unique.append(i)
                q.put(i)

def DFS(node):
    if node == None:
        return
    s = LifoQueue()
    unique = []
    s.put(node)
    unique.append(node)
    print(node.element)
    while not s.empty():
        cur = s.get()
        for i in cur.nexts:
            if i not in unique:
                s.put(cur)
                s.put(i)
                unique.append(i)
                print(i.element)
                break

def DFS_recursion(visited, graph, node):
    if node in visited:
        return
    print(node.element)
    visited.append(node)
    for i in node.nexts:
        DFS_recursion(visited, graph, i)

graph1 = graph()
graph1.nodes = {"A": node("A"), "B": node("B"), "C": node("C"), "D": node("D"), "E": node("E")}
graph1.nodes["A"].nodes_in = 3
graph1.nodes["A"].nodes_out = 3
graph1.nodes["A"].nexts = [graph1.nodes["B"], graph1.nodes["C"], graph1.nodes["E"]]
graph1.nodes["A"].edges = [edge(graph1.nodes["A"],graph1.nodes["B"]),
                           edge(graph1.nodes["A"],graph1.nodes["C"]),
                           edge(graph1.nodes["A"],graph1.nodes["E"])]
graph1.nodes["B"].nodes_in = 2
graph1.nodes["B"].nodes_out = 2
graph1.nodes["B"].nexts = [graph1.nodes["A"], graph1.nodes["C"]]
graph1.nodes["B"].edges = [edge(graph1.nodes["A"],graph1.nodes["B"]),
                           edge(graph1.nodes["B"],graph1.nodes["C"])]
graph1.nodes["C"].nodes_in = 4
graph1.nodes["C"].nodes_out = 4
graph1.nodes["C"].nexts = [graph1.nodes["A"], graph1.nodes["B"], graph1.nodes["D"], graph1.nodes["E"]]
graph1.nodes["C"].edges = [edge(graph1.nodes["A"],graph1.nodes["C"]),
                           edge(graph1.nodes["B"],graph1.nodes["C"]),
                           edge(graph1.nodes["C"],graph1.nodes["D"]),
                           edge(graph1.nodes["C"],graph1.nodes["E"])]
graph1.nodes["D"].nodes_in = 2
graph1.nodes["D"].nodes_out = 2
graph1.nodes["D"].nexts = [graph1.nodes["C"], graph1.nodes["E"]]
graph1.nodes["D"].edges = [edge(graph1.nodes["C"],graph1.nodes["D"]),
                           edge(graph1.nodes["D"],graph1.nodes["E"])]
graph1.nodes["E"].nodes_in = 3
graph1.nodes["E"].nodes_out = 3
graph1.nodes["E"].nexts = [graph1.nodes["A"], graph1.nodes["C"], graph1.nodes["D"]]
graph1.nodes["E"].edges = [edge(graph1.nodes["A"],graph1.nodes["E"]),
                           edge(graph1.nodes["C"],graph1.nodes["E"]),
                           edge(graph1.nodes["D"],graph1.nodes["E"])]
graph1.edges = [edge(graph1.nodes["A"],graph1.nodes["B"]), edge(graph1.nodes["A"], graph1.nodes["C"]),
                edge(graph1.nodes["A"], graph1.nodes["E"]), edge(graph1.nodes["B"], graph1.nodes["C"]),
                edge(graph1.nodes["C"], graph1.nodes["D"]), edge(graph1.nodes["C"], graph1.nodes["E"]),
                edge(graph1.nodes["D"], graph1.nodes["E"])]

BFS(graph1.nodes["A"])
BFS(graph1.nodes["B"])
DFS(graph1.nodes["A"])
DFS(graph1.nodes["B"])
visited = []
DFS_recursion(visited, graph1, graph1.nodes["A"])

