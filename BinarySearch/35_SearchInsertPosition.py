class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int start = 0;
        int end = nums.size();
        int m = 0;
        while(start < nums.size() && start <=end ){            
            
            m = (start + end) >> 1;
            //cout << start << " " << m << " " << end << "\n";
            if(nums[m] == target)   
                return m;
            if(nums[m]>target){
                end = m-1;
            }else{
                start = m+1;
            }
        }
        return start;
    }
};