# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:


        if not root: 
            return root

        q = deque()

        q.append(root)

        while q: 

            # for every single node
            _node = q.popleft() 
            
            # rotate left and right
            temp = _node.left
            _node.left = _node.right
            _node.right = temp # left 
            
            if _node.left: 
                q.append(_node.left) 
            if _node.right: 
                q.append(_node.right)

        return root 

    