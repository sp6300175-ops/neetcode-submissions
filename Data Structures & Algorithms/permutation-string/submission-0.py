from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count1 = Counter(s1)
        count2 = Counter(s2[0 : len(s1)])

        if count1 == count2:
            return True

        for right in range(len(s1), len(s2)):

            count2[s2[right]] += 1
            count2[s2[right - len(s1)]] -= 1

            if count1 == count2:
                return True
            
        return False


