class Solution:
    def candy(self, ratings: List[int]) -> int:
        ll = [1] * len(ratings)
        rr = [1] * len(ratings)

        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                ll[i]=ll[i-1]+1


        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                rr[i] = rr[i+1] + 1


        ans = 0
        #print(ll,rr)
        for i in range(len(ratings)):
            ans += max(ll[i],rr[i])
        return ans
        