class Node :
    def __init__(self, index) :
        self.index = index
        self.neighbors = None
        self.distance = 0
        self.previous = None

class Graph :
    def __init__(self, edges) :
        self.edges = edges
        indicies = []
        for (a,b) in self.edges :
            indicies.extend([a,b])
        self.nodes = [Node(index) for index in range(max(indicies) + 1)]
        self.build_from_edges()
    
    def find_neighbors(self, home) :
        neighbors = []
        for (neigh_0, neigh_1) in self.edges: 
            if neigh_0 == home :
                neighbors.append(neigh_1)
            elif neigh_1 == home :
                neighbors.append(neigh_0)
        return neighbors

    def build_from_edges(self) :
        for node in self.nodes :
            neighbors = self.find_neighbors(node.index)
            node_neighbors = [self.nodes[neigh_index] for neigh_index in neighbors]
            node.neighbors = node_neighbors

    def get_nodes_breadth_first(self, start) : 
        queue = [start]
        sorted_queue = []
        while queue != [] :
            q_index = queue[0]
            sorted_queue.append(q_index)
            neighbors = self.nodes[q_index].neighbors
            for neighbor in neighbors :
                if neighbor.index not in queue and neighbor.index not in sorted_queue :
                    queue.append(neighbor.index)
            queue.remove(q_index)
        return [self.nodes[sorted] for sorted in sorted_queue]

    def get_nodes_depth_first(self, start) : 
        stack = [start]
        sorted_stack = []
        while stack != [] :
            s_index = stack[len(stack) - 1]
            sorted_stack.append(s_index)
            neighbors = self.nodes[s_index].neighbors
            for neighbor in neighbors :
                if neighbor.index not in stack and neighbor.index not in sorted_stack :
                    stack.append(neighbor.index)
            stack.remove(s_index)
        return [self.nodes[sorted] for sorted in sorted_stack]

    def set_breadth_first_distance_and_previous(self, starting_node_index) :
        node_order = self.get_nodes_breadth_first(starting_node_index)
        current_node = self.nodes[node_order[0].index]
        current_node.distance = 0
        current_node.previous = None
        for index in range(1,len(node_order)) :
            for neighbor in current_node.neighbors :
                neigh_index = neighbor.index
                if current_node.previous == None or neighbor.previous != current_node.previous and neigh_index != current_node.previous.index :
                    self.nodes[neigh_index].previous = current_node
                    self.nodes[neigh_index].distance = current_node.distance + 1
            current_node = self.nodes[node_order[index].index]

    def calc_distance(self, starting_node_index, ending_node_index) :
        self.set_breadth_first_distance_and_previous(starting_node_index)
        return self.nodes[ending_node_index].distance

    def calc_shortest_path(self, starting_node_index, ending_node_index) :
        self.set_breadth_first_distance_and_previous(starting_node_index)
        current_node = self.nodes[ending_node_index] 
        short_path = []
        while True :
            short_path.append(current_node.index)
            if current_node.index == starting_node_index :
                break
            current_node = current_node.previous
        short_path.reverse()
        return short_path