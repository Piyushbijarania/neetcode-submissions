class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # hashStr = {}
        # l = 0
        # r = 0
        # maxLength = 0
        # for r in range(len(s)):
        #     while s[r] in hashStr:

        #         del hashStr[s[l]]
        #         l = l + 1
        #     hashStr[s[r]] = r
        #     length = r - l + 1
        #     maxLength = max(length, maxLength)
        #     # r += /1
            
        # return maxLength

        hashSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l += 1
            hashSet.add(s[r])
            res = max(res, r - l + 1)
        return res

        