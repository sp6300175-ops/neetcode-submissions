class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        alive = True
        for i in asteroids:
            alive = True
            while len(stack) != 0 and stack[-1] > 0 and i < 0:
                if abs(i) == abs(stack[-1]):
                    stack.pop()
                    alive = False
                    break
                elif abs(i) < abs(stack[-1]):
                    alive = False
                    break
                else:
                    stack.pop()

            if alive:
                stack.append(i)   
                
        return stack      