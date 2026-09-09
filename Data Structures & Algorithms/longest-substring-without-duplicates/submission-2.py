class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # hashStr = {}
        # l = 0
        # r = 0
        # maxLength = 0
        # while r < len(s):
        #     if s[r] not in hashStr:
        #         hashStr[s[r]] = r
        #         length = (r + 1) - l
        #         maxLength = max(length, maxLength)
        #         r += 1
        #     else:
        #         while s[r] not in hashStr:
        #             del hashStr[s[l]]
        #             l = l + 1
                    
        #         r += 1
        
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

        