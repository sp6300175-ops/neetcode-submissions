class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        for i in range(len(s)-1):
            c = abs(ord(s[i+1]) - ord(s[i]))
            sum += c
        return sum
