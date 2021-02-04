class Node :
    def __init__(self, index) :
        self.index = index
        self.neighbors = None
        self.distance = 0
        self.previous = None

class Graph :
    def __init__(self, edges) :
        self.edges = edges
        nodes = self.build_from_edges()
        self.nodes = [0 for _ in range(len(nodes))]
        for node in nodes :
            self.nodes[node.index] = node
    
    def find_neighbors(self, home) :
        neighbors = []
        for pair in self.edges: 
            if pair[0] == home :
                neighbors.append(pair[1])
            elif pair[1] == home :
                neighbors.append(pair[0])
        return neighbors

    def build_from_edges(self) :
        node_array = [Node(self.edges[0][0])]
        visited = []
        while node_array != [] :
            for node in node_array :
                visited.append(node)
                neighbors = self.find_neighbors(node.index)
                node_neighbors = [Node(neighbor) for neighbor in neighbors]
                node.neighbors = node_neighbors
            node_array = [neighbor for neighbor in node_neighbors if neighbor.index not in [visit.index for visit in visited]]
        return visited

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
        current_node = node_order[0]
        current_node.distance = 0
        index = 1
        while index < len(node_order) :
            next_node = node_order[index]
            for neighbor in next_node.neighbors :
                if neighbor.distance != current_node.distance + 1 and neighbor.index != current_node.index:
                    print(neighbor.index, current_node.index, next_node.index)
                    next_node.previous = current_node
                    next_node.distance = current_node.distance + 1
            current_node = next_node
            index += 1

    def calc_distance(self, starting_node_index, ending_node_index) :
        self.set_breadth_first_distance_and_previous(starting_node_index)
        return self.nodes[ending_node_index].distance