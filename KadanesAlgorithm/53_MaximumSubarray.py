class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]#max(nums)
        curr_sum = 0
        for n in nums:
            curr_sum += n
            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum < 0 :
                curr_sum = 0
        return max_sum
