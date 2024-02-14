class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """ 
        nums_len = len(numbers)
        start = 0
        end = nums_len -1
        if start == end:
            return numbers
            
        while start < end:
            if numbers[start] + numbers[end] <target:
                start +=1
            elif numbers[start] + numbers[end] > target:    
                end -=1
            else:
                return [start+1,end+1]
        return []