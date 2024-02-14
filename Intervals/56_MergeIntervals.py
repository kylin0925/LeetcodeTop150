class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 1
        cnt = len(intervals)
        if cnt ==0:
            return []
        tmp = intervals[0]
        res=[]
        print(tmp)
        while i < cnt:   
            
            if tmp[0] <= intervals[i][0] and tmp[1] >= intervals[i][0]:
                # overlap                
                tmp[1] = max(tmp[1],intervals[i][1])
        
            else:
                #print(i,tmp)
                res.append([tmp[0],tmp[1]])
                tmp[0] = intervals[i][0]
                tmp[1] = intervals[i][1]
        
                  
            i+=1
        res.append([tmp[0],tmp[1]])            
        return res
                