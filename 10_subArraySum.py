class Solution:
     def subarraySum(self, nums: List[int], k: int) -> int:
        ans = s = 0
        cnt = defaultdict(int)
        for i in nums:
            cnt[s] += 1
            s += i
            ans += cnt[s - k]
        return ans
     
# Time Complexity: O(n)