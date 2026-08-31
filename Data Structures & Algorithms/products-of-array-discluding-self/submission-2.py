class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        ans = []
        zero = 0
        for i in nums:
            if i == 0:
                zero = zero + 1
                continue
            mul = mul * i

        if zero == 1:
            for i in nums:
                if i == 0:
                    ans.append(mul)
                else:
                    ans.append(0)
            return ans
        elif zero >= 2:
            return [0]*len(nums)
        for i in nums:
            anss = mul // i
            ans.append(anss)
        return ans