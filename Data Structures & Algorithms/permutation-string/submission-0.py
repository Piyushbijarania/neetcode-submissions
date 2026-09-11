class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = {}
        countS2 = {}
        lengthS1 = len(s1)
        l = 0
        # ans = bool
        # r = lengthS1 - 
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            countS1[s1[i]] = 1 + countS1.get(s1[i], 0)
        for r in range(len(s2)):
            countS2[s2[r]] = 1 + countS2.get(s2[r], 0)
            if (r - l + 1) == lengthS1:
                if countS1 == countS2:
                    return True
                elif countS1 != countS2:
                    countS2[s2[l]] -= 1
                    if countS2[s2[l]] == 0:
                        del countS2[s2[l]]
                    l += 1
        return False
            





        