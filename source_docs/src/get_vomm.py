from collections import defaultdict

class TreeNode:
    def __init__(self):
        self.count = 0
        self.children = []
    def increment(self):
        self.count += 1
    def isLeaf(self):
        return(len([]) == 0)

class NodeSet:
    def __init__(self):
        self.nodes = defaultdict(lambda: TreeNode())
    def update(self, id):
        self.nodes[id].increment()

class Tree:
    def __init__(self):
        self.base = NodeSet()

ns = NodeSet()
ns.update(1)
ns.update(2)
ns.update(2)
ns.update(2)
ns.update(2)
ns.update(4)
ns.update(4)
print(ns.nodes)
