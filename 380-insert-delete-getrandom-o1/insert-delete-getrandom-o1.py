class RandomizedSet(object):

    def __init__(self):
        self.hashmap = {}  # Dictionary to store values and their indices in the array
        self.array = []    # List to store values

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.hashmap:
            return False
        self.array.append(val)
        self.hashmap[val] = len(self.array) - 1
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.hashmap:
            return False
        index = self.hashmap[val]
        last_val = self.array[-1]
        self.array[index] = last_val
        self.hashmap[last_val] = index
        self.array.pop()
        del self.hashmap[val]
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.array)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()