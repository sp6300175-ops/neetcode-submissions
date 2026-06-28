class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = s.strip().split()
        last = lst[-1]
        return len(last)