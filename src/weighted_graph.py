from graph import *

class Node :
    def __init__(self, index, node_name) :
        self.index = index
        self.dvalues = node_name[self.index]
        self.neighbors = None
        self.distance = 9999

class WeightedGraph (Graph) :
    def __init__(self, weights, vertex_vals) :
        self.weights = weights
        self.v_vals = vertex_vals
        self.edges = list(self.weights.keys())
        max = 0
        for pair in self.edges :
            if pair[0] > max :
                max = pair[0]
            elif pair[1] > max :
                max = pair[1]
        self.nodes = [Node(index, self.v_vals) for index in range(max + 1)]
        self.build_from_edges()

    def set_breadth_first_distance_and_previous(self, starting_node_index) :
        node_order = self.get_nodes_breadth_first(starting_node_index)
        current_node = self.nodes[node_order[0].index]
        current_node.distance = 0
        for index in range(1, len(node_order)) :
            current_index = current_node.index
            for neighbor in current_node.neighbors :
                neigh_index = neighbor.index
                if (current_index, neigh_index) in self.edges :
                    weight = self.weights[(current_index, neigh_index)]
                else :
                    weight = self.weights[(neigh_index, current_index)]
                if current_node.distance + weight < neighbor.distance :
                    self.nodes[neigh_index].distance = current_node.distance + weight
            current_node = self.nodes[node_order[index].index]