import sys
sys.path.append('src')
from weighted_graph import WeightedGraph

weights = {
    (0,1): 3,
    (1,7): 4,
    (7,2): 2,
    (2,5): 1,
    (5,6): 8,
    (0,3): 2,
    (3,2): 6,
    (3,4): 1,
    (4,8): 8,
    (8,0): 4
}
#vertex_values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
#weighted_graph = WeightedGraph(weights, vertex_values)
weighted_graph = WeightedGraph(weights)

print('Does the weighted_graphs calc_distance work?')

assert weighted_graph.calc_distance(8,4) == 7, 'No'

assert [weighted_graph.calc_distance(8,n) for n in range(9)] == [4, 7, 12, 6, 7, 13, 21, 11, 0], 'Not with multiple'
print('Yes it does', "\n")
