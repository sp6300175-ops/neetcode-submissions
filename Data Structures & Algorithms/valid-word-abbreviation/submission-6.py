class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        j, i = 0, 0
        num = 0
        while i < len(abbr):
    
            if abbr[i].isalpha():
                if j >= len(word):    
                    return False
                if abbr[i] != word[j]:
                    return False
                i += 1
                j += 1
            
            elif abbr[i].isdigit():
                if abbr[i] == '0' and num == 0:
                    return False
                num = num * 10 + int(abbr[i])
                i += 1
                if i == len(abbr) or not abbr[i].isdigit():
                    j += num
                    num = 0
            
        return i == len(abbr) and j == len(word)