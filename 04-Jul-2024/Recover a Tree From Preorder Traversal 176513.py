# Problem: Recover a Tree From Preorder Traversal - https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverFromPreorder(self, traversal):
        """
        :type traversal: str
        :rtype: TreeNode
        """
        def recoverFromPreorderHelper(traversal, level, i):
            j = i[0]
            while j < len(traversal) and traversal[j] == '-':
                j += 1 
            if level != j - i[0]:
                return None
            i[0] = j
            while j < len(traversal) and traversal[j] != '-':
                j += 1
            node = TreeNode(int(traversal[i[0]:j]))
            i[0] = j
            node.left = recoverFromPreorderHelper(traversal, level+1, i)
            node.right = recoverFromPreorderHelper(traversal, level+1, i)
            return node

        return recoverFromPreorderHelper(traversal, 0, [0])