# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxDepth(self, root):
            if root is None:
                return 0
            else:
                return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        return maxDepth(self, root)