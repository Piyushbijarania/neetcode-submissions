class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        store = 0
        while l < r:
            width = abs(l - r)
            height = min(heights[l], heights[r])
            store = max(store, (width * height))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return store


        