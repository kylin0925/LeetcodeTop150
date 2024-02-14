class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(32):
            mask = 1 << i
            tmp = 0
            for n in nums:
                tmp += (n & mask) !=0
                #print(n, mask, n & mask)
            tmp = tmp % 3
            cnt = cnt | (tmp << i)
            #print(tmp, cnt)
        #print(hex(cnt),cnt - (1 << 32))
        if cnt & 1<<31 > 0:
            cnt = cnt - (1 << 32)
        return cnt