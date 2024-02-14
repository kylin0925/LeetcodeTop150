class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        c = 1
        ans = 0
        print(nums)
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] +1:
                c+=1
            else:
                ans = max(ans,c)
                #c=1
                if nums[i] != nums[i-1] :
                    c=1
            #print(c)
        
        return max(ans,c)
    