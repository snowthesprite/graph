import sys
sys.path.append('src')
from tree import Tree

edges = [('a','c'), ('e','g'), ('e','i'), ('e','a'), ('g','b'), ('a','d'), ('d','f'), ('f','h'), ('d','j'), ('c','k')]

tree = Tree(edges)

tree.build_from_edges()
''''
>>> tree.root.value
'e'

>>> [node.value for node in tree.root.children]
['a', 'i', 'g']

# you may need to change the output of this test (and future tests)
# for example, if you have ['g', 'i', 'a'], then that's fine

>>> [node.value for node in tree.root.children[0].children] # children of a
['c', 'd']

# you may need to change the output of this test (and future tests)
# for example, if you had ['g', 'i', 'a'] earlier, then the 
# output would be the children of 'g', which is just ['b']

>>> [node.value for node in tree.root.children[1].children] # children of i
[]

>>> [node.value for node in tree.root.children[2].children] # children of g
['b']

>>> [node.value for node in tree.root.children[0].children[0].children] # children of c
['k']

>>> [node.value for node in tree.root.children[0].children[1].children] # children of d
['j', 'f']

>>> [node.value for node in tree.root.children[2].children[0].children] # children of b
[]

>>> [node.value for node in tree.root.children[0].children[0].children[0].children] # children of k
[]

>>> [node.value for node in tree.root.children[0].children[1].children[0].children] # children of j
[]

>>> [node.value for node in tree.root.children[0].children[1].children[1].children] # children of f
['h']

>>> [node.value for node in tree.root.children[0].children[1].children[1].children[0].children] # children of f
[]
'''