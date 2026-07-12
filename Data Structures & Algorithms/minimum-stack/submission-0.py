class MinStack:

    def __init__(self):
        self.lst = []
        self.min_lst = []

    def push(self, val: int) -> None:
        self.lst.append(val)
        if self.min_lst:
            self.min_lst.append(min(val,self.min_lst[-1]))
        else:
            self.min_lst.append(val)

    def pop(self) -> None:
        self.min_lst.pop()
        return self.lst.pop()

        

    def top(self) -> int:
        if len(self.lst) ==  0:
            return None
        else:
            return self.lst[-1]
        

    def getMin(self) -> int:
        return self.min_lst[-1]
        
