class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            c = s[0:i] + s[i+1:]

            if c == c[::-1]:
                return True
        return False
        