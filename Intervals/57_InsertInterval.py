class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        i = 0
        intervals.append(newInterval)
        cnt = len(intervals)
        
        if cnt ==0:
            return newInterval
        if len(newInterval) == 0:
            return intervals
        
        intervals.sort()    
        print(intervals)
        tmp = intervals[i]
        tmp[1] = max(tmp[1],intervals[i][1])
        
        print(tmp)
       
        i+=1       
        while i < cnt:   
            
            if tmp[0] <= intervals[i][0] and tmp[1] >= intervals[i][0]:
           
                tmp[1] = max(tmp[1],intervals[i][1])
        
            else:
                #print(i,tmp)
                res.append([tmp[0],tmp[1]])
                tmp[0] = intervals[i][0]
                tmp[1] = intervals[i][1]
        
                  
            i+=1
        res.append([tmp[0],tmp[1]])
        return res