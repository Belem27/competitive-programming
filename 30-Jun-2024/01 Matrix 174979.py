# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in xrange(len(mat)):
            for j in xrange(len(mat[i])):
                if not mat[i][j]:
                    continue
                mat[i][j] = float("inf")
                if i > 0:
                    mat[i][j] = min(mat[i][j], mat[i-1][j]+1)
                if j > 0:
                    mat[i][j] = min(mat[i][j], mat[i][j-1]+1)
        for i in reversed(xrange(len(mat))):
            for j in reversed(xrange(len(mat[i]))):
                if not mat[i][j]:
                    continue
                if i < len(mat)-1:
                    mat[i][j] = min(mat[i][j], mat[i+1][j]+1)
                if j < len(mat[i])-1:
                    mat[i][j] = min(mat[i][j], mat[i][j+1]+1)
        return mat