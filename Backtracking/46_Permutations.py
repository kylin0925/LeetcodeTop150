class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        nums_len = len(nums)
        res = []
        flags = []
        def dfs(p,idx):

            if idx == nums_len:
                res.append([x for x in p])
                return
            for i in range(nums_len):
                if flags[i] == 0:
                    p[idx] =  nums[i]
                    flags[i] = 1
                    dfs(p,idx+1)
                    flags[i]=0
        p = [x for x in nums]
        flags = [0 for x in nums]
        dfs(p,0)
        #print(res)
        return res