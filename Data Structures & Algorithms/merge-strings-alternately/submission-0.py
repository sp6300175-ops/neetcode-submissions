class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = 0
        right = 0
        new = ''

        while left < len(word1) and right < len(word2):
            new += word1[left] 
            new += word2[right]
            left += 1
            right += 1
        if left < len(word1):
            new += word1[left :]
        else:
            new += word2[right :]

        return new



        