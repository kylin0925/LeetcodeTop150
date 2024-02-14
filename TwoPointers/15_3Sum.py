class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        res = []
        #print nums
        
        i = 0
        while i < n-2:
            target = -nums[i]
            start = i + 1
            end = n-1
            #print i,start,end
            while start < end :
                tmp = nums[start] + nums [end]
                #print start,end," tmp ",tmp
                if tmp > target:
                    end-=1
                elif tmp < target:
                    start +=1
                else:
                    tmp = [nums[i] , nums[start] , nums[end]]              
                    res.append(tmp)
                    while start<end and nums[start]== nums[start+1]:
                        start+=1
                    while end>start and nums[end]== nums[end-1]:
                        end-=1    
                    start+=1
            
            while i<n-1 and nums[i]== nums[i+1]:
                i +=1
            i+=1    
        return res