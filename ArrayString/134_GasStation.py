class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        ngas = len(gas)
        old=[-1,-1]
        i=0
        while i < ngas:
            #print(i,old)
            if gas[i] >= cost[i] :
                tank=0
                j=i
                
                for k in range(ngas):
                    if tank+gas[j] < cost[j]:
                        break
                    tank=tank+gas[j]-cost[j]
                    #print(j,tank)
                    j = (j+1) % ngas
                    
                #print(i,"end",j,tank,cost[j])
                if j == i:
                    return i
                if i < j:
                    i=j
                else:
                    break
            else:
                i+=1
            
                           
        return -1
        