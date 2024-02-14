import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        minq = []
        maxq = []
        heapq.heapify(minq)
        heapq.heapify(maxq)
        cnt = 0
        stop = False
        for n1 in nums1:
            
            for n2 in nums2:
                if cnt < k:
                    heapq.heappush(minq,[n1+n2,n1,n2])
                    heapq.heappush(maxq,[-1*(n1+n2),n1,n2])
                    cnt+=1
                else:
                    if n1+n2 <= -maxq[0][0]:
                        heapq.heappush(minq, [n1 + n2, n1, n2]  )
                        heapq.heappop(maxq)
                        heapq.heappush(maxq, [-1*(n1 + n2), n1, n2])
                    else:

                        break

        ans=[]
        cnt = 0
        while len(minq)>0 and cnt<k:
            ans.append([minq[0][1],minq[0][2]])
            heapq.heappop(minq)
            cnt+=1
        return ans