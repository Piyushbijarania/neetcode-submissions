class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashone = {}
        hashtwo = {}

        if len(s) != len(t):
            return False
        

        for i in s:
            hashone[i] = hashone.get(i, 0) + 1
        for i in t:
            hashtwo[i] = hashtwo.get(i, 0) + 1

        if hashone == hashtwo :
            return True
        else:
            return False