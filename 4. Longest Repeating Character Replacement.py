class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        charmap={}
        left = 0
        right = 0
        for right in range(len(s)):
            charmap[s[right]]=charmap.get(s[right],0)+1
            max_len=max(max_len, charmap[s[right]])
            if (right-left+1)-max_len>k:
                charmap[s[left]]-=1
                left+=1
        return (right-left+1)
