class Solution:
    def trap(self, height: List[int]) -> int:
        cnt = 0
        start =0
        height_num = len(height)


        while(start < height_num):
            h = 0
            end = start+1
            pos = -1
            while end < height_num:
                if height[end] > height[start]:
                    pos = end
                    break
                end+=1
            if end == height_num:
                end = start + 1
                pos = end
                while end < height_num:
                    if height[end] > h:
                        h = height[end]
                        pos = end
                    end+=1
            if start < height_num and pos < height_num:
                #print(start,pos,height[start],height[pos])

                tmph = min(height[start],height[pos])
                if tmph!= 0:
                    for i in range(start+1,pos):
                        cnt+=tmph-height[i]
                #print(tmph,cnt)
            start=pos
        return cnt