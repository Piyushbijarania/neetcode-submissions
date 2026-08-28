class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashM = {}
        ans = []
        for i in strs:
            ii = "".join(sorted(i))
            hashM.setdefault(ii, []).append(i)
        return list(hashM.values())


        