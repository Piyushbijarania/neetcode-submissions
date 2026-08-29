class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countHash = {}
        ansArray = []
        for num in nums:
            countHash[num] = countHash.get(num, 0) + 1
        for num, cnt in countHash.items():
            ansArray.append([cnt, num])
        ansArray.sort()
        res = []
        while len(res) < k:
            res.append(ansArray.pop()[1])
        return res


        