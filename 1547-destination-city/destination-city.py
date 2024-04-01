class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        path_count = {}

        for path in paths:
            path_a, path_b = path
            path_count[path_a] = path_count.get(path_a, 0) + 1
            path_count[path_b] = path_count.get(path_b, 0)

        for city in path_count:
            if path_count[city] == 0:
                return city