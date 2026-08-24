class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = [(p, float(target - p)/s) for p, s in zip(position, speed)]
        pair.sort(key = lambda x : x[0], reverse = True)
        stack = []

        for i in pair:
            if len(stack) == 0 or i[1] > stack[-1]:
                stack.append(i[1])
            
        return len(stack)