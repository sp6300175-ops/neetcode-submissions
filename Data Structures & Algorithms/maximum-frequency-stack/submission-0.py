class FreqStack:

    def __init__(self):
        self.count = {}
        self.stacks = {}
        self.highest = 0

    def push(self, val: int) -> None:
        if val not in self.count:
            self.count[val] = 0
        self.count[val] += 1
        c = self.count[val]

        if c not in self.stacks:
            self.stacks[c] = []
        self.stacks[c].append(val)

        if c > self.highest:
            self.highest = c

    def pop(self) -> int:
        val = self.stacks[self.highest].pop()
        self.count[val] -= 1
        if len(self.stacks[self.highest]) == 0:
            self.highest -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()