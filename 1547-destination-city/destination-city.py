class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """

        return "".join(city for city in [paths[i][1] for i in range(len(paths))] if city not in [paths[i][0] for i in range(len(paths))])
