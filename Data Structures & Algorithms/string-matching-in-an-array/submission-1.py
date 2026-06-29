class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        lst = []
        for word in words:
            for other_word in words:
                if word in other_word and word != other_word:
                    lst.append(word)
                    break
        return lst