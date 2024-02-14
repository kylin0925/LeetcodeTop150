class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """
        max_area = 0
        arr_len = len(height)
        for i in xrange(arr_len):
            for j in xrange(i+1,arr_len):
                a = (j-i) * min(height[i],height[j])
                if max_area < a:
                    max_area = a
        return max_area
        """
        max_area = 0
        arr_len = len(height)
        l = 0
        r = arr_len - 1
        
        while l < r:
            a = (r - l) * min(height[r],height[l])    
                     
            if a > max_area:
                max_area = a                
            if height[r] > height[l]:
                l +=1
            else:
                r -=1
            #print l,r 
        return max_area