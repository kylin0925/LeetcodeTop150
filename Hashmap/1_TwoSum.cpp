class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans;
        unordered_map<int, vector<int>>  num_map ;
        int tmp = 0;
        for(int i =0 ; i<nums.size(); i++){
            tmp = target-nums[i];
            if(num_map.find(tmp) == num_map.end()){
                vector<int> v = {i};
                num_map[tmp]=v;
            }else{
                vector<int> v = num_map[tmp];
                v.push_back(i);
                num_map[tmp]=v;
            }
        }
        
        for(int i = 0; i<nums.size(); i++){
            if(num_map.find(nums[i])!=num_map.end()){
                vector<int> v = num_map[nums[i]];
                for(int j:v){
                    if(j!=i){
                        ans.push_back(i);
                        ans.push_back(j);
                        return ans;
                    }
                }
            }
        }
        return ans;
    }
};