# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        val = root.val
        queue = deque([root])
        while queue:
            visited = queue.popleft()
            if visited.val != val:
                return False
            if visited.left:
                queue.append(visited.left)
            if visited.right:
                queue.append(visited.right)
        return True
