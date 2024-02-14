class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = nums[0]
        min_sum = nums[0]
        curr_max = 0
        curr_min = 0
        total = 0

        for n in nums:
            total += n
            curr_max += n
            curr_min += n
            max_sum = max(curr_max, max_sum)
            min_sum = min(curr_min, min_sum)
            if curr_max < 0:
                curr_max = 0
            if curr_min > 0:
                curr_min = 0
        
        if total == min_sum:
            return max_sum
        else:
            return max(max_sum, total-min_sum)
        