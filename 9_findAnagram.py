class Solution:
    def findAnagrams(self, s: str, p: str):
        m, n = len(s), len(p)
        if m < n:
            return []
        
        # Initialize frequency arrays
        count = [0] * 26
        for char in p:
            count[ord(char) - ord('a')] += 1

        res = []
        l = 0
        # Sliding window to find anagrams
        for r in range(m):
            count[ord(s[r]) - ord('a')] -= 1

            # If the count goes negative, move the left pointer
            while count[ord(s[r]) - ord('a')] < 0:
                count[ord(s[l]) - ord('a')] += 1
                l += 1
                
            # If the window size matches the length of p, we found an anagram
            if r - l + 1 == n:
                res.append(l)

        return res
    
# time complexity: O(m + n)