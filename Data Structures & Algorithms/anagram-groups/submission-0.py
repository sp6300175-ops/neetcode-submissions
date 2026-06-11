class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            key = tuple(sorted(i))
            if key not in d:
                d[key] = []
            d[key].append(i)
        return list(d.values())
         