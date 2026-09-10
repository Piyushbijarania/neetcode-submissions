class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # l = 0
        # r = l + 1
        # res = 0
        # countS = {}
        # for r in range(len(s)):
        #     if s[l] == s[r]:
        #         length = r - l + 1
        #         res = max(res, length)
        #         r += 1
        #     elif s[l] != s[r] and k > 0:
        #         k -= 1
        #         length = r - l + 1
        #         res = max(res, length)
        #         r += 1
        #     else:
        #         l = r
        #         r = r + 1
        
        # return res
        

        res = 0
        windowSize = 0
        countS = {}
        l = 0
        r = 0
        for r in range(len(s)):
            countS[s[r]] = 1 + countS.get(s[r], 0)
            
            while (r - l + 1) - max(countS.values()) > k:
                countS[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res


