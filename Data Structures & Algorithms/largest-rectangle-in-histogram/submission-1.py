class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        right_arr = [0]*len(heights)
        stack = []
        for i in range(len(heights) - 1, -1, -1):
            while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not(stack):
                stack.append(i)
                right_arr[i] = len(heights)
            else:
                right_arr[i] = stack[-1]
                stack.append(i)
        left_arr = [0] * len(heights)
        lstack = []
        for i in range(len(heights)):
            while lstack and heights[lstack[-1]] >= heights[i]:
                lstack.pop()
            if not(lstack):
                lstack.append(i)
                left_arr[i] = -1
            else:
                left_arr[i] = lstack[-1]
                lstack.append(i)

        # width = r - l - 1
        max_area = 0
        for i in range(len(heights)):
            curr_area = heights[i] * (right_arr[i] - left_arr[i] - 1)
            max_area = max(curr_area, max_area)
        return max_area

        
        