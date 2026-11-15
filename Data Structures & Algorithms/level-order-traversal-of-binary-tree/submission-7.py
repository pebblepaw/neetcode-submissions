# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root: 
            return [] 

        q = deque([root])
        res = []

        while q: 

            temp_res = []

            for i in range(len(q)): # for this level 
            
                _node = q.popleft()
                temp_res.append(_node.val)

                if _node.left: 
                    q.append(_node.left)
                if _node.right:
                    q.append(_node.right)

            res.append(temp_res)

        return res 


