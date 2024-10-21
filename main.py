from astar.astar import Astar

astar = Astar({
    'A': {'B': 4, 'C': 1, 'D': 3},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 8, 'E': 10},
    'D': {'E': 2},
    'E': {}
}, 'A', 'D')

astar.compute_heuristics()