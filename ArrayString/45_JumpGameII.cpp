class Solution:
    def jump(self, nums: List[int]) -> int:
        farest = 0
        end = 0
        n = len(nums)
        jump = 0
        for i in range(n-1):
            farest = max(farest, i + nums[i])
            if i == end:
                jump += 1
                end = farest
        return jump
        