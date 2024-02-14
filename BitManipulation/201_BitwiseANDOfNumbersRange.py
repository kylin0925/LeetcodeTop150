class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        int bit=0;
        unsigned int mask = 1<<31;
        int tmp = 0;
        for(int i = 0;i<32;i++){
            int l = (mask & left);
            int r = (right & mask);
            if( l && r){
                bit|=mask;
                //cout << bit << endl;
            }else{
                if(r > l)
                    break;
            }
            mask >>=1;
        }
        return bit;
    }
};