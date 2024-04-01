class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        s = [paths[i][0] for i in range(len(paths))]
        d = [paths[i][1] for i in range(len(paths))]

        for city in d:
            if city not in s:
                return city
