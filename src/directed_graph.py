class Node :
    def __init__(self, index) :
        self.index = index
        self.distance = 0
        self.children = []
        self.parents = []

class DirectedGraph :
    def __init__(self, edges) :
        self.edges = edges
        max = 0
        for pair in self.edges :
            if pair[0] > max :
                max = pair[0]
            elif pair[1] > max :
                max = pair[1]
        self.nodes = [Node(index) for index in range(max + 1)]
        self.build_from_edges()

    def get_children(self, parent) :
        return [pair[1] for pair in self.edges if pair[0] == parent]

    def get_parents(self, child) :
        return [pair[0] for pair in self.edges if pair[1] == child]

    def build_from_edges(self) :
        for node in self.nodes :
            children = self.get_children(node.index)
            parents = self.get_parents(node.index) 
            node.parents = [self.nodes[parent_index] for parent_index in parents]
            node.children = [self.nodes[child_index] for child_index in children]
    
    def nodes_breadth_first(self,start) : 
        queue = [self.nodes[start]]
        sorted_nodes = []
        while queue != [] :
            sorted_nodes.append(queue[0])
            children = queue[0].children
            for child in children :
                if child.index not in [node.index for node in sorted_nodes] :
                    queue.append(child)
            queue.pop(0)
        return sorted_nodes

    def nodes_depth_first(self,start) : 
        stack = [self.nodes[start]]
        sorted_nodes = []
        while stack != [] :
            sorted_nodes.append(stack[len(stack) - 1])
            children = stack[len(stack) -1].children
            stack.pop(len(stack) - 1)
            for child in children :
                if child.index not in [node.index for node in sorted_nodes] :
                    stack.append(child)
        return sorted_nodes

    def set_breadth_first_distance(self, starting_node_index) :
        node_order = self.nodes_breadth_first(starting_node_index)
        current_node = self.nodes[node_order[0].index]
        visited = [current_node.index]
        current_node.distance = 0
        for index in range(1, len(node_order)) :
            for child in current_node.children :
                if child.index not in visited :
                    self.nodes[child.index].distance = current_node.distance + 1
                    visited.append(child.index)
            current_node = self.nodes[node_order[index].index]

    def calc_distance(self, starting_node_index, ending_node_index) :
        if self.nodes[starting_node_index].children == [] :
            return False
        self.set_breadth_first_distance(starting_node_index)
        return self.nodes[ending_node_index].distance

    def calc_shortest_path(self, starting_node_index, ending_node_index) :
        if self.nodes[starting_node_index].children == [] :
            return False
        self.set_breadth_first_distance(starting_node_index)
        current_node = self.nodes[ending_node_index] 
        short_path = []
        while True :
            short_path.append(current_node.index)
            if current_node.index == starting_node_index :
                break
            for parent in current_node.parents :
                if parent.distance == current_node.distance - 1 :
                    current_node = self.nodes[parent.index]
                elif parent.distance == current_node.distance :
                    current_node = self.nodes[starting_node_index]
        short_path.reverse()
        return short_path