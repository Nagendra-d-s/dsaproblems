class MinStack(object):

    def __init__(self):
        self.s=[]
        self.mini=[]
    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        if not self.mini or value<=self.mini[-1]:
            self.mini.append(value)
        self.s.append(value)

    def pop(self):
        """
        :rtype: None
        """
        if not self.s:
            return None
        value = self.s.pop()
        if value==self.mini[-1]:
            self.mini.pop()
        return value

    def top(self):
        """
        :rtype: int
        """
        if not self.s:
            return None
        return self.s[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if not self.mini:
            return None
        return self.mini[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()