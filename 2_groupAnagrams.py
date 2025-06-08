class Solution:
    def groupAndgrams(self, strs):
        anagrams = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(s)
        
        return list(anagrams.values())
    
# time complexity: O(n * k log k)