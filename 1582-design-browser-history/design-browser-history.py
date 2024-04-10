class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.history = [homepage]
        self.curr_idx = 0
    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.curr_idx += 1
        self.history = self.history[:self.curr_idx]
        self.history.append(url)

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.curr_idx = max(0, self.curr_idx - steps)
        return self.history[self.curr_idx]

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.curr_idx = min(len(self.history) -1, self.curr_idx + steps)
        return self.history[self.curr_idx]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)