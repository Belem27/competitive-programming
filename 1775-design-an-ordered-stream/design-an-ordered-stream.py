class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.stream = [None] * n  # Initialize an array to store values
        self.ptr = 0  # Pointer to the next empty slot

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        # Insert the value into the stream at the appropriate index
        self.stream[idKey - 1] = value
        chunk = []
        # Collect all non-null values starting from ptr
        while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
            chunk.append(self.stream[self.ptr])
            self.ptr += 1
        return chunk
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)