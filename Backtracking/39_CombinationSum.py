class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        arr_len = len(candidates)
        combinations = []
        candidates.sort()
        def dfs(idx,start,now):
            #print(combinations)
            num_map = {}
            if now == target:
                #print(idx,combinations)
                res.append([x for x in combinations])
                return
            if now > target:
                return
            now_num = candidates[start] -1
            for i in range(start,arr_len):
                if now_num != candidates[i] and candidates[i]!=0:
                    now_num = candidates[i]
                    combinations.append(candidates[i])
                    dfs(idx+1,i,now+candidates[i])
                    combinations.pop()
        dfs(0,0,0)
        return res
        