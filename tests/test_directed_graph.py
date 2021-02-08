import sys
sys.path.append('src')
from directed_graph import DirectedGraph

edges = [(0,1),(1,2),(3,1),(4,3),(1,4),(4,5),(3,6)]

directed_graph = DirectedGraph(edges)

#print([[parent.index for parent in node.parents] for node in directed_graph.nodes])

assert [[child.index for child in node.children] for node in directed_graph.nodes] == [[1], [2,4], [], [1,6], [3,5], [], []]

assert [[parent.index for parent in node.parents] for node in directed_graph.nodes] == [[], [0,3], [1], [4], [1], [4], [3]]

print([node.index for node in directed_graph.nodes_breadth_first(4)])

print([node.index for node in directed_graph.nodes_depth_first(4)])

print()

print([node.index for node in directed_graph.get_nodes_breadth_first(4)])

print([node.index for node in directed_graph.get_nodes_depth_first(4)])

#assert [node.index for node in directed_graph.nodes_breadth_first(4)] == [4, 3, 5, 6, 1, 2]

#assert [node.index for node in directed_graph.nodes_depth_first(4)] == [4, 3, 6, 1, 2, 5]