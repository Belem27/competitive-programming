# Problem: N Queens - https://leetcode.com/problems/n-queens/

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        col = set()
        p_diag = set()
        n_diag = set()
        res = []
        board = [["."]*n for _ in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r+c) in p_diag or (r-c) in n_diag:
                    continue
                col.add(c)
                p_diag.add(r+c)
                n_diag.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                col.remove(c)
                p_diag.remove(r+c)
                n_diag.remove(r-c)
                board[r][c] = "."

        backtrack(0)
        return res