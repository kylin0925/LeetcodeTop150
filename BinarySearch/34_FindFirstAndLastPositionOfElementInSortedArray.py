class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def binarySearch(nums,start,end,target):
            while start < end:
                #print(start,end)
                mid = start + int((end - start)/2)
                if nums[mid] >= target:
                    end = mid
                else:
                    start = mid+1
            return start
        nums_len = len(nums)
        if nums_len<0:
            return [-1, -1]
        s = binarySearch(nums,0,nums_len,target)
        #print(s)
        if s==nums_len or nums[s]!=target:
            return [-1,-1]
        s2 = binarySearch(nums,0,nums_len,target+1)-1
        #print(s2)
        return [s,s2]