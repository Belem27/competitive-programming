class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """

        for city in [paths[i][1] for i in range(len(paths))]:
            if city not in [paths[i][0] for i in range(len(paths))]:
                return city
