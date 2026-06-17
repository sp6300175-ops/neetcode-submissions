class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l = []
        for i in range(len(operations)):
            if operations[i] =='+':
                c = l[-1] + l[-2]
                l.append(c)
            elif operations[i] == 'C':
                l.pop()
            elif operations[i] == 'D':
                double = 2*l[-1]
                l.append(double)
            else:
                l.append(int(operations[i]))
        return sum(l)

                