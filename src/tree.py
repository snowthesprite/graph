class Node :
    def __init__(self, given, node_values) :
        if type(given) == int :
            self.value = node_values[given]
            self.index = given
        else :
            self.value = given
            self.index = node_values.index(given)
        self.children = []

class Tree :
    def __init__(self, edges, node_values) :
        self.node_vals = node_values
        self.root = Node(self.get_root(edges)[0], self.node_vals)
        self.edges = edges

    def get_children(self, parent) :
        return [kid for (guardian, kid) in self.edges if guardian == parent]

    def get_parents(self, child) :
        return [guardian for (guardian, kid) in self.edges if kid == child]

    def get_root(self, tree_list) :
        for pair in tree_list :
            check = self.get_parents(pair[0])
            if check == [] :
                return [pair[0]]

    def build_from_edges(self) :
        node_array = [self.root]
        while node_array != [] :
            child_array = []
            for node in node_array :
                node_child_array = []
                children = self.get_children(node.value)
                if children == [] :
                    children = self.get_children(node.index)
                for child in children :
                    child_array.append(Node(child, self.node_vals))
                    node_child_array.append(Node(child, self.node_vals))
                node.children = node_child_array
            node_array = node_child_array

    def nodes_breadth_first(self) : 
        queue = [self.root]
        sorted_nodes = []
        while queue != [] :
            sorted_nodes.append(queue[0])
            children = queue[0].children
            for child in children :
                queue.append(child)
            queue.pop(0)
        return sorted_nodes

    def nodes_depth_first(self) : 
        stack = [self.root]
        sorted_nodes = []
        while stack != [] :
            sorted_nodes.append(stack[len(stack) - 1])
            children = stack[len(stack) -1].children
            stack.pop(len(stack) - 1)
            for child in children :
                stack.append(child)
        return sorted_nodes
