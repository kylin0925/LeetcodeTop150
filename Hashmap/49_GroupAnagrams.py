class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = {}
        for word in strs:
            tmp = list(word)
            tmp.sort()
            tmp2 = "".join(tmp)
            if str_map.get(tmp2) == None:
                str_map[tmp2] = [word]
            else:
                tmp3 = str_map[tmp2]
                tmp3.append(word)
                str_map[tmp2] = tmp3
        #print(str_map)                
        ans = []    
        for key in str_map.keys():
            ans.append(str_map[key])
        return ans            
            
            