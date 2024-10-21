import math

class Heap():

    def __init__(self, dict):
        self.dict = dict
        self.nodes = list(self.dict.keys())

        print("The dict: ", self.dict)
        print("The noodes: ", self.nodes)

    def buildMinHeap(self):
        n = len(self.dict)
        for i in range(math.floor(n // 2 - 1), -1, -1):
            self.minHeapify(self.dict, self.nodes, i, n)

        print(f"The order of the nodes should be {self.nodes}")

        new_dict = {}
        for node in self.nodes:
            if node in self.dict:
                new_dict[node] = self.dict[node]

        print(f"New reordered dictionary: {new_dict}")
        return new_dict

    def minHeapify(self, dict, nodes, i, n):
        
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if (left < n) and (dict[nodes[left]] < dict[nodes[smallest]]):
            smallest = left

        if (right < n) and (dict[nodes[right]] < dict[nodes[smallest]]):
            smallest = right

        if smallest != i:
            nodes[i], nodes[smallest] = nodes[smallest], nodes[i]
            self.minHeapify(dict, nodes, smallest, n)
        else:
            return