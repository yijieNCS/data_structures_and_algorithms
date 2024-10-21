from heap import Heap
import math

class Dijkstra:

    def __init__(self, graph, source, target):
        self.graph = graph
        self.source = source
        self.target = target

    def find_shortest_path(self):
        distance = {node: float('inf') for node in self.graph}
        visited = {node: False for node in self.graph}
        predecessor = {node: None for node in self.graph}
        
        distance[self.source] = 0

        current_node = self.source
        current_dist_travelled = 0

        while(True):

            if current_node == self.target:
                init_path = []
                shortest_path = self.construct_path(self.target, predecessor, init_path)
                shortest_distance = self.calculate_distance(distance, shortest_path)
                print(f"The shortest path is {shortest_path} and the distance to be travelled: {shortest_distance}")
                break

            visited[current_node] = True
            neighbors = self.graph[current_node]

            for node, dist in neighbors.items():
                tentative_dist = current_dist_travelled + dist

                if visited[node] == False and tentative_dist < distance[node]:
                    distance[node] = tentative_dist
                    predecessor[node] = current_node

            # No Min Heap so complexity high
            # Implement next time
            # shortest_node = ''
            # shortest_dist = float('inf')
            # for k, v in distance.items():
            #    if shortest_dist > v and visited[k] == False:
            #        shortest_node = k
            #        shortest_dist = v
            # current_node = shortest_node

            #################################
            heap = Heap({key: value for key, value in distance.items() if not (math.isinf(value) or value == 0) and visited.get(key) is False}).buildMinHeap()
            current_node = list(heap.keys())[0]

    def construct_path(self, target, predecessor, init_path):
        path = [] + init_path
        if predecessor[target] is None:
            path.append(target)
            path.reverse()
            return path
        else:
            path.append(target)
            target = predecessor[target]
            return self.construct_path(target, predecessor, path)
        
    def calculate_distance(self, dist, path):
        total_dist = 0
        for p in path:
            total_dist += dist[p]

        return total_dist