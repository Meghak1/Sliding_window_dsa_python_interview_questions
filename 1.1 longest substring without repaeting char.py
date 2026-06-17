class Solution:
    def longestSubstring(self, s: str) -> str:
        left = 0
        max_len = 0
        start = 0
        charset = set()

        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left += 1

            charset.add(s[right])

            if right - left + 1 > max_len:
                max_len = right - left + 1
                start = left

        return s[start:start + max_len]


# Example
s = "abcabcbb"
print(Solution().longestSubstring(s))
