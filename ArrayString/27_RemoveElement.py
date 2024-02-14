class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        last = len(nums) - 1
        cnt = 0
        while i <= last:
            if nums[i] == val:
                nums[i], nums[last] = nums[last], nums[i]
                last -=1
            if nums[i] !=val:
                i+=1
                cnt+=1
            print(i,cnt)
        return cnt