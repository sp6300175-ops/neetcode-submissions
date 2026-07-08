class MyStack:

    def __init__(self):
        self.lst = []

    def push(self, x: int) -> None:
        self.lst.append(x)

    def pop(self) -> int:
        if len(self.lst) == 0:
            return None
        else:
            return self.lst.pop(-1)

    def top(self) -> int:
        if len(self.lst) == 0:
            return None
        else:
            return self.lst[-1]

    def empty(self) -> bool:
        if len(self.lst) == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()