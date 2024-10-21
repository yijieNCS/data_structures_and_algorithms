import random

class Astar:

    def __init__(self, graph, source, target) -> None:
        self.graph = graph
        self.source = source
        self.target = target
        self.f_costs = {}
        self.h_costs = {}

    def compute_heuristics(self):
        # Compute from each node to the goal node
        # Random Generation for now and save into a dictionary

        nodes = list(self.graph.keys())

        for node in nodes:
            if node == self.target:
                self.h_costs[node] = 0
            else:
                self.h_costs[node] = random.randint(0, 10)

        print("The generated heuristics: ", self.h_costs)

    def find_shortest_path(self):
        for k, v in self.h_costs.items():
            self.f_costs[k] = v
        
        g_costs = {node: float('inf') for node in self.graph}
        visited = {node: False for node in self.graph}
        predecessor = {node: None for node in self.graph}
