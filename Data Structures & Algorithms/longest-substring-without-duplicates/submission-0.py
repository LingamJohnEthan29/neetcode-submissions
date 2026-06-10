class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = 0
        l = 0
        n = len(s)
        maxLen = 0
        seen = set()
        while r < n and l < n:
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
            else:
                maxLen = max(maxLen, r-l)
                seen.remove(s[l])
                l += 1
        maxLen = max(maxLen, r-l)
        return maxLen