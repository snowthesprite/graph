class Node :
    def __init__(self, index) :
        self.index = index
        self.neighbors = []

class Graph :
    def __init__(self, edges) :
        self.edges = edges
    
    def find_neighbors(self, home) :
        neighbors = []
        for pair in self.edges: 
            if pair[0] == home :
                neighbors.append(pair[1])
            elif pair[1] == home :
                neighbors.append(pair[0])
        return neighbors

    def get_nodes_breadth_first(self, start) : 
        queue = [start]
        sorted_queue = []
        while queue != [] :
            sorted_queue.append(queue[0])
            neighbors = self.find_neighbors(queue[0])
            for neighbor in neighbors :
                if neighbor not in queue and neighbor not in sorted_queue :
                    queue.append(neighbor)
            queue.pop(0)
        return [Node(index) for index in sorted_queue]

    def get_nodes_depth_first(self, start) : 
        stack = [start]
        sorted_stack = []
        while stack != [] :
            current_index = len(stack) - 1
            sorted_stack.append(stack[current_index])
            neighbors = self.find_neighbors(stack[current_index])
            stack.pop(current_index)
            for neighbor in neighbors :
                if neighbor not in stack and neighbor not in sorted_stack :
                    stack.append(neighbor)
        return [Node(index) for index in sorted_stack]