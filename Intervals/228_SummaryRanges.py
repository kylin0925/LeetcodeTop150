class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) ==0:
            return []
        ans=[]
        s = t = nums[0]
        fstr="{start}->{end}"
        for i in range(1, len(nums)):
            if nums[i] == t+1:
                t=nums[i]
            else:
                if s!=t:
                    ans.append(f"{s}->{t}")
                else:
                    ans.append(f"{s}")
                s=t=nums[i]
        if s!=t:
            ans.append(f"{s}->{t}")
        else:
            ans.append(f"{s}")
        return ans
                
        