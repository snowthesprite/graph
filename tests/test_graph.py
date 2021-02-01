import sys
sys.path.append('src')
from graph import Graph

edges = [(0,1),(1,2),(1,3),(3,4),(1,4),(4,5)]
graph = Graph(edges)

bf = graph.get_nodes_breadth_first(2)

df = graph.get_nodes_depth_first(2)

print('Does our general graphs get nodes breadth first and get nodes depth first work?')

assert [node.index for node in bf] == [2, 1, 0, 3, 4, 5], 'Breadth first does not work'


assert [node.index for node in df] == [2, 1, 4, 5, 3, 0], 'Depth first does not work'

print('Yes they do!')