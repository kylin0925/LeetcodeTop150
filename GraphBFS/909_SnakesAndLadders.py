class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        dir_map = {}
        num = 1
        dir = 0
        for i in range(n-1,-1,-1):
            if dir == 0:
                for j in range(n):
                    dir_map[num] = board[i][j]
                    num+=1
                dir = 1
            else:
                for j in range(n-1,-1,-1):
                    dir_map[num] = board[i][j]
                    num+=1
                dir = 0
        #for i in range(1, n*n + 1):
        #    print(i,dir_map[i])

        lv = 1
        next = 0
        q = deque([])
        q.append([1,0])
        target = n * n
        visit = {}
        visit[1] = 1
        while len(q) > 0:
            lbl = q.popleft()
            curr = lbl[0]
            lv = lbl[1]
            for i in range(curr + 1, min(curr + 6, target) + 1):
                next_pos = dir_map[i]
                if next_pos == target or i == target:
                    return lv + 1
                
                if next_pos == -1:
                    if i not in visit:
                        q.append([i, lv + 1])
                        visit[i] = 1
                else:
                    if next_pos not in visit:
                        q.append([next_pos, lv + 1])
                        visit[next_pos] = 1
            #print(q)
                
        return -1