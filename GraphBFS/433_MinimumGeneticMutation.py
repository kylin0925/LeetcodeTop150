class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def diff_gene(agene,bgene):
            cnt = 0
            a = list(agene)
            b = list(bgene)
 
            for i in range(8):
                if a[i]!=b[i]:
                    cnt+=1
            #print(a, b, cnt)
            return cnt

        g = defaultdict(list)
        n = len(bank)
        for i in range(n):
            if diff_gene(startGene,bank[i]) == 1:
                g[startGene].append(bank[i])
            for j in range(i+1,n):                
                if diff_gene(bank[i],bank[j]) == 1:
                    g[bank[i]].append(bank[j])
                    g[bank[j]].append(bank[i])
        visit = {}        
        #print(g)
        lv = 1
        q = deque([])
        q.append([startGene, 0])
        #visit[startGene] = 1
        while len(q) > 0:
            gene = q.popleft()
            if gene[0] in g and gene[0] not in visit :
                visit[gene[0]] = 1
                neighbors = g[gene[0]]
                for neighbor in neighbors:
                    #print(neighbor)
                    if neighbor == endGene:
                        return gene[1] + 1
                    else:
                        q.append([neighbor, gene[1] + 1])
            #print(q)
        return -1