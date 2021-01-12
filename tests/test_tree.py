import sys
sys.path.append('src')
from tree import Tree

edges = [('a','c'), ('e','g'), ('e','i'), ('e','a'), ('g','b'), ('a','d'), ('d','f'), ('f','h'), ('d','j'), ('c','k')]

tree = Tree(edges)

tree.build_from_edges()

print('Does all this work?')

assert tree.root.value == 'e'

assert [node.value for node in tree.root.children] == ['g', 'i', 'a']


assert [node.value for node in tree.root.children[0].children] == ['b']

assert [node.value for node in tree.root.children[1].children] == []

assert [node.value for node in tree.root.children[2].children] == ['c', 'd']

assert [node.value for node in tree.root.children[2].children[0].children] == ['k']

assert [node.value for node in tree.root.children[2].children[1].children] == ['f', 'j']

assert [node.value for node in tree.root.children[0].children[0].children] == []

assert [node.value for node in tree.root.children[2].children[0].children[0].children] == []

assert [node.value for node in tree.root.children[2].children[1].children[1].children] == []

assert [node.value for node in tree.root.children[2].children[1].children[0].children] == ['h']

assert [node.value for node in tree.root.children[2].children[1].children[0].children[0].children] == []

print('Looks like it!')

edges = [('a','c'), ('e','g'), ('e','i'), ('e','a'), ('d','b'), ('a','d'), ('d','f'), ('f','h'), ('d','j'), ('d','k')]
tree = Tree(edges)
tree.build_from_edges()

print('Printing the tree going by breadth')

tree.print_breadth_first()
print()

print('Printing the tree going by depth')

tree.print_depth_first()
print()