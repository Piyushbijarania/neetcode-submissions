class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, n in enumerate(nums):
            A.append([n, i])
        A.sort()
        i = 0
        j = len(nums) - 1
        while i < j:
            curr = A[i][0] + A[j][0]
            if curr == target:
                return [min(A[i][1], A[j][1]), max(A[i][1],A[j][1])]
            elif curr < target:
                i += 1
            else:
                j -= 1
        return []
