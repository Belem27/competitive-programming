# Problem: Path Sum III - https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        def pathSumHelper(root, curr, targetSum, lookup):
            if root is None:
                return 0
            curr += root.val
            print(curr)
            print(targetSum)
            if curr-targetSum in lookup:
                result = lookup[curr-targetSum]
            else:
                result = 0
            lookup[curr] += 1
            result += pathSumHelper(root.left, curr, targetSum, lookup) + \
                      pathSumHelper(root.right, curr, targetSum, lookup)
            lookup[curr] -= 1
            if lookup[curr] == 0:
                del lookup[curr]
            return result

        lookup = collections.defaultdict(int)
        lookup[0] = 1
        return pathSumHelper(root, 0, targetSum, lookup)