from directed_graph import DirectedGraph

class Node :
    def __init__(self, given, node_values) :
        if type(given) == int :
            self.value = node_values[given]
            self.index = given
        else :
            self.value = given
            self.index = node_values.index(given)
        self.children = []

class Tree (DirectedGraph) :
    def __init__(self, edges, node_values) :
        self.node_vals = node_values
        self.edges = edges
        self.root = Node(self.get_root()[0], self.node_vals)
        self.nodes = [Node(index, self.node_vals) for index in range(len(self.node_vals)) if index != self.root.index]
        self.nodes.insert(0,self.root)
        self.build_from_edges()
        
    def get_root(self) :
        for pair in self.edges :
            check = self.get_parents(pair[0])
            if check == [] :
                return [pair[0]]

    def build_from_edges(self) :
        node_array = [self.root]
        while node_array != [] :
            for node in node_array :
                children = self.get_children(node.value)
                if children == [] :
                    children = self.get_children(node.index)
                child_array = [Node(child, self.node_vals) for child in children]
                node.children = child_array
            node_array = child_array
