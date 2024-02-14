class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_num = len(nums)
        ans = [1] * len_num
        
        
        for i in range(1,len_num):            
            ans[i] = ans[i-1] * nums[i-1]
        
        print(ans)
        prod = 1
        for i in range(len_num-2,-1,-1):
            ans[i] *= prod * nums[i+1]
            prod = prod * nums[i+1]
        
        return ans
'''
       1 1  2 6 24  1
       1 24 24 12 4 1
'''