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
                while l < r and heights[l] <= height:
                    l += 1
            else:
                while l < r and heights[r] <= height:
                    r -= 1
            

        return store


        