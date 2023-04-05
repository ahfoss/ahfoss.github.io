from collections import defaultdict
from random import random, choices
import heapq
from operator import itemgetter

class TreeNode:
    def __init__(self):
        self.nodeCount = 0
        self.childEdges = EdgeMap()
    # Increment this node, and propagate update down to child.
    def increment(self, idlist):
        self.nodeCount += 1
        if len(idlist) > 1:
            self.childEdges.updateNode(idlist[:-1])
    def isLeaf(self):
        return(self.childEdges.len() == 0)
    def getLeafCount(self, idlist):
        # If is leaf, return count. Else, recurse down child.
        # May need to change to dict, and control behavior when unknown
        # key is queried.
        if self.isLeaf() or (len(idlist) == 0):
            return(self.nodeCount)
        else:
            return(self.childEdges.nodes[idlist[-1]].getLeafCount(idlist[:-1]))
    def print(self, depth):
        print(':', self.nodeCount)
        self.childEdges.print(depth + 1)

# A set of edges emanating from a node.
class EdgeMap:
    def __init__(self):
        self.nodes = defaultdict(lambda: TreeNode())
    # Update the relevant node.
    def updateNode(self, idlist):
        id = idlist[-1]
        self.nodes[id].increment(idlist)
    def len(self):
        return(len(self.nodes))
    def print(self, depth):
        for k,v in self.nodes.items():
            ch1 = '  '
            ch2 = '-'
            prefix = ch1 * (depth-1)
            if depth > 0:
                prefix += ch2
            print(prefix, k, sep = '', end = '')
            v.print(depth)

class Tree:
    def __init__(self):
        self.base = EdgeMap()
    def update(self, idlist):
        idlist = list(idlist) # Cleans up strings. Leaves lists unchanged.
        self.base.updateNode(idlist)
    def predictNext(self, idlist):
        idlist = list(idlist) # Cleans up strings. Leaves lists unchanged.
        outchar = []
        outcount = []
        total = 0
        for k,v in self.base.nodes.items():
            outchar.append(k)
            tmp = v.getLeafCount(idlist)
            outcount.append(tmp)
            total += tmp
        # Normalize counts into probs.
        if total == 0:
            return([' '], [1])
        else:
            outcount = [x / total for x in outcount]
        return(outchar, outcount)
    def sample(self, idlist, topk = 999):
        '''
        topk: Int The available choices will be limited to (at most) the
              topk most common choices.
        '''
        chars, probs = self.predictNext(idlist)
        if topk >= len(chars):
            return(choices(chars, probs))
        else:
            i_val = heapq.nlargest(topk, enumerate(probs), key=itemgetter(1))
            i_val_char = [(x[0],x[1],chars[x[0]]) for x in i_val]
            probs = [val for (i, val, _) in sorted(i_val_char)]
            chars = [val for (i, _, val) in sorted(i_val_char)]
        return(choices(chars, probs))
    def babble(self, idlist, nchar, contextLength, topk = 999):
        '''
        topk: Int The available choices will be limited to (at most) the
              topk most common choices.
        '''
        currId = list(idlist)
        outstr = ''
        for _ in range(nchar):
            thisChar = self.sample(currId, topk = topk)
            outstr += thisChar[0]
            currId = currId[1:] + thisChar
        return(outstr)
    def print(self):
        self.base.print(0)

if __name__ == "__main__":
    t1 = Tree()
    t1.update('abc')
    t1.update('bbc')
    t1.update('abd')
    t1.update('abd')
    t1.update('abd')
    t1.print()
    c1, p1 = t1.predictNext('ab')
    print("t1.predictNext('ab')")
    print(t1.predictNext('ab'))
    assert c1 == ['c','d']
    assert p1 == [0.25, 0.75]
    print("t1.sample('ab')")
    print(t1.sample('ab'))
