class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        hours = 0
        while left < right:
            mid = (left + right) // 2
            for p in piles:
                hours = hours + ((p + mid - 1) // mid)
            if hours <= h:
                hours = 0
                right = mid
            else:
                hours = 0
                left = mid + 1
        return right
