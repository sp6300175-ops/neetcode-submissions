class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ''
        for index in range (len(min(strs))):
            char = strs[0][index]
            for word in strs:
                if word[index] != char:
                    return s
            s+=char
        return s    
