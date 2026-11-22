"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node: 
            return node

        # hash map 
        oldtonew = {}

        def dfs(node):

            copy = Node(node.val)
            oldtonew[node] = copy 
            
            for n in node.neighbors: 

                # check if it's in our map
                if n in oldtonew: 
                    copy.neighbors.append(oldtonew[n])
                else: 
                    copy.neighbors.append(dfs(n))
            return copy

        return dfs(node) 