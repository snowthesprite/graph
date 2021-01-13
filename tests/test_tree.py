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
print()

edges = [('a','c'), ('e','g'), ('e','i'), ('e','a'), ('d','b'), ('a','d'), ('d','f'), ('f','h'), ('d','j'), ('d','k')]
tree = Tree(edges)
tree.build_from_edges()

print('Does nodes_breadth_first work?')
nodes = tree.nodes_breadth_first()
assert [node.value for node in nodes] == ['e','g','i','a','c','d','b','f','j','k','h'], 'No it doesnt'
print('Yes it does')
print()

print('Does nodes_depth_first work?')

nodes = tree.nodes_depth_first()

assert [node.value for node in nodes] == ['e','a','d','k','j','f','h','b','c','i','g'], 'No it doesnt'
print('Yes it does')
print()