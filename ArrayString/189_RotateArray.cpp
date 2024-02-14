class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = k % nums.size();
        int tmp = 0;
        for(int i =0, j = nums.size() -  n - 1;i<j;i++,j--) {
            tmp = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;
        }
        for(int i = nums.size() -  n , j = nums.size()-1;i<j;i++,j--) {
            tmp = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;
        }
        for(int i = 0, j = nums.size() - 1 ; i < j ;i++, j--) {
            tmp = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;
        }
    }
};