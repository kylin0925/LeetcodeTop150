class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        length = [1]
        length[0] = nums[0]
        for i in range(1,len(nums)):
            #bin search
            l = 0
            r = len(length) -1
            while l <= r:
                m = (l + r)//2
                #print("l", l, "r", r, "m", m, length)
                if length[m] < nums[i]:
                    l = m+1
                else:
                    r = m -1

            if l >= len(length):
                length.append(nums[i])
            else:
                length[l] = nums[i]
        #print(length)
        return len(length)