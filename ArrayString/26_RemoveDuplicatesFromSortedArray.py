class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        for j in range(1, n):
            #print(nums[i], nums[j])
            if nums[j]!= nums[i]:
                i+=1
                nums[i] = nums[j]
        return i+1