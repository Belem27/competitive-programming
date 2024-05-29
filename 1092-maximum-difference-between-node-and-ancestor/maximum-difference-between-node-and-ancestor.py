# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxAncestorDiffHelper(node, mx, mn): 
            if not node:
                return 0
            res = max(mx-node.val, node.val-mn)
            mx = max(mx, node.val)
            mn = min(mn, node.val)
            res = max(res, maxAncestorDiffHelper(node.left, mx, mn))
            res = max(res, maxAncestorDiffHelper(node.right, mx, mn))
            return res

        return maxAncestorDiffHelper(root, 0, float("inf"))