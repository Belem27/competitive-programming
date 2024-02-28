class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        d = collections.defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                d[i+j].append(mat[i][j])
        
        print(d)
        ans= []
        for entry in d.items():
            print(entry[1])
            if entry[0] % 2 == 0:
                ans.extend(entry[1][::-1])
            else:
                ans.extend(entry[1])
        return ans
                