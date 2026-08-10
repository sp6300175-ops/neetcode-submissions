from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0 or len(t) > len(s):
            return ""

        count1 = Counter(t)

        left = 0
        matched = 0
        required = len(Counter(t)) # len(set(t)) gives the same result
        window = Counter()
        best_so_far = float('inf')

        for right in range (0, len(s)):
            window[s[right]] += 1
            if s[right] in count1 and window[s[right]] == count1[s[right]]:
                matched += 1
            
            while matched == required:
                if (right - left + 1) < best_so_far:
                    best_so_far = right - left + 1
                    best_left = left
                    best_right = right

                if s[left] in count1 and window[s[left]] == count1[s[left]]:
                    matched -= 1
                window[s[left]] -= 1
                left += 1

        if best_so_far == float('inf'):
            return ""
        else:
            return s[best_left: best_right + 1]



