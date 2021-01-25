import sys
sys.path.append('src')
from tree import Tree

node_values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']

edges = [('a','c'), ('e','g'), ('e','i'), ('e','a'), ('g','b'), ('a','d'), ('d','f'), ('f','h'), ('d','j'), ('c','k')]

tree = Tree(edges, node_values)

tree.build_from_edges()

print('Does all this work?')

assert tree.root.value == 'e'

assert set(node.value for node in tree.root.children) == {'g', 'i', 'a'}


assert set(node.value for node in tree.root.children[0].children) == {'b'}

assert [node.value for node in tree.root.children[1].children] == []

assert set(node.value for node in tree.root.children[2].children) == {'c', 'd'}

assert set(node.value for node in tree.root.children[2].children[0].children) == {'k'}

assert set(node.value for node in tree.root.children[2].children[1].children) == {'f', 'j'}

assert [node.value for node in tree.root.children[0].children[0].children] == []

assert [node.value for node in tree.root.children[2].children[0].children[0].children] == []

assert [node.value for node in tree.root.children[2].children[1].children[1].children] == []

assert set(node.value for node in tree.root.children[2].children[1].children[0].children) == {'h'}

assert [node.value for node in tree.root.children[2].children[1].children[0].children[0].children] == []

print('Looks like it!')
print()

edges = [('a','c'), ('e','g'), ('e','i'), ('e','a'), ('d','b'), ('a','d'), ('d','f'), ('f','h'), ('d','j'), ('d','k')]
tree = Tree(edges, node_values)
tree.build_from_edges()

print('Does nodes_breadth_first work?')
nodes = tree.nodes_breadth_first()
assert set(node.value for node in nodes) == {'e','g','i','a','c','d','b','f','j','k','h'}, 'No it doesnt'
print('Yes it does')
print()

print('Does nodes_depth_first work?')

nodes = tree.nodes_depth_first()

assert set(node.value for node in nodes) == {'e','a','d','k','j','f','h','b','c','i','g'}, 'No it doesnt'
print('Yes it does')
print()

node_values = ['a', 'b', 'a', 'a', 'a', 'b', 'a', 'b', 'a', 'b', 'b']

edges = [(0,2), (4,6), (4,8), (4,0), (3,1), (0,3), (3,5), (5,7), (3,9), (3,10)]

tree = Tree(edges, node_values)
tree.build_from_edges()

print('Is the root node correct?')

assert tree.root.value == 'a', 'The value isnt quite right'
assert tree.root.index == 4, 'The index isnt quite right'

print('Yes')
print()

children = set(tree.root.children)

grandchildren = set([])
for child in children:
    grandchildren = grandchildren.union(set(child.children))

great_grandchildren = set([])
for grandchild in grandchildren:
    great_grandchildren = great_grandchildren.union(set(grandchild.children))

great_great_grandchildren = set([])
for great_grandchild in great_grandchildren:
    great_great_grandchildren = great_great_grandchildren.union(set(great_grandchild.children))

print('Are the children, grandchildren great grandchild, and great great grandchildren correct')
assert {node.index for node in children} == {0, 8, 6}, 'children indicies are not quite right'
assert {node.value for node in children} == {'a', 'a', 'a'}, 'children values are not quite right'

assert {node.index for node in grandchildren} == {2, 3}, 'grandchildren indicies are not quite right'
assert {node.value for node in grandchildren} == {'a', 'a'}, 'grandchildren values are not quite right'

assert {node.index for node in great_grandchildren} == {1, 9, 5, 10}, 'great grandchildren indicies are not quite right'
assert {node.value for node in great_grandchildren} == {'b', 'b', 'b', 'b'}, 'great grandchildren values are not quite right'

assert {node.index for node in great_great_grandchildren} == {7}, 'great great grandchildren indicies are not quite right'
assert {node.value for node in great_great_grandchildren} == {'b'}, 'great great grandchildren values are not quite right'

print('Yes')
print()