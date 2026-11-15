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

        q = deque() 
        q.append(root)
        counter = 1 # how many in the layer 
        res = []
        temp_res = []

        while q: 

            while counter > 0 and q: 

                # for each layer

                _node = q.popleft()

                temp_res.append(_node.val)

                if _node.left: 
                    q.append(_node.left)
                if _node.right:
                    q.append(_node.right)

                counter -= 1 
            res.append(temp_res)
            temp_res = []
            counter = len(q)

        return res 


