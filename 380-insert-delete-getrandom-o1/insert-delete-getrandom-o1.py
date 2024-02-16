class RandomizedSet(object):

    def __init__(self):
        self.hashmap = set()

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.hashmap:
            return False
        self.hashmap.add(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.hashmap:
            return False
        self.hashmap.remove(val)
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(list(self.hashmap))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()