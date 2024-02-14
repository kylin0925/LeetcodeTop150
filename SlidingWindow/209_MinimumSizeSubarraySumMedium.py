class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix = [0]
        acc = 0
        for n in nums:
            acc+=n
            prefix.append(acc)
        print(prefix)
        if prefix[-1] < target:
            return 0
        l = 0
        r = 1
        min_len = len(nums)+1
        while l < len(nums) + 1:
            print(l,r)
            tmp = prefix[r] - prefix[l]
            if tmp < target:
                r+=1
                if r > len(nums) :
                    break
            else:
                if min_len > r-l:
                    min_len = r-l
                l+=1
        return min_len