class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i = 0;
        int j = 0;
        int n = nums.size();
        while(j<n){
            int tmp = nums[j];
            int cnt = 0;
            while(j < n && nums[j]==tmp){
                j++;
                cnt++;
            }
            //cout << "cnt " << cnt << "j " << j << endl;
            if(cnt>=2){
                nums[i] = tmp;
                nums[i+1] = tmp;
                i+=2;
            }else{
                nums[i] = tmp;
                i++;
            }

        }
        return i;
    }
};