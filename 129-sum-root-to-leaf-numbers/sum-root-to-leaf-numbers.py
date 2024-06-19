# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, curr):
            if not node:
                return 0
            
            curr = curr * 10 + node.val

            if not node.left and not node.right:
                return curr

            l_sum = dfs(node.left, curr)
            r_sum = dfs(node.right, curr)
            
            return l_sum + r_sum
        
        return dfs(root, 0)        