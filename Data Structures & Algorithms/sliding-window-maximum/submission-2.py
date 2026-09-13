class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # res = []
        # l = 0 
        # r = 0 
        # hashmax = {}
        # for r in range(len(nums)):
        #     hashmax[r] = nums[r]
        #     if (r - l + 1) == k:
        #         res.append(max(hashmax.values()))
        #         del hashmax[l]
        #         l += 1

        # return res

        res = []
        q = collections.deque()
        for r in range(len(nums)):
            if q and q[0] < r - k + 1:
                q.popleft()
            
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if r >= k - 1:
                res.append(nums[q[0]])
            
        return res
