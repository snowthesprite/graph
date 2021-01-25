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

    def get_children(self, parent, tree_list) :
        children = []
        for pair in tree_list: 
            if pair[0] == parent :
                children.append(pair[1])
        return children

    def get_parents(self, child, tree_list) :
        parents = []
        for pair in tree_list :
            if pair[1] == child :
                parents.append(pair[0])
        return parents

    def get_root(self, tree_list) :
        for pair in tree_list :
            for parent_child in pair :
                check = self.get_parents(parent_child, tree_list)
                if check == [] :
                    return [parent_child]

    def build_from_edges(self) :
        node_array = [self.root]
        while node_array != [] :
            child_array = []
            for node in node_array :
                node_child_array = []
                children = self.get_children(node.value, self.edges)
                if children == [] :
                    children = self.get_children(node.index, self.edges)
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
