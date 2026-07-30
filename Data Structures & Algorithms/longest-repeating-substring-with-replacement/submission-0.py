class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        left = 0
        max_freq = 0
        max_len = 0
        count = 1

        for right in range(len(s)):
            if s[right] in window:
                window[s[right]] += 1
            else:
                window[s[right]] = 1

            max_freq = max(max_freq, window[s[right]])

            if (right - left + 1) - max_freq > k: # window_size is right - left + 1
                window[s[left]] -= 1 # we remove the leftmost character as window becomes invalid
                left += 1 # we shrink the size of the window
            max_len = max(max_len, right - left + 1)

        return max_len