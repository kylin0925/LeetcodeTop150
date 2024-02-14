class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tbl=[-1]*256
        los = 0
        cnt = 0
        start = 0
        for i in range(len(s)):
            
            tmp = ord(s[i])
            
            if tbl[tmp] == -1:
                cnt+=1
                tbl[tmp]=i
            else:
                if start > tbl[tmp]:
                    cnt+=1
                    tbl[tmp]=i
                else:
                    #print(i,cnt)                 
                    cnt =i-tbl[tmp]
                    start = tbl[tmp]+1
                    tbl[tmp] = i                                    
            if cnt > los:
                los = cnt                
            #print(i,"cnt",cnt,start)
                   
        return los
        
        
        