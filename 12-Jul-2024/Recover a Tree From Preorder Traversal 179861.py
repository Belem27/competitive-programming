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
        def recoverFromPreorderHelper(S, level, i):
            j = i[0]
            while j < len(S) and S[j] == '-':
                j += 1 
            if level != j - i[0]:
                return None
            i[0] = j
            while j < len(S) and S[j] != '-':
                j += 1
            node = TreeNode(int(S[i[0]:j]))
            i[0] = j
            node.left = recoverFromPreorderHelper(S, level+1, i)
            node.right = recoverFromPreorderHelper(S, level+1, i)
            return node

        return recoverFromPreorderHelper(traversal, 0, [0])