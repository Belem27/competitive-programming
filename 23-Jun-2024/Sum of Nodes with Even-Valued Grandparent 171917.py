# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        soln = {"ans": 0}
        def dfs(current, parent, grand):
            if not current:
                return None
            
            if grand and grand.val % 2 == 0:
                soln["ans"] += current.val

            dfs(current.left, current, parent)
            dfs(current.right, current, parent)
        
        dfs(root, None, None)
        return soln["ans"]