class Node :
    def __init__(self, data) :
        self.value = data
        self.children = []

class Tree :
    def __init__(self, edges) :
        self.root = Node(self.get_root(edges)[0])
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
                    return list(parent_child)

    def build_from_edges(self) :
        node_array = [self.root]
        while node_array != [] :
            child_array = []
            for node in node_array :
                node_child_array = []
                children = self.get_children(node.value, self.edges)
                for child in children :
                    child_array.append(Node(child))
                    node_child_array.append(Node(child))
                node.children = node_child_array
            node_array = node_child_array