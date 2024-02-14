class Solution:
    def reverseBits(self, n: int) -> int:
        mask = 1 << 31
        idx = 0
        ans = 0 
        for i in range(32):
            #print(bin(mask), bin(n & mask))            
            if n & mask >0:
                ans |= 1<<idx
                print(ans,idx)
            idx+=1
            mask >>= 1
            
        return ans