class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(mat)):
            res = res + mat[i][i] + mat[i][~i]

        if (len(mat)) % 2:
            mid = len(mat)//2
            res -= mat[mid][mid]
        
        return res