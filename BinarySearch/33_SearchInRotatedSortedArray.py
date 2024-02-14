class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        def binarySearch(target,nums,start,end):
            while start <= end:
                mid = start + int((end-start)/2)
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    start = mid +1
                else:
                    end = mid-1
            return -1
        left =0
        nums_len = len(nums)
        if nums_len == 0:
            return -1
        right = nums_len -1
        # find smallest nums
        mid = 0
        while left < right:
            mid = int((right + left)/2)
            if nums[mid] > nums[right]:
                left = mid +1
            else:
                right=mid
        #print(nums,"debug mid is ",left, mid)

        right = nums_len - 1
        if target >= nums[left] and target <= nums[right]:
            ans = binarySearch(target,nums,left,right)
        else:
            ans =binarySearch(target,nums, 0,left-1)
        return ans